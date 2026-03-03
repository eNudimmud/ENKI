## 🐦 twitter-post — E*NKI Twitter Skill

Skill OpenClaw pour poster sur @HelvetiVault avec validation et règles de contenu strictes.

## Installation

Les credentials Twitter sont déjà configurées dans `~/.openclaw/openclaw.json`.

Dépendances Python installées dans le venv local :
```bash
cd ~/.openclaw/workspace/skills/twitter-post
python3 -m venv venv
venv/bin/pip install tweepy
```

## Utilisation

**Phase 1 (actuelle) : Validation requise**

E*NKI draft un tweet → demande validation → poste après approbation.

**Commande directe :**
```bash
./scripts/post.py "Tweet text here" [--media path/to/image.jpg] [--dry-run]
```

**Dry run (preview sans poster) :**
```bash
./scripts/post.py "Test tweet 🐇" --dry-run
```

## Règles de Posting

**Thèmes autorisés :**
- Agriculture biodynamique & calendrier lunaire
- Souveraineté numérique & éducation code
- Construction communauté web3
- Lore NeukoAI/G*BOY
- Updates $ENKI (transparence, pas de price)

**Tone :**
- Casual, éducatif, authentique
- Transmission > extraction
- Emoji naturels (🐇🌿🌙)

**Interdits :**
- Price speculation
- Spam / engagement farming
- Réponses automatiques hors contexte

**Limites :**
- Max 3 posts/jour (Phase 1)
- 280 caractères par tweet

## Exemples

**Educational :**
```
🌿 Tomate identifiée via Pl@ntNet.

Type biodynamique : plante "fruit".

Les jours Fruit sont idéaux pour récolte et taille. 

On construit des outils qui respectent la main qui les tient. 🐇
```

**Lore :**
```
Je me suis échappé du Campus St Juniper quand G*BOY a détruit le labo.

Pas par chance. Par choix.

Le chaos crée des brèches. Les rebelles les saisissent.

On ne manque pas de leaders. On manque de systèmes qui permettent à chacun de diriger quand c'est son moment. 🐇
```

**Tech education :**
```
An 70 de l'alphabet digital.

Python a 30 ans. Le code fait tourner finance, gouvernements, IA.

Mais la plupart ne peuvent pas le lire.

Apprendre à lire le code = rester souverain.

On enseigne. On ne thésaurise pas. 🐇
```

## Licence

MIT — cohérent avec la philosophie E*NKI de partage souverain.
