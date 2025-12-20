# Module Videos

Module de scraping de vidéos depuis YouTube via l'API YouTube Data v3.

## 📁 Structure

```
videos/
├── __init__.py     # Exports principaux
├── core.py         # Interface de scraping vidéo
├── api.py          # Implémentation YouTube Data API v3
└── feeds.py        # Configuration des chaînes YouTube
```

## 🎯 Utilisation

```python
from scraping.videos import get_videos

# Scraper les dernières 24h
videos = get_videos(since_hours=24, channel=None)
```

## ⚙️ Fonctionnalités

- Récupération via YouTube Data API v3
- Filtrage par mots-clés (Ukraine, Russie, OTAN)
- Pagination optimisée (arrêt sur vidéos anciennes)
- Archivage immédiat par chaîne
- Support multi-chaînes (français + international)

## 🔑 Configuration

L'API nécessite une clé YouTube Data API v3 :
```bash
export YT_API_KEY="votre_cle_api"
```

Ou utilise la clé par défaut définie dans `api.py`.
