# manssuetude-ai-ki

Kit IA de Manssuétude : prompt système commun à tous les assistants IA de l'association (Claude, ChatGPT, Gemini ou autre), pour tous les membres et toutes les commissions.

## Principe

Le dépôt contient toutes les consignes : contexte de l'association, ton, règles Drive, nommage, charte, et règles propres à chaque commission. Les assistants les lisent au début de chaque conversation. Une modification ici s'applique à tous les membres dès la conversation suivante.

Un membre peut faire partie de plusieurs commissions : l'assistant charge les fichiers de chacune et range chaque document dans le Drive de la commission concernée. Le Président, le Vice-Président et le Secrétaire général font partie de toutes les commissions.

## Selon l'outil

| Outil | Mise en place | Fichier | État |
|---|---|---|---|
| **Claude** (projet) | Chaque membre colle un bloc dans les instructions de son projet | `instructions-projet.md` | Lien lisible, test en projet à faire |
| **ChatGPT** | Un GPT personnalisé commun, partagé par lien | `gpt/README.md` | Projets ChatGPT : échec de lecture ; GPT : à tester |
| **Gemini** (Gem) | Chaque membre colle le même bloc dans les instructions de son Gem | `instructions-projet.md` | À tester |
| **Autre outil** | Même bloc, si l'outil accepte des instructions permanentes et ouvre les liens web | `instructions-projet.md` | À tester |

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
