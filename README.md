# HYPNOGEN

Application web installable (Android et iPhone) qui reprend le générateur hypnagogique HYPNOGEN
(ESP32) : son binaural sur une porteuse de 200 Hz et lumière clignotante plein écran,
synchronisés sur une même phase de battement.

Tout se passe sur le téléphone. Les réglages et les calages de latence sont enregistrés dans le
navigateur du téléphone.

> **Avertissement** : lumière clignotante rythmée, contre-indiquée en cas d'épilepsie ou de
> photosensibilité. Toutes les séances restent sous 14 Hz. Ce n'est pas un dispositif médical.

## Utiliser l'application

L'application est publiée par GitHub Pages à l'adresse :

```
https://zigzagsgit.github.io/hypnogen-web/
```

### L'installer sur le téléphone

- **Android (Chrome)** : ouvrir l'adresse, puis menu ⋮ → « Installer l'application » (ou « Ajouter à l'écran d'accueil »).
- **iPhone (Safari)** : ouvrir l'adresse, bouton Partager → « Sur l'écran d'accueil ».

Une fois installée, elle s'ouvre en plein écran et fonctionne sans réseau (après une première ouverture avec réseau).

### Utilisation

- **Casque stéréo obligatoire** : le battement binaural n'existe pas sur un haut-parleur.
- Luminosité au maximum, luminosité automatique, True Tone / Night Shift ou Confort des yeux coupés.
- 11 séances à profil (RELAXATION, HYPNAGOGIE, ENDORMISSEMENT…), durée de 10 à 60 min.
- Mode **PROFIL** (la séance pilote la fréquence) ou **MANUEL** (fréquence fixe de 0,5 à 14 Hz).
- **Calage** : un clic retentit au début de chaque flash à 2 Hz ; régler le retard jusqu'à ce
  qu'ils coïncident. Le retard est mémorisé par sortie audio (filaire, chaque casque Bluetooth).

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
