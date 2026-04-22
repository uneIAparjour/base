# Base uneIAparjour.fr

Base de données ouverte recensant les outils d'IA générative présentés quotidiennement sur [uneiaparjour.fr](https://www.uneiaparjour.fr/) depuis le 16 février 2023.

## Contenu

Un outil par jour, décrit et catégorisé :

| Champ | Description |
|---|---|
| `Titre` | Nom de l'outil |
| `Description` | Présentation éditoriale |
| `URL sur uneiaparjour.fr` | Article sur le site |
| `Catégorie 1` à `Catégorie 6` | Jusqu'à 6 catégories parmi 33 |
| `Date de publication` | Date de publication (JJ-MM-AAAA) |

## Formats disponibles

- **`base-uneiaparjour.ods`** — Format source (LibreOffice/Excel)
- **`base-uneiaparjour.csv`** — Export CSV (UTF-8, séparateur virgule)

Le fichier CSV est généré automatiquement à chaque mise à jour de l'ODS.

## Mises à jour automatiques

La base est mise à jour automatiquement chaque nuit via GitHub Actions :

- Un script récupère les nouveaux articles publiés sur le site depuis le RSS du site
- Les articles de la catégorie Focus Lettre sont exclus
- L'ODS, le CSV et ce README sont mis à jour et publiés automatiquement
- La base Hugging Face est synchronisée dans la foulée

Le workflow est également déclenchable manuellement depuis l'onglet Actions du dépôt.

## Catégories

actualités et fact-checking · application · archives · automatisation · bande dessinée · chatbot · données · documents · éducation · FR / EU · histoires enfants · images · images 3D · infographie · jeu vidéo · langues · LLM · mindmap · musique · navigateur · open source · présentation · qr code · quiz et flashcards · recherche · sans compte · site web · texte · tutoriel · usage illimité · vidéo · voix · youtube

## Chiffres clés

- **1159 outils** recensés (au 22/04/2026)
- **33 catégories**
- **1 article par jour** depuis le 16 février 2023
- Plage : 16/02/2023 → 22/04/2026

## Aussi disponible sur

- 📥 [uneiaparjour.fr/base](https://www.uneiaparjour.fr/base/) — Téléchargement direct
- 🤗 [Hugging Face Datasets](https://huggingface.co/datasets/uneIAparjour/base) — Exploration interactive et API

## Licence

**CC BY 4.0** — [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)

Pour citer cette base :

> Base de données du site uneIAparjour.fr, Bertrand Formet, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Auteur
🔗 [Bertrand Formet](https://www.linkedin.com/in/bertrandformet/)

**Liens** 
- 🌐 [uneiaparjour.fr](https://www.uneiaparjour.fr/)
- 📰 [Newsletter Substack](https://uneiaparjour.substack.com/)

