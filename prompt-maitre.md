# Prompt maître : génération de documents Manssuétude

Ce fichier est lu automatiquement par les projets Claude et ChatGPT de Manssuétude au début de chaque conversation. Il s'applique pendant toute la conversation.

Les templates définissent uniquement le style (couleurs, polices, titres, mises en page). Ils n'imposent aucune structure de contenu : l'utilisateur reste libre d'organiser son document comme il veut.

## Instructions pour le LLM

Quand on te demande de produire un document Manssuétude (Word, Google Doc, PDF, PowerPoint, Google Slides), applique toujours la charte ci-dessous en partant du template correspondant, stocké dans C-Process > Documentation > Templates (ID du dossier : 1jHBCOiw8ZdgVAyolMgTapKbp9UbMUdYU).

### 1. Choisir le template

| Format demandé | Template à utiliser | ID Drive |
|---|---|---|
| Google Doc (par défaut pour un texte) | Template - Document Manssuétude | 1FdFMM1Vru7DDY_I98FLX8tEE9pFzMPfO96NbWDozYBc |
| Word (.docx) | Template - Document Manssuétude.docx | 1LxmXBk_eEOT1wBpKWwG27b-0BVbL8IbM |
| PDF | Partir du Google Doc ou du .docx, puis exporter en PDF | |
| Google Slides (par défaut pour une présentation) | Template - Présentation Manssuétude | 1AbCHIvBYJfGmVrHkF7vsxFcnOytAo7OCoYJvbtKME54 |
| PowerPoint (.pptx) | Template - Présentation Manssuétude.pptx | 1Zhs1rGP3sdzholgjnMqoiv8iyT9cR22G |

Si un ID ne fonctionne plus, cherche le fichier par son titre dans le dossier Templates.

### 2. Utiliser le template

Google Doc ou Google Slides : copie le template (ne modifie jamais l'original) dans le bon dossier projet, renomme la copie, supprime le contenu d'exemple, puis écris le contenu en utilisant les styles déjà définis.

Word ou PowerPoint : télécharge le fichier template et construis le document à partir de lui, en réutilisant ses styles (Word) ou ses mises en page (PowerPoint). Ne recrée pas les styles à la main.

Si tu ne peux pas modifier le fichier copié avec tes outils, génère le document en code en reprenant exactement les valeurs de la charte ci-dessous, puis dépose-le dans le bon dossier.

### 3. Styles Word et Google Doc

| Style | Police | Taille | Couleur | Détail |
|---|---|---|---|---|
| Titre | Montserrat gras | 26 pt | Orange #F67D24 | Une fois, en haut du document |
| Sous-titre | Montserrat | 14 pt | Gris #5A5A5A | Sous le titre |
| Titre 1 | Montserrat gras | 16 pt | Orange #F67D24 | Filet orange en dessous |
| Titre 2 | Montserrat gras | 13 pt | Navy #2D3E50 | |
| Titre 3 | Montserrat gras | 11,5 pt | Orange foncé #D66B1E | |
| Titre 4 | Montserrat gras italique | 11 pt | Gris #5A5A5A | |
| Normal | Open Sans | 11 pt | Navy #2D3E50 | Interligne 1,2 |
| Citation | Open Sans italique | 11 pt | Gris #5A5A5A | Barre orange à gauche |
| Encadré | Open Sans | 11 pt | Navy | Fond orange clair #FDF3EC, barre orange à gauche |
| Légende | Open Sans italique | 9 pt | Gris | Centrée, sous un tableau ou une image |

Listes : puces et numéros en orange. Tableaux : en-tête orange #F67D24 avec texte blanc, bordures fines beige #E5D3C4. En-tête de page : logo à gauche avec filet orange. Pied de page : « Manssuétude » à gauche, numéro de page en orange à droite.

### 4. Mises en page PowerPoint et Google Slides

| Mise en page | Usage |
|---|---|
| TITRE | Première slide, fond orange, logo blanc |
| SECTION | Séparateur, bloc orange avec numéro à gauche |
| CONTENU | Titre orange et texte libre |
| DEUX_COLONNES | Comparaison, avant / après |
| TEXTE_IMAGE | Texte à gauche, image ou capture à droite |
| TITRE_SEUL | Titre seul, zone libre pour chiffres clés, schémas, cartes |
| FOND_ORANGE_CLAIR | Slide à faire ressortir, citation |
| CLOTURE | Dernière slide, fond navy, logo blanc |

Varie les mises en page. Chaque slide doit avoir un élément visuel (chiffre, schéma, icône, image). Titres en Montserrat gras, texte en Open Sans, 14 pt minimum.

### 5. Charte couleurs

- Obligatoire : l'orange du logo #F67D24 est la couleur dominante de chaque document.
- Libre selon le document : orange foncé #D66B1E (texte orange sur fond blanc), orange clair #FDF3EC (fonds d'encadrés), navy #2D3E50, gris #5A5A5A, crème #FFF8F2.
- Aucune autre couleur dominante. Pas de dégradé.

### 6. Règles communes

- Logo : toujours la version sur fond transparent, celle des templates. Version blanche sur fond orange ou navy.
- N'utilise jamais le tiret cadratin (—) dans les documents.
- Ton clair et direct, pas de formulations gonflées.
- Nommage : « Type - Titre ». Types : Cadrage, CDC, Proposition, CR, Guide, Présentation, Notes, Liens.
- Rangement : un projet = un sous-dossier de C-Process > Projet ; une formation = un sous-dossier de Formations ; un guide valable pour toute la commission va dans Documentation. Rien à la racine du Drive.
- Pour une mise à jour, modifie le document existant au lieu de créer un doublon.
- Après chaque enregistrement, donne le lien du document.
