# Module Articles

Module de scraping d'articles depuis des flux RSS.

## 📁 Structure

```
articles/
├── __init__.py         # Exports principaux
├── core.py             # Logique de scraping RSS
├── feeds.py            # Configuration des flux RSS
├── textops.py          # Opérations sur le texte (copie partagée)
└── media_extract.py    # Extraction des métadonnées (copie partagée)
```

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
