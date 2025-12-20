# Module Videos

Module de scraping de vidéos depuis YouTube via l'API YouTube Data v3.

## 📁 Structure

```
videos/
├── __init__.py     # Exports principaux
├── core.py         # Interface de scraping vidéo
├── scraper.py      # Implémentation YouTube Data API v3
├── feeds.py        # Configuration des chaînes YouTube
├── keywords.py     # Liste des mots-clés
└── README.md
```

**Module autonome** : Tout le nécessaire pour le scraping YouTube est contenu dans ce dossier.

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

Vous pouvez aussi créer un fichier `.env` (chargé automatiquement) à la racine du projet Back/ pour le développement local :
```
YT_API_KEY=votre_cle_api
```

La clé n'est jamais hardcodée dans le code source. Si `YT_API_KEY` est absente, le scraping vidéo est désactivé.
