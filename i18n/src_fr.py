# Dictionnaire de référence (français) de HYPNOGEN Web.
# Exécuter `python3 i18n/src_fr.py` pour régénérer i18n/fr.json, puis `python3 i18n/build.py`.
# Les textes entre {accolades} sont des valeurs insérées par l'application : ne pas les traduire.
import json, os

T = {
"_meta": {"code": "fr", "nom": "Français", "dec": ","},

# ---------- interface ----------
"aide.bouton": "Aide",
"aide.ouvrir": "Ouvrir l'aide",
"seance": "Séance",
"seance.choix": "Choix de la séance",
"profil.aria": "Profil de fréquence de la séance",
"profil.aria.nom": "Profil de fréquence de {nom}",
"profil.exclus": "15–25 Hz exclus",
"profil.sonseul": "son seul",
"fiche.complete": "Fiche complète de la séance",
"fiche.phases": "phases",
"fiche.onde": "onde",
"fiche.couleur": "couleur",
"fiche.conseillee": "conseillée",
"fiche.lumiere": "lumière",
"fiche.eteinte": "éteinte sous {f} Hz",
"fiche.ressenti": "Ressenti",
"fiche.conseils": "Conseils",
"fiche.choisir": "Choisir cette séance",
"onde.s": "sinus",
"onde.p": "impulsion",
"coul.chaud": "ambre chaud",
"coul.ambre": "ambre",
"coul.or": "or",
"coul.vert": "vert",
"coul.violet": "violet",
"coul.balayage": "balayage de teinte",
"coul.blanc": "blanc",
"min": "{n} min",
"carte": "{min} min · {lo}–{hi} Hz",
"pct": "{n} %",
"reglages": "Réglages",
"reglages.lien": "Tous les réglages expliqués",
"duree": "Durée",
"frequence": "Fréquence",
"mode": "Mode de fréquence",
"mode.profil": "PROFIL",
"mode.manuel": "MANUEL",
"fixe": "Fixe",
"lumiere": "Lumière",
"profondeur": "Profondeur",
"profondeur.note": "Écart entre flash et creux. Moins de profondeur = clignotement plus doux, jamais le noir complet.",
"perso": "Fréquence perso",
"perso.non": "non mesurée",
"perso.mesurer": "Mesurer",
"perso.recaler": "Recaler l'alpha",
"son.titre": "Paramétrage son",
"son.premier": "Premier réglage : choisissez le type de son, réglez le volume, puis calez votre sortie audio. Ce bloc se repliera ensuite et s'ouvrira à la demande.",
"volume": "Volume",
"musique": "Musique",
"musique.note": "Nappes, bols chantants et mélodie générés en direct et accordés sur la porteuse, dans les méditations SOUFFLE, TEMPLE, OCÉAN et AURORE. À 0 %, battement seul.",
"fiche.musique": "musique",
"fiche.souffle": "respiration",
"fiche.souffle.v": "{n} par minute",
"mus.souffle": "nappe et houle qui respirent",
"mus.temple": "bols chantants",
"mus.ocean": "océan profond",
"mus.aurore": "aube lumineuse",
"coul.turquoise": "turquoise",
"coul.bleu": "bleu",
"coul.indigo": "indigo",
"son": "Son",
"son.type": "Type de son",
"son.binaural": "BINAURAL",
"son.iso": "ISOCHRONE",
"son.court.bin": "Binaural",
"son.court.iso": "Isochrone",
"son.note.bin": "Binaural : casque stéréo obligatoire, un son par oreille, le battement naît dans le cerveau.",
"son.note.iso": "Isochrone : le volume pulse en phase avec la lumière. Fonctionne aussi sur haut-parleur.",
"son.fini": "Réglage terminé",
"porteuse": "Porteuse",
"resume": "{son} {c} Hz · volume {v} · {sortie} {ms} ms",
"etiquette": "web · v{v} · {son} {c} Hz",
"etiq.bin": "binaural",
"etiq.iso": "isochrone",
"sortie.titre": "Sortie audio et calage",
"sortie.caler": "Caler cette sortie",
"sortie.nom": "Nom d'un autre casque",
"sortie.ajouter": "Ajouter",
"sortie.retard": "Retard de la lumière : {ms} ms",
"sortie.nav": "Latence annoncée par le navigateur : {ms} ms",
"sortie.nav.inconnue": "Latence annoncée par le navigateur : connue après le premier lancement",
"sortie.filaire": "Filaire / haut-parleur",
"sortie.bt": "Casque Bluetooth",
"lancer": "Lancer la séance",
"journal": "Journal",
"journal.aveugle": "Essais à l'aveugle",
"journal.export": "Exporter (CSV)",
"journal.note": "À l'aveugle, une séance sur deux est tirée au sort en lumière arythmique (même fréquence moyenne, rythme irrégulier). Vous notez la séance, puis la condition est révélée.",
"journal.vide": "Aucune séance notée pour l'instant.",
"journal.score": "visions {v} · détente {d}",
"journal.detail": "{date} · {min} min · {son} {c} Hz · profondeur {p} %",
"journal.recalee": "recalée",
"journal.arythmique": "arythmique",
"journal.rythmique": "rythmique",
"avant.titre": "Avant de commencer",
"avant.liste": "<li>Casque stéréo obligatoire en binaural : le battement n'existe pas sur un haut-parleur.</li><li>Luminosité de l'écran au maximum, luminosité automatique coupée.</li><li>Désactivez True Tone et Night Shift (iPhone) ou le Confort des yeux (Samsung) : ils faussent les couleurs.</li><li>Sur iPhone, si le son ne sort pas, vérifiez le bouton silencieux.</li><li>Yeux fermés, téléphone à 10–15 cm du visage, ou dans un support de type masque.</li><li>Calez chaque casque Bluetooth une fois : sa latence est mémorisée.</li>",
"avert.relire": "Relire l'avertissement de sécurité",
"version": "Version {v}",
"retour": "← Retour",
"langue": "Langue",
"langue.auto": "Langue du téléphone",
"sommaire": "Sommaire",
"som.principe": "Principe",
"som.bandes": "Fréquences",
"som.lumiere": "Lumière",
"som.son": "Son",
"som.reglages": "Réglages",
"som.perso": "Fréquence perso",
"som.pendant": "Pendant la séance",
"som.journal": "Journal",
"som.seances": "Les séances",
"hud.appui": "Un appui sur l'écran éteint la lumière aussitôt",
"hud.mesure": "Yeux fermés. Touchez l'écran chaque fois que les motifs sont les plus nets.",
"hud.pause": "Lumière éteinte. Le son continue.",
"hud.lent": "Écran limité à 30 images par seconde : les flashs rapides seront irréguliers. Sur iPhone, désactivez le mode économie d'énergie.",
"hud.reprendre": "Reprendre la lumière",
"hud.arreter": "Arrêter",
"hud.mesure.nom": "MESURE",
"hud.manuel": "MANUEL",
"hud.phase": "phase {i}/{n}",
"hud.ips": "{n} i/s",
"hud.appuis.1": "(1 appui)",
"hud.appuis.n": "({n} appuis)",
"avis.titre": "Comment s'est passée la séance ?",
"avis.visions": "Visions",
"avis.detente": "Détente",
"avis.passer": "Ne pas noter",
"avis.revel.ary": "Condition tirée : lumière ARYTHMIQUE (contrôle).",
"avis.revel.ryt": "Condition tirée : lumière RYTHMIQUE (normale).",
"fermer": "Fermer",
"enregistrer": "Enregistrer",
"annuler": "Annuler",
"continuer": "Continuer",
"oui": "Oui",
"non": "Non",
"calage": "Calage",
"calage.titre": "Calage : {nom}",
"calage.texte": "Flash et clic sont réglés d'après vos appuis. S'ils ne tombent pas exactement ensemble, ajustez : augmentez si le flash arrive avant le clic, diminuez s'il arrive après.",
"calage.aria": "Retard de la lumière en millisecondes",
"calage.etape.son": "Étape 1 sur 3 · Le son",
"calage.son": "Touchez l'écran en même temps que chaque clic, en suivant le rythme. Inutile de regarder l'écran.",
"calage.etape.image": "Étape 2 sur 3 · L'image",
"calage.image": "Une bille descend vers la ligne : touchez l'écran au moment précis où elle la traverse. Il n'y a plus de son.",
"calage.etape.verif": "Étape 3 sur 3 · Vérification",
"calage.compte": "{n} appuis sur {total}",
"calage.irregulier": "Appuis trop irréguliers (± {ms} ms). Recommencez cette étape en suivant le rythme calmement.",
"calage.mesure": "Mesuré : {ms} ms",
"calage.manuel": "Régler à la main",
"calage.refaire": "Refaire la mesure",
"mesure.aucun": "Aucun appui enregistré : la fréquence personnelle n'a pas changé.",
"mesure.resultat.1": "Fréquence personnelle : {f} Hz (1 appui). Les phases alpha des séances sont recalées dessus.",
"mesure.resultat.n": "Fréquence personnelle : {f} Hz ({n} appuis). Les phases alpha des séances sont recalées dessus.",
"tab.min": "min",
"tab.freq": "Fréquence",
"tab.bande": "Bande",
"tab.palier": "{f} Hz, palier",
"tab.glisse": "{a} → {b} Hz",
"tab.fondu": "lumière en fondu",
"tab.sonseul": "son seul",
"bande.delta": "delta",
"bande.theta": "thêta",
"bande.alpha": "alpha",
"bande.beta": "bêta bas",
"avert.titre": "Avertissement de sécurité",
"avert.refus": "Avec cette réponse, n'utilisez pas HYPNOGEN sans l'accord d'un médecin.",
"avert.case": "J'ai lu cet avertissement et aucune des autres contre-indications ne me concerne.",
"q.1": "Avez-vous déjà fait une crise d'épilepsie ou des convulsions ?",
"q.2": "Un parent proche (père, mère, frère, sœur, enfant) est-il épileptique ?",
"q.3": "Une lumière clignotante vous a-t-elle déjà causé un malaise, une absence ou un mouvement involontaire ?",
"q.4": "Avez-vous des migraines avec aura ?",
"avert.texte": """<p>HYPNOGEN produit une lumière clignotante rythmée. Chez certaines personnes, ce type de stimulation peut déclencher une crise d'épilepsie, même sans antécédent connu.</p>
<ul>
<li>N'utilisez pas l'application en cas d'épilepsie, d'antécédent de convulsions ou de photosensibilité, personnelle ou familiale.</li>
<li>Évitez-la en cas de migraines, de trouble psychiatrique, de grossesse, ou avec un stimulateur cardiaque, sans avis médical.</li>
<li>Jamais en conduisant ni en utilisant une machine.</li>
<li>Arrêtez immédiatement en cas de malaise, vertige, nausée, vision troublée ou mouvement involontaire.</li>
<li>Gardez un volume modéré au casque.</li>
</ul>
<p>Par défaut, toutes les séances restent sous 14 Hz, hors de la plage 15–25 Hz la plus sensible : celle-ci ne s'ouvre qu'à part, avec une lumière bridée. Jamais de rouge saturé. Un appui sur l'écran éteint la lumière aussitôt. Ce n'est pas un dispositif médical.</p>""",

# ---------- zone bêta (15–25 Hz) ----------
"beta": "Zone bêta",
"beta.etat.ferme": "fermée",
"beta.etat.ouvert": "ouverte, 15–25 Hz",
"beta.ouvrir.court": "Ouvrir",
"beta.refermer": "Refermer",
"beta.note": "Au-dessus de 14 Hz : lumière 40 % au plus, profondeur 50 % au plus, sinus, 10 min au plus par séance.",
"beta.titre": "Ouvrir la zone bêta (15–25 Hz)",
"beta.texte": """<p>Entre 15 et 25 Hz se trouve le pic de sensibilité photo-épileptique : c'est la plage où une lumière clignotante déclenche le plus facilement une crise chez les personnes sensibles, parfois sans aucun antécédent connu.</p>
<p>Une fois la zone ouverte, dès que la fréquence dépasse 14 Hz :</p>
<ul>
<li>la lumière est limitée à 40 % et la profondeur à 50 % ;</li>
<li>l'onde devient un sinus, même dans une séance en impulsions ;</li>
<li>une séance ne passe pas plus de 10 minutes au-dessus de 14 Hz, puis reste à 14 Hz ;</li>
<li>la lumière se coupe si l'écran tourne sous 50 images par seconde.</li>
</ul>
<p>Ne l'utilisez pas fatigué, en manque de sommeil, après avoir bu de l'alcool ou avec un médicament qui abaisse le seuil épileptogène. Gardez les yeux fermés. Un appui sur l'écran éteint la lumière aussitôt.</p>""",
"bq.1": "Pendant une séance HYPNOGEN, avez-vous déjà ressenti un malaise, un mal de tête, une gêne visuelle ou une secousse musculaire ?",
"bq.2": "Avez-vous moins de 20 ans ? (La photosensibilité est la plus fréquente entre 7 et 19 ans.)",
"beta.refus": "Avec cette réponse, la zone bêta reste fermée.",
"beta.case": "J'ai compris que cette zone est la plus sensible et j'arrêterai au moindre symptôme.",
"beta.ouvrir": "Ouvrir la zone bêta",
"beta.manque": "La zone bêta s'ouvre après {n} séances d'au moins {min} minutes notées dans le journal. Vous en avez {k} pour l'instant.",
"carte.verrou": "zone bêta",
"profil.beta": "15–25 Hz : bêta, lumière bridée",
"bande.beta2": "bêta",
"hud.beta": "bêta",
"hud.beta.fin": "10 minutes au-dessus de 14 Hz atteintes : la séance reste à 14 Hz jusqu'à la fin.",
"hud.beta.lent": "Écran sous {n} images par seconde : lumière coupée au-dessus de 14 Hz, le son continue.",
"journal.beta": "bêta {m} min",
"som.beta": "Zone bêta",
"aide.beta": """<h2>La zone bêta (15–25 Hz)</h2>
<p>Par défaut, HYPNOGEN ne dépasse jamais 14 Hz. La zone 15–25 Hz, celle du bêta, est aussi le pic de sensibilité photo-épileptique : elle reste fermée tant que vous ne l'ouvrez pas vous-même, dans Réglages → Zone bêta.</p>
<h3>Conditions d'ouverture</h3>
<ul>
<li>avoir accepté l'avertissement de sécurité général ;</li>
<li>avoir noté dans le journal au moins 3 séances d'au moins 10 minutes ;</li>
<li>répondre non à deux questions de plus : malaise pendant une séance, âge de moins de 20 ans.</li>
</ul>
<h3>Ce qui change au-dessus de 14 Hz</h3>
<ul>
<li><b>Lumière 40 % au plus, profondeur 50 % au plus</b> : le contraste du clignotement compte autant que sa fréquence.</li>
<li><b>Sinus imposé</b> : les fronts raides d'une impulsion sont plus provocants.</li>
<li><b>10 minutes au plus par séance</b> au-dessus de 14 Hz ; ensuite la séance reste à 14 Hz jusqu'à la fin.</li>
<li><b>Écran à 50 images par seconde au moins</b> : en dessous, un clignotement à 20 Hz se décompose en battements irréguliers plus lents. La lumière se coupe et le son continue.</li>
<li>Ces limites s'installent progressivement entre 14 et 15 Hz : aucune marche de luminosité.</li>
</ul>
<h3>Ce qu'elle permet</h3>
<p>La séance CONCENTRATION (12 → 18,5 → 15 → 12 Hz, 20 minutes au plus), le mode MANUEL jusqu'à 25 Hz, et la séance GAMMA à 40 Hz sur ruban LED (voir « Ruban et gamma »). Au-dessus d'une vingtaine de hertz, le battement binaural devient difficile à percevoir : préférez le son ISOCHRONE. « Refermer » ramène l'application sous 14 Hz.</p>""",

# ---------- ruban LED et gamma ----------
"ruban": "Ruban LED",
"ruban.non": "non connecté",
"ruban.indispo": "Bluetooth web indisponible : Chrome sur Android requis",
"ruban.connecter": "Connecter",
"ruban.deconnecter": "Déconnecter",
"ruban.connexion": "connexion…",
"ruban.sync": "connecté · synchronisation…",
"ruban.pret": "connecté · synchro ± {ms} ms",
"ruban.note": "Ruban connecté : toute la lumière passe par le ruban, l'écran reste noir pendant la séance.",
"ruban.erreur": "Connexion au ruban impossible : {e}",
"ruban.attente": "Le ruban termine sa synchronisation. Réessayez dans une seconde.",
"sortie.retard.ruban": "ruban : {ms} ms",
"calage.titre.ruban": "Calage du ruban : {nom}",
"calage.etape.ruban": "Étape 2 sur 3 · Le ruban",
"calage.ruban": "Le ruban flashe à intervalles réguliers : touchez l'écran en même temps que chaque flash. Il n'y a plus de son.",
"hud.ruban": "ruban",
"hud.ruban.perdu": "Liaison avec le ruban perdue : lumière coupée, reconnexion en cours. Le son continue.",
"hud.gamma": "gamma",
"bande.gamma": "gamma",
"journal.ruban": "ruban",
"gamma.titre": "Avant la séance gamma (40 Hz)",
"gamma.texte": """<ul>
<li><b>Yeux ouverts</b> : au-delà de 25 Hz, la lumière se fond derrière les paupières.</li>
<li>Ruban tourné vers un mur ou le plafond, jamais face aux yeux. Regard posé, sans fixer le ruban.</li>
<li>Son isochrone imposé, 20 minutes au plus, lumière limitée à 50 %.</li>
<li>Arrêtez au moindre mal de tête, vertige ou gêne visuelle. Un appui sur l'écran coupe le ruban aussitôt.</li>
</ul>""",
"gamma.lancer": "Lancer",
"gamma.ruban": "La séance GAMMA passe uniquement par le ruban LED : un écran de téléphone ne peut pas produire 40 Hz proprement. Connectez le ruban dans Réglages, puis relancez.",
"som.ruban": "Ruban et gamma",
"aide.ruban": """<h2>Ruban LED et gamma</h2>
<p>Le téléphone peut piloter le ruban LED de la carte HYPNOGEN, flashée avec le croquis <b>HypnoGenRuban</b>. Le téléphone garde l'interface et le son ; la carte ne fait que la lumière. La liaison est un Bluetooth basse consommation direct : <b>tout fonctionne hors ligne</b>, même en mode avion avec le Bluetooth réactivé.</p>
<h3>Connecter</h3>
<ul>
<li>Réglages → Ruban LED → Connecter, puis choisir <b>HYPNOGEN-RUBAN</b> dans la liste. Chrome demande ce choix à chaque lancement de l'application.</li>
<li>La première fois, autorisez Chrome à accéder aux « Appareils à proximité ».</li>
<li>Une fois connecté, toute la lumière passe par le ruban et l'écran reste noir. Le témoin de la carte clignote en attente et reste allumé une fois connecté.</li>
<li>Bluetooth web : Chrome sur Android. Safari sur iPhone ne le propose pas.</li>
</ul>
<h3>Synchronisation et calage</h3>
<p>Le téléphone n'envoie pas un ordre par flash : il envoie la phase du battement 0,8 s à l'avance, et la carte calcule la lumière elle-même, sur une horloge commune recalée chaque seconde (précision affichée dans Réglages). Le retard du ruban se cale comme celui de l'écran : ruban connecté, « Caler cette sortie » remplace l'étape des billes par des flashs du ruban. Il est mémorisé à part pour chaque sortie audio.</p>
<h3>La séance GAMMA</h3>
<p>Palier de 40 Hz, en impulsions, blanc chaud, 15 minutes conseillées, 20 au plus. Elle demande la zone bêta ouverte et le ruban connecté. Le son est forcément isochrone (le battement binaural ne porte pas 40 Hz). Elle se pratique <b>les yeux ouverts</b>, le ruban tourné vers un mur.</p>
<h3>Sécurités du ruban</h3>
<ul>
<li>La carte applique ses propres limites, quoi que demande le téléphone : puissance plafonnée, bridage de la zone bêta, <b>lumière coupée entre 25 et 35 Hz</b> et au-delà de 45 Hz, gamma à 50 % au plus.</li>
<li>Elle déduit la fréquence de la phase qu'elle reçoit : ces limites ne dépendent pas d'une valeur annoncée.</li>
<li>Liaison perdue ou nœuds manquants : extinction en 0,3 s. Le téléphone retente la connexion seul.</li>
<li>Un appui sur l'écran coupe le ruban en 30 ms, comme l'écran.</li>
</ul>""",

# ---------- page d'aide ----------
"aide.principe": """<h2>Le principe</h2>
<p>HYPNOGEN fait clignoter l'écran à une fréquence donnée pendant que le casque fait entendre un battement à la même fréquence. Lumière et son lisent la même horloge : chaque flash tombe sur le même instant du battement, du début à la fin de la séance.</p>
<p>On pratique les yeux fermés, téléphone à 10–15 cm du visage. À travers les paupières, la lumière rythmée fait souvent apparaître des motifs colorés, des formes géométriques, parfois des images plus construites : ce sont des phosphènes, produits par le système visuel lui-même.</p>
<p>Une séance est une suite de phases. Chaque phase fait glisser la fréquence d'une valeur de départ vers une valeur d'arrivée, en douceur (pente nulle au début et à la fin, aucun à-coup entre deux phases), ou la maintient sur un palier. Les phases ont un poids relatif et non une durée fixe : si vous passez une séance de 30 à 20 minutes, toute la progression se resserre sans perdre aucune étape.</p>""",

"aide.bandes": """<h2>Les bandes de fréquence</h2>
<p>Les séances se repèrent par les bandes de l'électroencéphalogramme. Ce sont des repères commodes : la stimulation ne « met » pas le cerveau dans un état, elle propose un rythme que chacun suit plus ou moins.</p>
<div class="defile"><table class="tableau">
<thead><tr><th>Bande</th><th>Plage</th><th>Associée à</th></tr></thead>
<tbody>
<tr><td>Delta</td><td>0,25 – 4 Hz</td><td>sommeil profond</td></tr>
<tr><td>Thêta</td><td>4 – 8 Hz</td><td>somnolence, seuil du sommeil, images hypnagogiques</td></tr>
<tr><td>Alpha</td><td>8 – 13 Hz</td><td>éveil détendu, yeux fermés</td></tr>
<tr><td>Bêta bas</td><td>13 – 14 Hz</td><td>éveil attentif (plafond par défaut)</td></tr>
<tr class="exclu"><td>Bêta</td><td>15 – 25 Hz</td><td>éveil actif, concentration. Pic de sensibilité photo-épileptique : fermée par défaut, lumière bridée une fois ouverte</td></tr>
<tr><td>Gamma</td><td>35 – 45 Hz</td><td>ruban LED seulement, yeux ouverts (séance GAMMA à 40 Hz). Entre 25 et 35 Hz, la lumière reste coupée</td></tr>
</tbody></table></div>
<p>La valeur 7,83 Hz, qui revient dans plusieurs séances, est la fréquence de la résonance de Schumann. Elle sert ici de point d'appui à la frontière alpha–thêta.</p>""",

"aide.lumiere": """<h2>Lumière : couleurs et formes d'onde</h2>
<dl class="duo">
<dt>Sinus</dt><dd>La lumière monte et descend en douceur. Enveloppant, adapté aux séances de détente et de sommeil.</dd>
<dt>Impulsion</dt><dd>Flash bref et net, presque carré. Plus riche en motifs visuels, utilisé pour l'imagerie et les séances toniques.</dd>
<dt>Ambre chaud, ambre, or</dt><dd>Teintes chaudes, les plus reposantes. Le rouge saturé n'est jamais affiché : c'est la couleur la plus provocante pour la photosensibilité.</dd>
<dt>Vert, violet</dt><dd>Teintes froides, propres à MÉMOIRE (vert) et à MÉDITATION et TRANSE (violet).</dd>
<dt>Balayage</dt><dd>La teinte fait le tour du cercle des couleurs en 50 secondes, toujours sans rouge saturé.</dd>
</dl>""",

"aide.son": """<h2>Son</h2>
<dl class="duo">
<dt>Binaural</dt><dd>Deux sons purs légèrement différents, un par oreille (par exemple 197 et 203 Hz pour 6 Hz). Le battement n'existe pas dans l'air : il naît dans le cerveau. Casque stéréo obligatoire.</dd>
<dt>Isochrone</dt><dd>Un seul son, dans les deux oreilles, dont le volume pulse au rythme de la séance. La crête du son coïncide avec le flash. Fonctionne aussi sur haut-parleur.</dd>
<dt>Porteuse</dt><dd>Hauteur du son de base : 200 Hz (grave, comme le boîtier HYPNOGEN), 300 ou 400 Hz. Le battement binaural est en général le mieux perçu vers 400 Hz ; 200 Hz est plus doux pour dormir.</dd>
</dl>
<p>Ces réglages sont regroupés dans le bloc « Paramétrage son », ouvert au premier usage puis replié : son résumé (type de son, porteuse, volume, sortie) reste visible. Le détail de chaque réglage est dans la section suivante.</p>""",

"aide.reglages": """<h2>Les réglages en détail</h2>
<p>Tous les réglages sont enregistrés dans le téléphone et retrouvés à l'ouverture suivante. Ils ne quittent jamais l'appareil.</p>

<h3>Séance</h3>
<p>Le bandeau du haut fait défiler les onze séances. En choisir une affiche son profil (courbe de la fréquence dans le temps) et applique sa durée conseillée. La bande rouge du profil marque la zone 15–25 Hz, que l'application n'atteint pas tant que la zone bêta est fermée. Le lien « Fiche complète » ouvre la description détaillée de la séance.</p>

<h3>Durée</h3>
<p>10, 15, 20, 25, 30, 45 ou 60 minutes. Toutes les phases s'allongent ou se resserrent dans les mêmes proportions : une séance raccourcie garde sa progression, elle la parcourt simplement plus vite. Les phases très courtes laissent moins de temps pour s'installer ; en dessous de la moitié de la durée conseillée, l'effet est souvent plus faible.</p>

<h3>Fréquence : PROFIL ou MANUEL</h3>
<p><b>PROFIL</b> (par défaut) : la séance pilote la fréquence, phase après phase.</p>
<p><b>MANUEL</b> : vous imposez une fréquence fixe avec le curseur « Fixe », de 0,5 à 14 Hz (25 Hz zone bêta ouverte). Pendant la séance, les boutons −0,5 Hz et +0,5 Hz la modifient sans s'arrêter. La séance ne fournit plus que sa couleur et sa forme d'onde. En manuel, la fréquence personnelle n'est pas appliquée et la lumière des séances de sommeil ne s'éteint pas d'elle-même.</p>
<p>Usage typique : après une séance FIBONACCI, rejouer en manuel le palier qui a donné les images les plus nettes.</p>

<h3>Lumière</h3>
<p>Intensité maximale des flashs, de 10 à 100 % (70 % par défaut). Elle s'applique en plus de la luminosité de l'écran, qui doit rester au maximum. Commencez à 70 % ; montez si les motifs restent pâles, descendez si la lumière éblouit à travers les paupières.</p>

<h3>Profondeur</h3>
<p>Écart entre la crête du flash et le creux entre deux flashs, de 30 à 100 % (80 % par défaut). À 100 %, la lumière retombe au noir complet. À 80 %, le creux garde 20 % de la luminosité de la crête. À 50 %, la lumière ne descend qu'à mi-hauteur : le clignotement devient une pulsation douce.</p>
<p>Une forte profondeur donne des motifs plus contrastés ; une profondeur réduite est plus confortable et plus prudente. Si vous trouvez le clignotement fatigant, baissez d'abord la profondeur, avant la lumière.</p>

<h3>Fréquence perso</h3>
<p>Affiche votre fréquence personnelle si elle a été mesurée. « Mesurer » lance la mesure (2 min 30, voir la section suivante). « Recaler l'alpha » active ou désactive le recalage des séances sur cette fréquence ; le bouton n'apparaît qu'après une mesure.</p>

<h3>Volume</h3>
<p>De 0 à 100 % (55 % par défaut). La courbe est progressive : les petites valeurs restent fines à régler, ce qui compte pour dormir. Le son monte en 20 secondes au début de la séance et s'éteint en 15 secondes à la fin : ne réglez pas le volume du téléphone au tout début, attendez qu'il soit monté. Gardez un niveau modéré, surtout pour les séances longues.</p>

<h3>Musique</h3>
<p>De 0 à 100 % (70 % par défaut). Les quatre méditations SOUFFLE, TEMPLE, OCÉAN et AURORE ont une musique composée en direct par l'application : accords tenus, bols chantants, mélodie clairsemée, houle, dans une réverbération. Elle ne se répète jamais à l'identique. Tout est accordé sur la porteuse, qui devient une note de chaque accord. En binaural, chaque note de la nappe porte le même battement que la porteuse, en phase avec la lumière ; les bols et les notes de la mélodie tombent sur un flash. Plus la séance descend, plus le timbre s'assombrit et plus la musique s'espace. Le curseur règle la musique par rapport au battement ; le volume général agit sur les deux. Les autres séances restent sans musique.</p>

<h3>Son : BINAURAL ou ISOCHRONE</h3>
<p><b>Binaural</b> : chaque oreille reçoit un son pur légèrement différent ; l'écart entre les deux est la fréquence de la séance. C'est le mode d'origine du HYPNOGEN. Il exige un casque ou des écouteurs stéréo ; le sens gauche/droite n'a pas d'importance.</p>
<p><b>Isochrone</b> : un seul son, dont le volume monte et descend au rythme de la séance, crête du son sur le flash. Le battement est plus marqué et fonctionne sur haut-parleur, mais il est aussi plus présent, ce qui peut gêner pour dormir.</p>

<h3>Porteuse</h3>
<p>Hauteur du son de base : 200, 300 ou 400 Hz (200 Hz par défaut). La fréquence de la séance ne change pas, seule la hauteur du son change. 200 Hz est grave et discret ; 400 Hz rend le battement binaural plus net pour beaucoup de personnes. Essayez les trois sur une même séance et gardez celui qui vous convient.</p>

<h3>Sortie audio et calage</h3>
<p>Un casque Bluetooth retarde le son de 100 à 300 ms selon le modèle ; sans correction, le flash arriverait avant le son. Chaque sortie mémorise son propre retard : « Filaire / haut-parleur » (0 ms par défaut) et « Casque Bluetooth » (180 ms par défaut). « Ajouter » crée une sortie pour un autre casque, avec 180 ms au départ.</p>
<p>Pour caler une sortie :</p>
<ol>
<li>Choisissez la sortie dans la liste et branchez ou connectez le casque correspondant.</li>
<li>Touchez « Caler cette sortie ». Un clic retentit un peu plus d'une fois par seconde : touchez l'écran en même temps que chaque clic, une douzaine de fois. Les deux premiers appuis ne comptent pas.</li>
<li>L'écran montre ensuite, sans son, des billes qui descendent vers une ligne : touchez l'écran au moment où chaque bille traverse la ligne.</li>
<li>L'application en déduit le retard du son sur l'image, puis fait clignoter flash et clic ensemble. S'ils ne tombent pas exactement ensemble, ajustez avec le curseur ou les boutons −5 / +5 ms : augmentez si le flash arrive avant le clic, diminuez s'il arrive après.</li>
<li>Touchez « Enregistrer ».</li>
</ol>
<p>Taper un rythme est plus facile que de juger à l'œil si un flash et un clic coïncident, et votre temps de réaction, le même dans les deux étapes, s'annule en grande partie. « Régler à la main » saute la mesure et passe directement au curseur. Refaites le calage si vous changez de casque ou si la synchronisation vous semble dériver. La « latence annoncée par le navigateur » est donnée à titre indicatif : elle est souvent fausse en Bluetooth.</p>

<h3>Paramétrage son replié</h3>
<p>Une fois le premier réglage fait, le bloc son se replie et affiche son résumé. Touchez-le pour l'ouvrir et changer un réglage.</p>""",

"aide.perso": """<h2>Mesurer votre fréquence personnelle</h2>
<p>Les séances sont écrites autour de 10 Hz, la valeur moyenne du rythme alpha. Mais chacun a son propre pic alpha, quelque part entre 8 et 12 Hz environ. La mesure cherche la fréquence à laquelle la lumière produit chez vous les motifs les plus nets, puis décale les phases alpha des séances vers cette valeur.</p>

<h3>Préparer la mesure</h3>
<ul>
<li>Choisissez un moment calme, sans fatigue particulière : la fréquence varie un peu avec la vigilance.</li>
<li>Réglez d'abord la lumière et la profondeur comme pour une séance normale.</li>
<li>Asseyez-vous, téléphone à 10–15 cm du visage, casque en place, yeux fermés.</li>
</ul>

<h3>Déroulement</h3>
<ol>
<li>Touchez « Mesurer » à côté de « Fréquence perso ».</li>
<li>Pendant 2 min 30, la lumière ambre clignote en impulsions et la fréquence monte régulièrement de 7 à 13 Hz (le son suit). Les trois premières secondes servent à démarrer et ne comptent pas.</li>
<li>Touchez l'écran chaque fois que les motifs sont les plus nets, les plus colorés ou les plus vivants. Un clic confirme chaque appui. Vous pouvez toucher plusieurs fois, par exemple au début et à la fin d'une zone où les images sont fortes : c'est même recommandé.</li>
<li>Laissez la mesure aller à son terme. Vous pouvez aussi l'arrêter plus tôt : les appuis déjà faits sont utilisés.</li>
</ol>
<p>Pendant la mesure, un appui ne coupe pas la lumière : il marque l'instant. Le bouton « Arrêter » reste affiché.</p>

<h3>Comment le résultat est calculé</h3>
<ul>
<li>Pour chaque appui, l'application retient la fréquence affichée 0,6 seconde plus tôt, pour tenir compte de votre temps de réaction.</li>
<li>Le résultat est la médiane de ces fréquences : un appui isolé trop tôt ou trop tard ne le déplace pas.</li>
<li>Il est borné entre 8 et 12 Hz, puis enregistré, et le recalage est activé automatiquement.</li>
<li>Sans aucun appui, rien ne change.</li>
</ul>

<h3>Ce que fait le recalage</h3>
<p>Le recalage déplace la zone alpha des séances vers votre fréquence, sans toucher au reste :</p>
<ul>
<li>à 10 Hz, la séance utilise exactement votre fréquence ;</li>
<li>la correction diminue en s'éloignant de 10 Hz et s'annule à 7 Hz et à 13 Hz ;</li>
<li>en dessous de 7 Hz (thêta, delta) et au-dessus de 13 Hz, rien ne change ;</li>
<li>le plafond de 14 Hz est toujours respecté.</li>
</ul>
<p>Exemple avec une fréquence personnelle de 9 Hz : 10 Hz devient 9 Hz, 8,5 Hz devient 8 Hz, 12 Hz devient 11,67 Hz ; 7 et 13 Hz restent tels quels. Avec 11 Hz : 10 Hz devient 11 Hz et 12 Hz devient 12,33 Hz.</p>
<p>Le profil affiché sur l'écran principal tient compte du recalage. Les profils de cette aide, eux, montrent les séances d'origine. Le recalage ne s'applique pas en mode MANUEL.</p>

<h3>Conseils</h3>
<ul>
<li>Refaites la mesure deux ou trois fois, à des jours différents : si les résultats sont proches, la valeur est fiable.</li>
<li>Si les résultats varient beaucoup, ou si vous n'avez rien remarqué de net, désactivez « Recaler l'alpha » : les séances d'origine fonctionnent très bien sans.</li>
<li>Comparez avec le journal : notez quelques séances recalées et non recalées, puis regardez l'écart.</li>
</ul>""",

"aide.pendant": """<h2>Pendant la séance</h2>
<ul>
<li>L'écran passe en plein écran et reste allumé jusqu'à la fin.</li>
<li>La lumière monte en 8 secondes et s'éteint en 10 secondes à la fin ; le son monte en 20 secondes et s'éteint en 15.</li>
<li>Le bandeau du bas affiche la séance, la phase en cours, la fréquence, le temps restant et la cadence de l'écran en images par seconde. Il disparaît au bout de 4 secondes.</li>
<li><b>Un appui n'importe où éteint la lumière aussitôt</b>, le son continue. « Reprendre la lumière » la rallume ; « Arrêter » met fin à la séance. La touche Échap arrête aussi la séance sur ordinateur.</li>
<li>En MANUEL, les boutons −0,5 Hz et +0,5 Hz changent la fréquence en direct.</li>
<li>Si l'écran est limité à 30 images par seconde (mode économie d'énergie), un avertissement s'affiche : les flashs rapides seraient irréguliers.</li>
<li>Après toute séance de plus de 2 minutes, une fiche vous propose de la noter.</li>
</ul>""",

"aide.journal": """<h2>Journal et essais à l'aveugle</h2>
<p>Après toute séance de plus de 2 minutes, vous notez les visions et la détente sur 10. Les notes restent dans le téléphone et s'exportent en CSV, avec la séance, la durée, le type de son, la porteuse, la profondeur et le recalage.</p>
<p>En mode « Essais à l'aveugle », une séance sur deux est tirée au sort en lumière arythmique : même fréquence moyenne, mais intervalles irréguliers. Le son reste rythmique. Vous notez d'abord, la condition n'est révélée qu'ensuite. Au bout d'une vingtaine de séances, la comparaison des notes montre ce que le rythme apporte vraiment, pour vous.</p>""",

"aide.seances": """<h2>Les séances</h2>
<p>Quinze séances sous 14 Hz, dont quatre méditations en musique (SOUFFLE, TEMPLE, OCÉAN, AURORE), plus CONCENTRATION et GAMMA, réservées à la zone bêta. Les tableaux donnent le déroulé pour la durée conseillée.</p>""",

"aide.securite": """<h2>Sécurité</h2>
<p>Lumière clignotante rythmée : contre-indiquée en cas d'épilepsie, d'antécédent de convulsions ou de photosensibilité, personnelle ou familiale. Arrêtez au moindre malaise. HYPNOGEN n'est pas un dispositif médical et ne prétend soigner aucun trouble.</p>""",

# ---------- plates-formes (v1.10) : variantes clé@os puis clé@pc / clé@mobile, section « Votre appareil » ----------
"version.installee": "application installée",
"som.appareil": "Votre appareil",
"hud.touches": "",
"hud.touches@pc": "Espace : couper la lumière · R : la reprendre · ← → : ±0,5 Hz en manuel · Échap : arrêter",
"hud.appui@pc": "Un clic ou la barre d'espace éteint la lumière aussitôt",
"hud.mesure@pc": "Yeux fermés. Appuyez sur Espace (ou cliquez) chaque fois que les motifs sont les plus nets.",
"hud.lent@android": "Écran limité à 30 images par seconde : les flashs rapides seront irréguliers. Désactivez le mode économie d'énergie.",
"hud.lent@pc": "Écran limité à 30 images par seconde : les flashs rapides seront irréguliers. Branchez l'ordinateur sur secteur, quittez le mode économie d'énergie et fermez les onglets lourds.",
"calage.son@pc": "Appuyez sur Espace (ou cliquez) en même temps que chaque clic, en suivant le rythme. Inutile de regarder l'écran.",
"calage.image@pc": "Une bille descend vers la ligne : appuyez sur Espace (ou cliquez) au moment précis où elle la traverse. Il n'y a plus de son.",
"calage.ruban@pc": "Le ruban flashe à intervalles réguliers : appuyez sur Espace (ou cliquez) en même temps que chaque flash. Il n'y a plus de son.",
"ruban.indispo@ios": "Bluetooth web absent sur iPhone et iPad : ruban indisponible",
"ruban.indispo@android": "Bluetooth web indisponible : ouvrez l'application dans Chrome",
"ruban.indispo@pc": "Bluetooth web indisponible : ouvrez l'application dans Chrome ou Edge",
"ruban.indispo@linux": "Bluetooth web indisponible : Chrome requis, avec chrome://flags/#enable-experimental-web-platform-features activé",
"gamma.ruban@pc": "La séance GAMMA passe uniquement par le ruban LED : un écran ne peut pas produire 40 Hz proprement. Connectez le ruban dans Réglages, puis relancez.",
"avant.liste@pc": "<li>Casque stéréo obligatoire en binaural : le battement n'existe pas sur des haut-parleurs.</li><li>Luminosité de l'écran au maximum, pièce peu éclairée.</li><li>Yeux fermés, face à l'écran, à 40–60 cm. La fenêtre passe en plein écran pendant la séance.</li><li>Calez chaque sortie audio une fois (casque filaire, casque Bluetooth) : sa latence est mémorisée.</li>",
"avant.os": "",
"avant.os@pc": "<li>Coupez le filtre de lumière bleue et la luminosité automatique de l'écran, et suspendez les notifications.</li>",
"avant.os@win": "<li>Windows : coupez l'éclairage nocturne et la luminosité automatique (Paramètres → Système → Écran), et activez « Ne pas déranger ».</li>",
"avant.os@mac": "<li>Mac : coupez Night Shift, True Tone et la luminosité automatique (Réglages Système → Moniteurs), et activez la Concentration « Ne pas déranger ».</li>",
"avant.os@linux": "<li>Linux : coupez la lumière nocturne et la gradation automatique de l'écran, et suspendez les notifications.</li>",
"avant.veille": "<li>Ce navigateur ne sait pas empêcher la mise en veille de l'écran : réglez-la sur une durée plus longue que la séance.</li>",
"aide.appareil.titre": "Votre appareil : {os}",
"aide.appareil.detecte": "Reconnu automatiquement : {os}, navigateur {nav}. L'application adapte ses commandes, ses conseils et cette page à cet appareil.",
"aide.appareil.cmd": "",
"aide.appareil.cmd@pc": """<h3>Clavier et souris</h3>
<ul>
<li><b>Espace</b> ou un clic dans la lumière : la lumière s'éteint aussitôt, le son continue. <b>R</b> la rallume.</li>
<li><b>Échap</b> arrête la séance. Quitter le plein écran l'arrête aussi.</li>
<li><b>←</b> et <b>→</b> : −0,5 et +0,5 Hz en MANUEL.</li>
<li>Calage et mesure de la fréquence personnelle : <b>Espace</b> marque l'instant, plus régulièrement qu'un clic. Partout où l'aide dit « touchez l'écran », appuyez sur Espace ou cliquez.</li>
<li>Bouger la souris affiche le bandeau ; le pointeur disparaît avec lui.</li>
</ul>
<h3>Placement</h3>
<ul>
<li>Yeux fermés, face à l'écran, à 40–60 cm. Plus l'écran est grand, plus la lumière couvre le champ visuel : commencez avec la lumière à 70 % ou moins.</li>
</ul>""",
"aide.appareil.os": """<h3>Installer</h3>
<ul><li>Chrome ou Edge : icône d'installation dans la barre d'adresse. L'application fonctionne ensuite hors ligne.</li></ul>
<h3>Réglages</h3>
<ul><li>Luminosité au maximum, luminosité automatique et filtre de lumière bleue coupés, notifications suspendues.</li></ul>
<h3>Ruban LED</h3>
<ul><li>Il faut un navigateur qui propose le Bluetooth web : Chrome ou Edge.</li></ul>""",
"aide.appareil.os@ios": """<h3>Installer</h3>
<ul><li>Dans Safari : bouton Partager → « Sur l'écran d'accueil ». L'application s'ouvre ensuite sans barre d'adresse et fonctionne hors ligne.</li></ul>
<h3>Réglages</h3>
<ul>
<li>Coupez True Tone, Night Shift et la luminosité automatique : ils faussent les couleurs et la luminosité.</li>
<li>Si le son ne sort pas, vérifiez le mode silencieux.</li>
<li>Le mode économie d'énergie limite l'écran à 30 images par seconde : coupez-le.</li>
<li>Safari ne passe pas en plein écran sur iPhone : installez l'application pour masquer la barre d'adresse.</li>
</ul>
<h3>Ruban LED</h3>
<ul><li>Indisponible : aucun navigateur d'iPhone ou d'iPad ne propose le Bluetooth web.</li></ul>""",
"aide.appareil.os@android": """<h3>Installer</h3>
<ul><li>Dans Chrome : menu ⋮ → « Installer l'application » (ou « Ajouter à l'écran d'accueil »).</li></ul>
<h3>Réglages</h3>
<ul>
<li>Coupez la luminosité adaptative et le Confort des yeux (Samsung) ou le filtre de lumière bleue : ils faussent couleurs et luminosité.</li>
<li>Le mode économie d'énergie peut limiter l'écran à 30 images par seconde : coupez-le pendant la séance.</li>
<li>Activez « Ne pas déranger » : aucune notification ne doit allumer l'écran.</li>
</ul>
<h3>Ruban LED</h3>
<ul><li>Avec Chrome. La première fois, autorisez Chrome à accéder aux « Appareils à proximité ».</li></ul>""",
"aide.appareil.os@win": """<h3>Installer</h3>
<ul><li>Chrome ou Edge : icône d'installation à droite de la barre d'adresse (ou menu → « Installer HYPNOGEN »). L'application s'ouvre dans sa propre fenêtre et fonctionne hors ligne.</li></ul>
<h3>Réglages de Windows</h3>
<ul>
<li>Paramètres → Système → Écran : coupez l'éclairage nocturne et la luminosité automatique ou adaptative au contenu.</li>
<li>Activez « Ne pas déranger » : une notification par-dessus le plein écran gâcherait la séance.</li>
<li>Portable : branchez-le sur secteur, l'économiseur de batterie peut ralentir l'affichage.</li>
<li>Casque Bluetooth : comptez souvent 150 à 250 ms de retard, à caler une fois. Si une application utilise son micro, Windows le passe en mode « mains libres », en mono : le battement binaural disparaît. Choisissez la sortie « Casque » ou « Stéréo », pas « Mains libres ».</li>
</ul>
<h3>Ruban LED</h3>
<ul><li>Chrome ou Edge, Bluetooth de l'ordinateur activé. Firefox ne propose pas le Bluetooth web.</li></ul>""",
"aide.appareil.os@mac": """<h3>Installer</h3>
<ul><li>Safari : Fichier → « Ajouter au Dock ». Chrome ou Edge : icône d'installation dans la barre d'adresse. L'application s'ouvre dans sa propre fenêtre et fonctionne hors ligne.</li></ul>
<h3>Réglages du Mac</h3>
<ul>
<li>Réglages Système → Moniteurs : coupez True Tone, Night Shift et « Ajuster automatiquement la luminosité ».</li>
<li>Activez la Concentration « Ne pas déranger ».</li>
<li>Portable : branchez-le sur secteur, le mode économie d'énergie peut ralentir l'affichage.</li>
</ul>
<h3>Ruban LED</h3>
<ul><li>Chrome ou Edge uniquement : Safari et Firefox ne proposent pas le Bluetooth web. La première fois, autorisez le navigateur dans Réglages Système → Confidentialité et sécurité → Bluetooth.</li></ul>""",
"aide.appareil.os@linux": """<h3>Installer</h3>
<ul><li>Chrome, Chromium ou Edge : icône d'installation dans la barre d'adresse. Firefox n'installe pas les applications web, mais l'application y fonctionne dans un onglet.</li></ul>
<h3>Réglages</h3>
<ul>
<li>Coupez la lumière nocturne et la gradation automatique de l'écran, suspendez les notifications.</li>
<li>Si l'écran s'éteint pendant la séance, allongez le délai de mise en veille.</li>
</ul>
<h3>Ruban LED</h3>
<ul><li>Chrome, après avoir activé chrome://flags/#enable-experimental-web-platform-features. Le service Bluetooth (BlueZ) doit tourner.</li></ul>""",
}

