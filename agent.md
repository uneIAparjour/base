# agent.md — Base uneIAparjour.fr

## Contexte

Ce dépôt contient la base de données du site uneiaparjour.fr : un outil d'IA générative présenté chaque jour depuis le 16 février 2023 par Bertrand Formet.

## Structure des fichiers

```
base-uneiaparjour.ods    # Source de vérité (LibreOffice Calc)
base-uneiaparjour.csv    # Export automatique (ne pas modifier à la main)
README.md                 # Documentation publique
agent.md                  # Ce fichier (instructions pour agents IA)
```

## Schéma de données

| Colonne | Type | Obligatoire | Description |
|---|---|---|---|
| Titre | texte | oui | Nom de l'outil |
| Description | texte | oui | Présentation éditoriale complète |
| URL sur uneiaparjour.fr | URL | oui | Lien vers l'article sur le site |
| Catégorie 1 à 6 | texte | cat. 1 oui | Parmi les 33 catégories existantes |
| Date de publication | date | oui | Format JJ-MM-AAAA |

## Règles impératives

1. **Ne jamais modifier les URLs** — Les extraire fidèlement, ne jamais les inventer
2. **Ne jamais modifier le CSV directement** — Il est généré automatiquement depuis l'ODS
3. **Format de date** : toujours `JJ-MM-AAAA`
4. **Catégories** : utiliser exclusivement les 33 catégories existantes, respecter la casse exacte (minuscules sauf `FR / EU` et `LLM`)
5. **Un article = un jour** — Sauf rares exceptions (bonus 365e jour d'une année)
6. **Ordre** : chronologique inverse (plus récent en premier)

## Les 33 catégories valides

```
actualités et fact-checking, application, archives, automatisation,
bande dessinée, chatbot, données, documents, éducation, FR / EU,
histoires enfants, images, images 3D, infographie, jeu vidéo, langues,
LLM, mindmap, musique, navigateur, open source, présentation, qr code,
quiz et flashcards, recherche, sans compte, site web, texte, tutoriel,
usage illimité, vidéo, voix, youtube
```

## Republications

Certains outils sont présentés une seconde fois après évolution significative. Dans ce cas :
- Le titre est identique ou similaire
- L'URL peut différer (suffixe `-2` ou slug différent)
- La description est mise à jour
- Les deux entrées coexistent dans la base

## Source de vérité

- **Dates de publication** : le site WordPress fait foi (pas le flux RSS qui peut contenir des dates de republication)
- **Descriptions** : le contenu complet de l'article WordPress fait foi
- **Catégories** : les catégories WordPress de chaque article font foi

## Mise à jour

La base est mise à jour désormais tous les 6 mois environ. Le CSV est regénéré automatiquement via GitHub Actions à chaque push de l'ODS.
