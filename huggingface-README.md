---
license: cc-by-4.0
language:
  - fr
pretty_name: "Base uneIAparjour.fr — Applications IA génératives"
size_categories:
  - 1K<n<10K
task_categories:
  - text-classification
tags:
  - ai-tools
  - generative-ai
  - curation
  - french
  - daily-updates
source_datasets: []
dataset_info:
  features:
    - name: Titre
      dtype: string
    - name: Description
      dtype: string
    - name: URL sur uneiaparjour.fr
      dtype: string
    - name: Catégorie 1
      dtype: string
    - name: Catégorie 2
      dtype: string
    - name: Catégorie 3
      dtype: string
    - name: Catégorie 4
      dtype: string
    - name: Catégorie 5
      dtype: string
    - name: Catégorie 6
      dtype: string
    - name: Date de publication
      dtype: string
---

# Base uneIAparjour.fr — Applications IA génératives

Base de données ouverte recensant **un outil d'IA générative par jour** depuis le 16 février 2023, présentés sur [uneiaparjour.fr](https://www.uneiaparjour.fr/).

## Description

Chaque jour, un nouvel outil d'IA générative gratuit ou freemium est testé, décrit et catégorisé. Cette base constitue un observatoire unique de l'évolution du paysage des outils IA accessibles au grand public et aux enseignants.

## Contenu

- **1 093 outils** (au 14 février 2026)
- **33 catégories** : chatbot, images, texte, vidéo, musique, éducation, open source…
- **Période** : 16 février 2023 → 14 février 2026
- **Langue** : français

## Champs

| Champ | Description |
|---|---|
| `Titre` | Nom de l'outil |
| `Description` | Présentation éditoriale de l'outil |
| `URL sur uneiaparjour.fr` | Lien vers l'article complet |
| `Catégorie 1` à `Catégorie 6` | Jusqu'à 6 catégories |
| `Date de publication` | Date au format JJ-MM-AAAA |

## Utilisation

```python
from datasets import load_dataset

dataset = load_dataset("uneIAparjour/base")
df = dataset["train"].to_pandas()

# Outils de génération d'images
images = df[df["Catégorie 1"] == "images"]
print(f"{len(images)} outils de génération d'images")
```

## Source et mises à jour

Source : [GitHub](https://github.com/uneIAparjour/base)
Site : [uneiaparjour.fr](https://www.uneiaparjour.fr/)
Newsletter : [Substack](https://uneiaparjour.substack.com/)

## Auteur et licence

**Bertrand Formet** 

Licence : [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

> Base de données du site uneIAparjour.fr au 14/02/2026, Bertrand Formet, licence CC BY 4.0.