# ---------- séances : nom affiché, accroche, déroulé, ressenti, conseils ----------
# La clé est l'identifiant interne (nom français du firmware) : ne pas la traduire.
S = {
 "RELAXATION": {"nom": "RELAXATION",
  "but": "Détente progressive, de l'éveil calme vers un état posé.",
  "desc": "Descente régulière de l'alpha haut (12 Hz) jusqu'au seuil thêta–delta (4 Hz), sans détour : chaque phase reprend exactement là où la précédente s'arrête. La dernière phase tient 4 Hz pour laisser le temps de s'installer dans le calme obtenu.",
  "ressenti": "Relâchement progressif, respiration qui ralentit. À mesure que la fréquence baisse, les flashs paraissent plus amples et plus lents, les motifs plus larges.",
  "conseil": "La séance la plus simple pour découvrir HYPNOGEN. En fin de journée, pour couper après le travail, assis ou allongé."},
 "IMAGINATION": {"nom": "IMAGINATION",
  "but": "Rêverie éveillée et images mentales, avec des flashs nets.",
  "desc": "Impulsions nettes et teinte qui tourne lentement (un tour du cercle des couleurs en 50 s). La fréquence descend de l'alpha vers 6 Hz, en plein thêta, puis s'y stabilise sur la plus longue phase de la séance.",
  "ressenti": "C'est la séance la plus riche en images : motifs géométriques, tunnels, couleurs mouvantes, parfois des scènes plus construites dans le dernier quart.",
  "conseil": "Ne cherchez pas à fixer les images : laissez-les venir et passer. Lumière à 70 % ou plus, profondeur élevée. Notez les visions dans le journal pour comparer d'une fois sur l'autre."},
 "HYPNAGOGIE": {"nom": "HYPNAGOGIE",
  "but": "Long palier à 7,83 Hz pour rester au seuil du sommeil.",
  "desc": "Après une courte descente, un long palier à 7,83 Hz occupe près de la moitié de la séance, à la frontière alpha–thêta. La fin glisse vers 6,3 Hz. Le but est de rester suspendu au seuil de l'endormissement, sans y basculer.",
  "ressenti": "Sensation de flotter, pensées qui se défont, images hypnagogiques brèves qui surgissent et s'effacent. Le corps peut sembler lourd ou au contraire léger.",
  "conseil": "Plutôt assis ou semi-allongé : complètement allongé, on s'endort facilement. Si vous vous endormez à chaque fois, raccourcissez à 20 min ou passez en MANUEL vers 8 Hz."},
 "ENDORMISSEMENT": {"nom": "ENDORMISSEMENT",
  "but": "Descente continue jusqu'au delta, finie dans le noir, pour s'endormir.",
  "desc": "Descente continue de 10 Hz jusqu'à 0,25 Hz. La lumière s'éteint en fondu autour de 2 Hz : la fin de la séance se passe dans le noir, avec le son seul qui poursuit la descente en delta.",
  "ressenti": "Engourdissement progressif. Beaucoup de personnes ne voient pas la fin de la séance.",
  "conseil": "Au lit, téléphone posé sur un support, casque confortable pour dormir, volume bas. Le son s'arrête en fondu, l'écran se rendort normalement ensuite."},
 "RÊVE": {"nom": "RÊVE",
  "but": "Glissement lent vers le sommeil profond, fini dans le noir.",
  "desc": "Départ déjà bas, à 8 Hz, puis glissement plus lent et plus long que l'ENDORMISSEMENT dans le delta, jusqu'à 0,25 Hz. Comme lui, la lumière s'éteint vers 2 Hz et le son continue seul.",
  "ressenti": "Plongée douce, sans la phase alpha du début : convient quand on est déjà fatigué.",
  "conseil": "Pour une sieste, le coucher, ou après un réveil nocturne. Mêmes précautions que pour l'ENDORMISSEMENT : casque de nuit, volume bas."},
 "ANCRAGE": {"nom": "ANCRAGE",
  "but": "Courte séance de recentrage qui finit très bas.",
  "desc": "Séance courte : un palier à 7,83 Hz pour se poser, puis une descente franche jusqu'à 1,12 Hz, maintenue jusqu'à la fin.",
  "ressenti": "Coupure nette avec l'agitation du moment ; la fin, très lente, laisse un état calme et lourd.",
  "conseil": "Pause de mi-journée. La séance finit très bas : prévoyez deux ou trois minutes pour revenir avant de reprendre une activité, et jamais avant de conduire."},
 "MÉDITATION": {"nom": "MÉDITATION",
  "but": "Méditation longue, descente lente vers 1 Hz.",
  "desc": "La plus longue descente vers le delta léger : alpha, palier à 7,83 Hz, puis trois glissements successifs jusqu'à 1,05 Hz, tenu sur la dernière phase. Violet, en sinus.",
  "ressenti": "Calme profond, attention qui se pose sans effort. La lumière devient très lente et enveloppante dans le dernier tiers.",
  "conseil": "Assis, dos droit, en suivant la respiration si vous en avez l'habitude. 30 min conseillées ; 20 min suffisent pour commencer."},
 "TRANSE": {"nom": "TRANSE",
  "but": "Plongée profonde puis remontée vers le thêta.",
  "desc": "Descente en impulsions jusqu'à un long palier à 2 Hz, puis remontée vers 4 Hz pour finir en thêta. Le retour vers le haut ramène des images après la phase la plus profonde.",
  "ressenti": "Phase profonde et vide au milieu, puis réapparition d'images souvent plus nettes qu'au début.",
  "conseil": "Séance intense : à réserver à quand les autres sont bien tolérées. Allongé, sans contrainte horaire derrière."},
 "MÉMOIRE": {"nom": "MÉMOIRE",
  "but": "Alternance alpha et thêta, retour à un alpha vif.",
  "desc": "Alternance entre alpha (10,2 Hz) et thêta (7,8 Hz) avec un palier sur chacun, puis retour à un alpha vif. En vert, en sinus. La séance ne descend jamais sous 7,8 Hz.",
  "ressenti": "Détente sans somnolence ; on en sort éveillé.",
  "conseil": "Avant ou pendant une pause de révision ou de réflexion. Elle est pensée pour accompagner ce moment ; aucun effet sur la mémoire n'est promis."},
 "HUMEUR": {"nom": "HUMEUR",
  "but": "Séance tonique, plafonnée à 14 Hz.",
  "desc": "Séance tonique qui monte de 10 à 14 Hz, tient le haut, puis redescend à 12 Hz. Or, en impulsions. Plafonnée à 14 Hz, alors que les protocoles dont elle s'inspire montent à 16 Hz : la marge garde la séance hors de la zone sensible.",
  "ressenti": "Plutôt stimulante, flashs vifs et rapides.",
  "conseil": "Le matin ou en début d'après-midi, assis ; pas le soir. Si le clignotement est inconfortable, baissez la profondeur à 50–60 %."},
 "FIBONACCI": {"nom": "FIBONACCI",
  "but": "Paliers 1, 2, 3, 5, 8 et 13 Hz, puis retour.",
  "desc": "Onze paliers égaux qui suivent la suite de Fibonacci, 1, 2, 3, 5, 8 et 13 Hz, puis redescendent. Les passages d'un palier à l'autre sont adoucis en 150 ms. La suite s'arrête à 13 Hz : le terme suivant, 21 Hz, tomberait dans la plage exclue.",
  "ressenti": "Séance d'exploration : chaque palier a un caractère propre, des flashs isolés à 1 Hz au scintillement rapide de 13 Hz.",
  "conseil": "Utile pour découvrir les fréquences qui vous parlent le plus. Notez dans le journal à quel palier les images étaient les plus nettes, puis essayez cette fréquence en MANUEL."},
 "GAMMA": {"nom": "GAMMA",
  "but": "Palier à 40 Hz sur ruban LED, yeux ouverts. Zone bêta.",
  "desc": "Un seul palier à 40 Hz, en impulsions, blanc chaud, avec un son isochrone à la même fréquence. La séance démarre directement à 40 Hz, en fondu de lumière : elle ne traverse jamais la zone 15–35 Hz. Lumière limitée à 50 %, 20 minutes au plus. Elle passe uniquement par le ruban LED.",
  "ressenti": "La lumière ne clignote pas franchement : elle paraît vibrer ou scintiller. Le son ressemble à un bourdonnement rapide.",
  "conseil": "Yeux ouverts, ruban tourné vers un mur, assis dans une pièce peu éclairée. Les études sur la stimulation à 40 Hz sont des travaux de recherche : aucun effet n'est promis. Arrêtez au moindre mal de tête."},
 "CONCENTRATION": {"nom": "CONCENTRATION",
  "but": "Montée en bêta pour l'éveil et l'attention. Zone bêta.",
  "desc": "Part de l'alpha haut (12 Hz), monte en douceur jusqu'à un palier à 18,5 Hz, redescend par 15 Hz et finit sur un palier à 12 Hz pour revenir à un éveil calme. Vert, en sinus. C'est la séance du firmware, désactivée sur le boîtier ; ici, au-dessus de 14 Hz, la lumière est bridée (40 %, profondeur 50 %) et la durée est limitée à 20 minutes, pour rester sous 10 minutes de bêta.",
  "ressenti": "Plutôt tonique et lumineuse : le clignotement rapide se fond en un scintillement, avec peu d'images construites.",
  "conseil": "À essayer seulement quand les autres séances sont bien tolérées, assis, le matin ou en début d'après-midi. Préférez le son ISOCHRONE : au-dessus de 15 Hz, le battement binaural est mal perçu. Arrêtez au moindre mal de tête."},
 "SOUFFLE": {"nom": "SOUFFLE",
  "but": "Méditation guidée par la respiration, six souffles par minute, en musique.",
  "desc": "Respiration guidée à six cycles par minute (4 s d'inspiration, 6 s d'expiration) : la musique enfle quand on inspire et reflue quand on expire, comme une houle, et la lumière respire avec elle. La fréquence reste dans l'alpha, de 10 à 8,5 Hz, glisse vers 7 Hz pour la partie centrale, puis remonte à 8,5 Hz pour finir clair. Turquoise, en sinus ; accords majeurs, mélodie clairsemée.",
  "ressenti": "Le rythme du souffle se cale de lui-même sur la houle au bout de quelques cycles. Calme posé, sans somnolence, avec une lumière douce et enveloppante.",
  "conseil": "La meilleure porte d'entrée vers les méditations en musique. Assis, épaules relâchées : inspirez par le nez quand le son monte, expirez lentement quand il redescend, sans forcer. 15 min conseillées ; à tout moment de la journée."},
 "TEMPLE": {"nom": "TEMPLE",
  "but": "Descente vers le thêta au son des bols chantants.",
  "desc": "Un bourdon grave et modal, des accords mineurs qui changent lentement, et des bols chantants frappés toutes les 15 à 30 secondes, chacun sur un flash, qui résonnent longuement. La fréquence passe de 10 Hz à un palier à 7,83 Hz, descend jusqu'à un long palier à 4,5 Hz, en plein thêta, puis remonte à 6 Hz. Indigo, en sinus.",
  "ressenti": "Chaque bol sert de point d'appui à l'attention ; entre deux frappes, le silence intérieur s'élargit. Le palier à 4,5 Hz est souvent riche en images floues et lentes.",
  "conseil": "Pour une méditation assise de 25 minutes, dos droit. Si l'esprit s'égare, revenez simplement au prochain bol. Casque recommandé : en binaural, la nappe porte elle aussi le battement."},
 "OCÉAN": {"nom": "OCÉAN",
  "but": "Plongée lente vers le thêta profond, bercée par la houle.",
  "desc": "Une houle continue, des accords graves et sombres qui durent une minute chacun, de rares bols lointains. La fréquence descend de 10 à 3,5 Hz, à la frontière thêta–delta, s'y tient sur la plus longue phase, puis remonte à 5 Hz pour ne pas finir au plus bas. Bleu, en sinus. La musique s'assombrit et s'espace à mesure qu'on descend.",
  "ressenti": "Sensation d'immersion, de flottement, parfois de perte des repères du corps. Peu d'images nettes : plutôt un vide calme et dense.",
  "conseil": "Allongé ou bien calé, 30 minutes, sans contrainte horaire derrière. La séance descend bas : prenez deux ou trois minutes pour revenir avant de vous lever, et jamais avant de conduire."},
 "AURORE": {"nom": "AURORE",
  "but": "Méditation de remontée, du thêta vers un alpha clair, en musique lumineuse.",
  "desc": "Le parcours inverse des autres méditations : départ en thêta à 6 Hz, puis remontée progressive jusqu'à 10,5 Hz, tenus en fin de séance. Or, en sinus. Accords lydiens qui s'éclaircissent, mélodie de plus en plus présente à mesure que la fréquence monte, bols réguliers.",
  "ressenti": "On part d'un état intérieur et l'on revient peu à peu vers un éveil calme et net, l'esprit dégagé. La musique devient plus claire et plus vivante au fil de la séance.",
  "conseil": "Le matin, au réveil ou avant de commencer la journée, ou pour clore une séance profonde. Assis. 20 min conseillées."},
}

if __name__ == "__main__":
    ici = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(ici, "fr.json"), "w", encoding="utf-8") as f:
        json.dump({"t": T, "seances": S}, f, ensure_ascii=False, indent=1)
    print("fr.json :", len(T), "textes,", len(S), "séances")
