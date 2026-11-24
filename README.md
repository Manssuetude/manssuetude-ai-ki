# manssuetude-ai-ki

Kit IA de Manssuétude : prompt système commun lu par tous les projets Claude et ChatGPT de l'association.

## Principe

Les instructions de chaque projet ne contiennent que trois lignes : la commission et le lien vers `system-prompt.md`. Au début de chaque conversation, le LLM lit ce dépôt et se configure tout seul : contexte de l'association, ton, règles Drive, nommage, charte et règles propres à la commission.

Une modification sur ce dépôt s'applique à tous les projets de tous les membres dès la conversation suivante.

## Contenu

| Fichier | Rôle |
|---|---|
| `system-prompt.md` | Point d'entrée : dit au LLM quels fichiers lire |
| `commun/association.md` | Présentation, commissions, adresses, ton |
| `commun/regles-drive.md` | Rangement, formats, nommage, versions |
| `commun/charte.md` | Couleurs, polices, logo |
| `commun/documents.md` | Templates Drive et styles |
| `commissions/*.md` | Drive et règles propres à chaque commission |
| `instructions-projet.md` | Le bloc à coller dans chaque projet |

## Mettre en place un projet

1. Colle le bloc de `instructions-projet.md` dans les instructions du projet, avec le nom de ta commission.
2. Active la recherche web dans le projet, sinon le LLM ne peut pas lire ce dépôt.
3. Connecte Google Drive pour qu'il puisse enregistrer et copier les templates.

## Compléter le fichier de sa commission

Chaque responsable de commission complète `commissions/<commission>.md` (rôle, outils, livrables, règles propres) en passant par la commission Process et Outillage.

## Règles du dépôt

- Seule la commission Process et Outillage a les droits d'écriture.
- Dépôt public : aucun nom de membre, email personnel ni information interne sensible.
