# manssuetude-ai-ki

Kit IA de Manssuétude : prompt système commun à tous les assistants IA de l'association, pour tous les membres et toutes les commissions.

## Principe

Le dépôt contient toutes les consignes : contexte de l'association, ton, règles Drive, nommage, charte, et règles propres à chaque commission. Les assistants les lisent au début de chaque conversation. Une modification ici s'applique à tous les membres dès la conversation suivante.

Un membre peut faire partie de plusieurs commissions : l'assistant charge les fichiers de chacune et range chaque document dans le Drive de la commission concernée.

## Deux façons de l'utiliser

| Outil | Mise en place | Fichier |
|---|---|---|
| **Claude** (projet) | Chaque membre colle un bloc dans les instructions de son projet | `instructions-projet.md` |
| **ChatGPT** | Un GPT personnalisé commun, partagé par lien (les projets ChatGPT n'arrivent pas à lire le dépôt) | `gpt/README.md` |

Vérification : la première réponse de l'assistant commence par « Configuration Manssuétude chargée (MNS-CFG-...) ». Sinon, la configuration n'est pas chargée.

## Contenu

| Fichier | Rôle |
|---|---|
| `system-prompt.md` | Point d'entrée : code de contrôle, fichiers à lire, gestion multi-commissions |
| `commun/association.md` | Présentation, commissions, adresses, ton |
| `commun/regles-drive.md` | Rangement, formats, nommage, versions |
| `commun/charte.md` | Couleurs, polices, logo |
| `commun/documents.md` | Templates Drive et styles |
| `commissions/*.md` | Drive et règles propres à chaque commission |
| `instructions-projet.md` | Bloc à coller dans un projet Claude |
| `gpt/` | Instructions, Action et politique de confidentialité du GPT personnalisé |
| `scripts/check_links.py` | Monitoring des liens (lancé par GitHub Actions) |

## Compléter le fichier de sa commission

Chaque responsable de commission complète `commissions/<commission>.md` (rôle, outils, livrables, règles propres) en passant par la commission Process et Outillage.

## Règles du dépôt

- Seule la commission Process et Outillage a les droits d'écriture.
- Après une modification importante, change le code de contrôle dans `system-prompt.md` (MNS-CFG-2611, puis 2612...).
- Dépôt public : aucun nom de membre, email personnel ni information interne sensible.
