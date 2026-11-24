# GPT personnalisé « Assistant Manssuétude »

Les projets ChatGPT n'arrivent pas à ouvrir le lien du prompt système (leur outil de navigation passe par un moteur de recherche qui ne trouve pas ce fichier). Le GPT personnalisé contourne ce problème grâce à une **Action** : un appel direct aux fichiers du dépôt, sans passer par la recherche web.

Un seul GPT pour toute l'association. Chaque membre l'utilise via un lien, quelle que soit sa ou ses commissions.

## Créer le GPT (une seule fois, compte ChatGPT payant requis)

1. Dans ChatGPT : **GPTs**, puis **Créer**, puis l'onglet **Configurer**.
2. **Nom** : `Assistant Manssuétude`
3. **Description** : `Assistant IA des membres de Manssuétude : applique la charte, les règles de rangement Drive et les règles de chaque commission.`
4. **Instructions** : colle le contenu de `gpt/instructions.md`.
5. **Amorces de conversation** (conversation starters) :
   - `Je suis dans la commission Process et Outillage`
   - `Je fais partie de plusieurs commissions`
   - `Rédige le compte rendu de notre réunion`
   - `Quelles règles appliques-tu pour ranger un document ?`
6. **Connaissances** (facultatif, en secours) : ajoute les fichiers de `commun/`. Attention, ils ne se mettent pas à jour seuls : à renvoyer après chaque modification importante.
7. **Capacités** : active la recherche web et l'interpréteur de code (pour générer des fichiers Word, PowerPoint ou PDF).
8. **Actions**, puis **Créer une action** :
   - Authentification : **Aucune**
   - Schéma : colle le contenu de `gpt/action-openapi.yaml`
   - Politique de confidentialité : `https://github.com/Manssuetude/manssuetude-ai-ki/blob/main/gpt/confidentialite.md`
   - Teste l'action `getSystemPrompt` avec le bouton **Tester** : la réponse doit contenir le code de contrôle.
9. **Créer**, puis partage avec **Toute personne disposant du lien** (ou ton espace de travail si l'association a ChatGPT Team).
10. Envoie le lien aux membres.

## Vérifier que ça marche

Ouvre le GPT, écris « Je suis dans la commission Process et Outillage ». La première réponse doit commencer par :

`Configuration Manssuétude chargée (MNS-CFG-2611) : Process et Outillage`

Au premier appel, ChatGPT demande l'autorisation d'appeler `raw.githubusercontent.com` : choisis **Toujours autoriser**.

## Limites

- Le GPT ne peut pas toujours enregistrer directement dans Google Drive. Dans ce cas, il fournit le fichier et indique le Drive, le dossier et le nom à utiliser.
- Les membres avec un compte ChatGPT gratuit peuvent utiliser le GPT, avec des limites d'usage.
- Toute modification du dépôt GitHub s'applique au GPT dès la conversation suivante, sans le reconfigurer. Seul `gpt/instructions.md` ou `gpt/action-openapi.yaml` demandent de modifier le GPT à la main.
