# Module Articles

Module de scraping d'articles depuis des flux RSS.

## 📁 Structure

```
articles/
├── __init__.py         # Exports principaux
├── core.py             # Logique de scraping RSS
├── feeds.py            # Configuration des flux RSS
├── filters.py          # Filtrage par mots-clés
├── keywords.py         # Liste des mots-clés
├── textops.py          # Opérations sur le texte
├── media_extract.py    # Extraction des métadonnées
├── http_state.py       # Sessions HTTP avec headers
└── README.md
```

**Module autonome** : Tout le nécessaire pour le scraping RSS est contenu dans ce dossier.

## 🎯 Utilisation

```python
from scraping.articles import get_articles, FR_FEEDS

# Scraper les dernières 24h
articles = get_articles(FR_FEEDS, query="", since_hours=24, include_meta=True)
```

## ⚙️ Fonctionnalités

- Parsing de flux RSS avec `feedparser`
- Filtrage par mots-clés (Ukraine, Russie, OTAN)
- Extraction des métadonnées (auteur, médias)
- Normalisation du texte
- Gestion des erreurs HTTP
