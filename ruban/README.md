# HYPNOGEN — ruban LED piloté par le téléphone

Croquis **HypnoGenRuban** pour la carte HYPNOGEN (Arduino Nano ESP32, ruban RGB 12 V sur 3 MOSFET,
PWM R/V/B = D2/D3/D4). Le téléphone garde l'interface et le son ; la carte ne fait que la lumière,
par Bluetooth basse consommation. **Tout fonctionne hors ligne.**

C'est ce qui permet le gamma : un écran de téléphone à 60 i/s ne rend pas un 40 Hz propre, le PWM du ruban si.

## Mise en route

1. Arduino IDE, paquet **esp32** d'Espressif (2.x ou 3.x), carte **Arduino Nano ESP32**,
   Pin Numbering « By Arduino pin » (défaut). Aucune bibliothèque à installer.
2. Ouvrir `HypnoGenRuban/HypnoGenRuban.ino` et téléverser. Le moniteur série (115 200 bauds) affiche
   `HYPNOGEN-RUBAN pret`.
3. Témoin de la carte : clignote en attente, fixe quand le téléphone est connecté.
4. Dans l'appli (v1.9 et plus) : Réglages → Ruban LED → Connecter → choisir **HYPNOGEN-RUBAN**.
   Chrome sur Android uniquement (Safari iPhone n'a pas Bluetooth web).
5. Caler le ruban une fois par sortie audio : ruban connecté, « Caler cette sortie ».

Ce croquis remplace le firmware principal sur la carte (pas d'OLED, pas d'encodeurs, pas de son) :
c'est la carte « lumière » du téléphone. L'intégrer plus tard comme mode du firmware HypnoGenNano
revient à reprendre `ruban_core.h` et le service GATT tels quels.

## Principe

Le téléphone n'envoie pas un ordre par flash (l'intervalle de connexion BLE, 7,5–30 ms, dépasse la
période à 40 Hz). Il envoie la **phase du battement**, 0,8 s à l'avance, par nœuds de 50 ms datés sur
l'horloge de la carte. La carte interpole la phase entre deux nœuds et calcule la lumière à 1 kHz.
L'horloge commune vient d'allers-retours SYNC (le plus court des 12 derniers, recalé chaque seconde).

Format des nœuds, commandes et UUID : en tête de `ruban_core.h` et de `HypnoGenRuban.ino`.

## Sécurités appliquées par la carte, quoi que demande le téléphone

| Règle | Valeur |
|---|---|
| Puissance maximale du ruban | 50 % (`LUM_MAX`) |
| 14 → 15 Hz | fondu vers les plafonds bêta |
| 15 – 26,5 Hz (bêta) | lumière ≤ 40 %, profondeur ≤ 50 %, sinus imposé |
| 26,5 – 33,5 Hz | **lumière coupée** |
| 33,5 – 46,5 Hz (gamma) | lumière ≤ 50 % |
| au-delà de 46,5 Hz | lumière coupée |
| Durée | filet : 11 min de bêta, 21 min de gamma par séance |
| Liaison perdue ou nœuds manquants | extinction en 0,3 s |
| Appui sur l'écran du téléphone | extinction en 30 ms |

La fréquence est **déduite de la pente de la phase reçue**, jamais lue dans un champ : un téléphone
défaillant ne peut pas annoncer « 10 Hz » en envoyant du 20 Hz. Les coupures ont 1,5 Hz de marge sur
celles de l'appli (25, 35, 45 Hz), parce que l'appli peut faire glisser l'horloge de 2 % au plus pour
absorber ses recalages.

## Tests

```
cd test
g++ -O2 -std=c++17 test_ruban.cpp -o t && ./t          # 18 contrôles du noyau
g++ -O2 -std=c++17 rejouer.cpp -o r && ./r noeuds.hex  # rejoue des nœuds captés depuis l'appli
```

## Pas encore vérifié sur la carte

Le croquis n'a pas été compilé avec la chaîne ESP32 (seulement contre des en-têtes imitant les API 2.x
et 3.x). Points à contrôler au premier téléversement :

- si `BLE2902` provoque une erreur avec un paquet esp32 récent, supprimer la ligne `addDescriptor` ;
- mesurer au téléphone la précision de synchro affichée (attendu : quelques millisecondes) ;
- vérifier à l'oscilloscope sur D2 un 40 Hz propre en séance GAMMA, et l'extinction en coupant le Bluetooth du téléphone.
