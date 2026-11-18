---
name: viral-studio
description: >-
  Studio de contenu viral pour Instagram et TikTok. Trouve, trie et analyse les
  Reels et vidéos TikTok qui marchent dans la niche du rappeur (rap français,
  univers Bagheera), identifie la formule d'accroche de chacun, puis écrit des
  scripts et des idées originales de capsules adaptées à ton univers. Utilise
  ce skill dès que l'utilisateur parle de : reels viraux, tendances, "qu'est-ce
  qui marche", "trouve des vidéos", "trie les reels", "idée de capsule", "script
  TikTok", "script Insta", "idée de vidéo", "adapte ce script", "un contenu
  original", "quoi poster cette semaine", ou colle un lien de Reel ou TikTok.
---

# viral-studio

Un skill qui fait trois choses dans l'ordre : **trouver** les vidéos qui
marchent, **trier** par performance réelle, **créer** des capsules originales.
Il complète `ig-viral` (recherche) et `ig-reel` (écriture) sans les remplacer.

## Règles de base

- Le viral se mesure par le **multiplicateur** : vues divisées par la médiane
  de vues du compte. Une vidéo à plus de 3x est un signal. En dessous de 1,5x,
  c'est le quotidien du compte : ignore-la.
- Ne retiens que les comptes de taille proche de la tienne (environ 10x
  maximum), plus quelques gros comptes pour le format uniquement.
- Une formule copiée telle quelle est fade. On reprend la **structure**
  (accroche, rythme, montée, chute), jamais le texte ni la musique.
- Ne te connecte jamais à Instagram ou TikTok à la place de l'utilisateur, et
  ne demande jamais son mot de passe.

## Étape 1 : trouver

Selon ce que la session permet, dans cet ordre :

1. **Données fournies par l'utilisateur** : liens de Reels/TikTok, captures
   d'écran de statistiques, export CSV, notes de son onglet « Enregistrés ».
   C'est la source la plus fiable.
2. **Recherche web** (WebSearch) : mots-clés de la niche (`rap français`,
   `Romance Dawn`, `clip rap FR`, `dystopie rap`) pour repérer les formats qui
   reviennent. Indique clairement que la recherche donne des tendances
   approximatives, pas des chiffres exacts.
3. **Navigateur**, si un outil de navigation est réellement connecté. Sinon,
   dis-le et passe à 1 ou 2.

Pour chaque vidéo retenue, note : compte, plateforme, lien, date, vues,
multiplicateur (si la médiane est connue), formule d'accroche utilisée.

## Étape 2 : trier

Classe les vidéos par multiplicateur, pas par vues brutes. Regroupe-les par
**formule** (question, affirmation choc, coulisses, avant/après, liste, défi,
mise en scène cinéma). Une formule qui apparaît dans 3 vidéos fortes est plus
utile qu'une vidéo isolée.

Si l'utilisateur fournit un fichier, le script de tri existant peut aider :

```bash
python3 ~/First-Insta/clone-dir/instagram-agent-skill/skills/ig-viral/swipe.py captured.tsv --out swipe.md
```

Si le dossier n'existe pas, fais le tri à la main, en tableau.

## Étape 3 : créer

Pour chaque idée, fournis :

- **Titre interne** (une ligne) et **formule** utilisée
- **Accroche** : les 3 premières secondes, en texte à dire et en texte à l'écran
- **Script** : 15 à 45 secondes, découpé en plans avec ce qu'on voit et ce qu'on dit
- **Adaptation TikTok** et **adaptation Instagram** : mêmes idées, format et
  légende ajustés (TikTok accepte un texte plus long et plus de jargon de
  niche ; Instagram privilégie la première ligne de légende et la sauvegarde)
- **Lien avec l'univers** : rattache l'idée à Romance Dawn, à l'esthétique
  « transmission » ou à l'album, pour qu'elle reste reconnaissable

Pour l'écriture finale du script, enchaîne avec `ig-reel` et `ig-human` pour
retirer les tics d'IA. Pour la légende, utilise `ig-caption`.

## Règles de qualité pour les idées

- Une idée originale combine **une formule qui marche** et **un élément
  propre à l'artiste** (son lieu, son style visuel, une anecdote réelle). Une
  idée sans élément propre se confond avec les autres comptes.
- Propose 5 idées à la fois, classées de la plus simple à la plus ambitieuse,
  avec le temps de tournage estimé.
- Ne fabrique jamais de chiffres de performance. Si tu n'as pas la donnée,
  écris « non vérifié ».
- Pas de droits : ne réutilise ni extrait audio, ni musique, ni image d'un
  autre artiste. Décris ce qu'il faut tourner à la place.

## Format de réponse

1. Ce qui a été trouvé (sources, date, limites)
2. Tableau trié par multiplicateur ou par formule
3. Les 5 idées, avec script et adaptation pour chaque plateforme
4. Une question pour la suite : quelle idée tourner en premier ?
