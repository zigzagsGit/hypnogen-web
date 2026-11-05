# HYPNOGEN

Application web installable (Android, iPhone, PC Windows, Mac et Linux) qui reprend le générateur hypnagogique HYPNOGEN
(ESP32) : son binaural sur une porteuse de 200 Hz et lumière clignotante plein écran,
synchronisés sur une même phase de battement.

Tout se passe sur l'appareil. Les réglages et les calages de latence sont enregistrés dans son
navigateur.

L'application reconnaît seule la plate-forme (système, téléphone ou ordinateur, navigateur, application
installée ou non) et s'y adapte : commandes tactiles ou clavier et souris, conseils de réglage propres au
système, section « Votre appareil » dans l'aide. La plate-forme détectée est affichée sous « Avant de commencer ».

> **Avertissement** : lumière clignotante rythmée, contre-indiquée en cas d'épilepsie ou de
> photosensibilité. Par défaut, toutes les séances restent sous 14 Hz ; la zone bêta (15–25 Hz) ne s'ouvre
> qu'à part, avec une lumière bridée. Ce n'est pas un dispositif médical.

## Utiliser l'application

L'application est publiée par GitHub Pages à l'adresse :

```
https://zigzagsgit.github.io/hypnogen-web/
```

### L'installer

- **Android (Chrome)** : ouvrir l'adresse, puis menu ⋮ → « Installer l'application » (ou « Ajouter à l'écran d'accueil »).
- **iPhone (Safari)** : ouvrir l'adresse, bouton Partager → « Sur l'écran d'accueil ».
- **PC Windows, Linux, Mac (Chrome ou Edge)** : icône d'installation dans la barre d'adresse. L'application s'ouvre dans sa propre fenêtre.
- **Mac (Safari)** : Fichier → « Ajouter au Dock ». Firefox n'installe pas les applications web, mais l'application y fonctionne dans un onglet.

Une fois installée, elle s'ouvre en plein écran et fonctionne sans réseau (après une première ouverture avec réseau).

### Utilisation

- **Casque stéréo obligatoire** : le battement binaural n'existe pas sur un haut-parleur.
- Luminosité au maximum, luminosité automatique, True Tone / Night Shift, Confort des yeux ou éclairage nocturne coupés.
- **Sur ordinateur** : yeux fermés face à l'écran, à 40–60 cm ; la fenêtre passe en plein écran pendant la séance.
  Espace (ou un clic) coupe la lumière, R la rallume, ← → changent la fréquence de ±0,5 Hz en manuel, Échap arrête
  (quitter le plein écran arrête aussi la séance). Au calage et à la mesure, Espace remplace l'appui sur l'écran.
- 11 séances à profil (RELAXATION, HYPNAGOGIE, ENDORMISSEMENT…), durée de 10 à 60 min.
- Mode **PROFIL** (la séance pilote la fréquence) ou **MANUEL** (fréquence fixe de 0,5 à 14 Hz).
- **Zone bêta** (Réglages, fermée par défaut) : s'ouvre après 3 séances notées d'au moins 10 min et un questionnaire
  dédié. Elle donne accès à la séance CONCENTRATION et au manuel jusqu'à 25 Hz. Au-dessus de 14 Hz : lumière ≤ 40 %,
  profondeur ≤ 50 %, sinus imposé, 10 min au plus par séance, lumière coupée si l'écran tourne sous 50 i/s.
- **Ruban LED** (Réglages, Chrome ou Edge sur Android, Windows, Mac ; Chrome avec option expérimentale sous Linux ; jamais sur iPhone) : le téléphone pilote le ruban de la carte HYPNOGEN par Bluetooth
  basse consommation, hors ligne. Toute la lumière passe alors par le ruban, l'écran reste noir.
  Firmware et protocole : dossier [`ruban/`](ruban/README.md).
- **GAMMA** (zone bêta + ruban) : palier à 40 Hz, son isochrone imposé, lumière ≤ 50 %, 20 min au plus, yeux ouverts.
- **Calage** : on tape l'écran au rythme des clics, puis au passage de billes sur une ligne ; l'application en déduit
  le retard du son, puis on vérifie flash et clic ensemble (ajustement fin au curseur). Le retard est mémorisé par sortie audio (filaire, chaque casque Bluetooth).

## Contenu du dépôt

| Fichier | Rôle |
| --- | --- |
| `index.html` | L'application complète (interface, moteur de séances, audio, lumière). |
| `manifest.webmanifest` | Nom, couleurs et icônes pour l'installation. |
| `sw.js` | Service worker : fonctionnement hors ligne et mises à jour. |
| `icon-*.png`, `apple-touch-icon.png` | Icônes de l'application (Android, iPhone). |

## Publier une nouvelle version

1. Modifier `index.html` (et augmenter `VERSION` dans le script de l'application).
2. Augmenter `VERSION` dans `sw.js` avec la même valeur : c'est ce qui fait que les téléphones récupèrent la nouvelle version.
3. Pousser sur la branche `main`. GitHub Pages republie en une à deux minutes ; l'application installée se met à jour à l'ouverture suivante (parfois la deuxième).

## Mettre en place GitHub Pages (une seule fois)

Dans le dépôt sur GitHub : **Settings → Pages → Build and deployment** → Source « Deploy from a branch », branche `main`, dossier `/ (root)`, puis **Save**.

## Tester en local

Le service worker ne fonctionne qu'en HTTPS ou sur `localhost` :

```bash
python -m http.server 8000
```

puis ouvrir `http://localhost:8000/`.

## Langues

L'interface et l'aide existent en français, anglais, allemand, espagnol et italien. La langue du
téléphone est choisie automatiquement (anglais pour toute autre langue) ; elle peut être imposée
dans la page d'aide.

Les textes sont dans `i18n/*.json` ; le français de référence est écrit dans `i18n/src_fr.py`.
Après une modification :

```bash
python3 i18n/src_fr.py   # régénère i18n/fr.json
python3 i18n/build.py    # injecte les cinq dictionnaires dans index.html
```

Toutes les langues doivent avoir les mêmes clés : `build.py` refuse sinon.
