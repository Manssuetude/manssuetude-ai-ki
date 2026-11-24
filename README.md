# manssuetude-ai-kit

Kit IA de Manssuétude : prompts, charte graphique et règles de rangement lus par les LLM des projets de l'association.

## À quoi ça sert

Tous les projets Claude et ChatGPT de l'association lisent le même fichier au début de chaque conversation. Résultat : les documents produits (Google Docs, Word, PDF, Slides, PowerPoint) suivent la même charte et les mêmes règles de nommage et de rangement, quel que soit le membre ou l'outil utilisé.

## Contenu

| Fichier | Rôle |
|---|---|
| `prompt-maitre.md` | Le fichier lu par les LLM : charte, templates, styles, règles communes |
| `instructions-projet.md` | Le bloc à coller dans les instructions de chaque projet Claude ou ChatGPT |

Les templates eux-mêmes (Google Doc, Word, Google Slides, PowerPoint) sont sur le Drive partagé C-Process, dans Documentation > Templates.

## Mettre en place un projet

1. Ouvre les instructions du projet (Claude : « Instructions du projet » ; ChatGPT : « Instructions »).
2. Colle le bloc de `instructions-projet.md`.
3. Active la recherche web dans le projet, sinon le LLM ne peut pas lire ce dépôt.
4. Connecte Google Drive pour qu'il puisse copier les templates.

## Modifier les règles

- Toute modification de `prompt-maitre.md` s'applique à tous les projets dès la conversation suivante.
- Seule la commission Process & Outillage a les droits d'écriture sur ce dépôt.
- Ce dépôt est public : n'y mets aucun nom de membre, email personnel ou information interne.
