# AXIOME - Backend

Backend Flask + Scraping RSS pour le média indépendant AXIOME dédié au conflit Ukraine-Russie.

## Structure

```
Back/
├── scraping/           # Module de scraping RSS + YouTube
│   ├── __init__.py
│   ├── api.py         # API Flask avec endpoints
│   ├── core.py        # Logique de parsing RSS articles
│   ├── video.py       # Scraping videos YouTube
│   ├── archive.py     # Persistence des articles/vidéos dans archive.json
│   ├── feeds.py       # Listes de flux RSS français + YouTube
│   ├── filters.py     # Filtrage des articles
│   ├── keywords.py    # Mots-clés de filtrage
│   ├── media_extract.py
│   ├── textops.py
│   ├── http_state.py
│   ├── scraping.py
│   └── archive.json   # Archive permanente des articles/vidéos
├── venv/              # Environnement Python virtuel
├── requirements.txt   # Dépendances Python
└── README.md
```

## Installation

### 1. Créer l'environnement virtuel

```bash
python -m venv venv
```

### 2. Activer l'environnement virtuel

**Windows (cmd):**
```bash
venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

## Démarrage

### Lancer l'API Flask (port 5000)

```bash
python -m scraping.api
```

L'API sera disponible sur `http://127.0.0.1:5000`

### Endpoints disponibles

- **GET `/articles`** - Récupère les articles filtrés
  - Paramètres:
    - `q` : Requête de recherche (par défaut: `ukraine`)
    - `hours` : Nombre d'heures (par défaut: `48`)
    - `meta` : Inclure métadonnées (1 ou 0, par défaut: `1`)

Exemple:
```bash
curl "http://127.0.0.1:5000/articles?q=ukraine&hours=48&meta=1"
```

## Features

- ✅ Scraping automatique de 50+ flux RSS français
- ✅ Scraping automatique de 27 chaînes YouTube (français + international)
- ✅ Archive permanente des articles et vidéos dans archive.json
- ✅ Filtrage par mots-clés Ukraine, Russie, NATO
- ✅ Cache 15 minutes des résultats
- ✅ Extraction d'images et auteurs
- ✅ Support CORS pour connexion au frontend
- ✅ Planification automatique du scraping (15 min)
- ✅ Détection et prévention des doublons
- ✅ Thread-safe archive operations

## Configuration

### Flux RSS Articles
Les flux RSS articles sont définis dans `scraping/feeds.py` avec les meilleures sources françaises:
- Le Monde, Figaro, Franceinfo
- RFI, France 24
- Et 45+ autres sources

### Chaînes YouTube
Les chaînes YouTube pour vidéos sont dans `FR_VIDEO_FEEDS` (scraping/feeds.py):
- **Français**: ARTE, Le Monde, France 24, BFM TV, CNews, France Inter, Mediapart, Brut, Konbini
- **International**: BBC News, DW News, Euronews, CNN, ABC News, CBS News, Fox News, Reuters, Al Jazeera, Sky News
- **Military**: Warthog Defense, Defense Updates
- **Russian/Eastern**: TV Rain, Популярная политика
- **Documentary**: National Geographic, Discovery Channel

## API Endpoints

### GET /articles
Récupère les articles filtrés

**Paramètres**:
- `q` (string): Mots-clés de recherche (défaut: "ukraine")
- `hours` (int): Articles des N dernières heures (défaut: 48)
- `meta` (int): Inclure métadonnées (défaut: 1)

**Réponse**:
```json
{
  "articles": [
    {
      "source": "Le Monde",
      "title": "Titre de l'article",
      "link": "https://...",
      "published": "2025-12-15T10:30:00+00:00",
      "author": "Nom Auteur",
      "media": {"url": "image.jpg"},
      "image": "image.jpg",
      "publishedTime": 1765000000000
    }
  ]
}
```

### GET /videos
Récupère les vidéos YouTube

**Paramètres**:
- `hours` (int): Vidéos des N dernières heures (défaut: 48)
- `channel` (string): Filtrer par chaîne (optionnel)
- `limit` (int): Nombre max de vidéos (défaut: 30)

**Réponse**:
```json
{
  "videos": [
    {
      "channel": "ARTE",
      "title": "Titre de la vidéo",
      "link": "https://youtube.com/watch?v=...",
      "published": "2025-12-15T10:30:00+00:00",
      "thumbnail": "image.jpg",
      "summary": "Description de la vidéo",
      "type": "youtube",
      "publishedTime": 1765000000000
    }
  ]
}
```

### GET /stats
Statistiques de l'archive permanente

**Réponse**:
```json
{
  "total_articles": 150,
  "total_videos": 85,
  "last_update": "2025-12-15T12:00:00+00:00"
}
```

## Archive Persistance

L'archive est sauvegardée dans `scraping/archive.json` avec la structure:
```json
{
  "articles": [
    {
      "source": "...",
      "title": "...",
      "link": "...",
      "published": "...",
      "archived_at": "2025-12-15T12:00:00+00:00"
    }
  ],
  "videos": [
    {
      "channel": "...",
      "title": "...",
      "link": "...",
      "published": "...",
      "archived_at": "2025-12-15T12:00:00+00:00"
    }
  ]
}
```

**Fonctionnalités**:
- Tous les articles/vidéos scrapés sont automatiquement archivés
- Les doublons (par URL) sont détectés et ignorés
- Chaque article/vidéo reçoit un timestamp `archived_at`
- Archive thread-safe avec locking mutex
- Historique permanent conservé
- La Croix, Libération
- Et 40+ autres sources
