# Architecture et Workflow - Archive Unique

## Vue d'ensemble

Le projet utilise **un seul fichier archive.json** partagé entre le backend (scraping) et le frontend (affichage).

## Emplacement unique de l'archive

```
Front/public/archive.json
```

Ce fichier contient :
- `articles[]` : Articles scrapés depuis les flux RSS
- `videos[]` : Vidéos scrapées depuis l'API YouTube

## Workflow Backend → Archive

### 1. Configuration de l'archive (Back/scraping/archive.py)

```python
ARCHIVE_FILE = Path(__file__).parent.parent.parent / "Front" / "public" / "archive.json"
```

Le backend écrit **directement** dans le fichier public du frontend.

### 2. Scraping Articles (Back/scraping/core.py)

**Fonction principale** : `get_articles()`

1. Récupère les flux RSS configurés dans `feeds.py`
2. Filtre par mots-clés Ukraine/Russie/OTAN (via `keywords.py`)
3. Déduplique par lien
4. Ajoute `publishedTime` (timestamp en ms)
5. **Archive immédiatement** via `add_articles()`

**Points clés** :
- Archivage automatique à chaque scraping
- Pas de limite de conservation (add-only)
- Tri par date décroissante
- Déduplication par lien

### 3. Scraping Vidéos (Back/scraping/video_api.py)

**Fonction principale** : `get_all_videos()`

1. Itère sur tous les channels YouTube dans `YOUTUBE_CHANNELS`
2. Pour chaque channel :
   - Scrape via YouTube Data API v3
   - Filtre par mots-clés
   - **Archive immédiatement** via `add_videos()`
3. Retourne toutes les vidéos triées par date

**Points clés** :
- Archivage par channel (immédiat, incrémental)
- Déduplication par lien YouTube
- Support de `stop_after_match` (limite par channel, None = illimité)

### 4. Module d'archivage (Back/scraping/archive.py)

**Fonctions principales** :

- `add_articles(articles)` : Ajoute des articles avec déduplication
- `add_videos(videos)` : Ajoute des vidéos avec déduplication
- `_load_archive()` : Charge et trie l'archive
- `_save_archive(data)` : Sauvegarde avec tri

**Politique** :
- ✅ Add-only (pas de suppression)
- ✅ Déduplication par lien
- ✅ Tri par `publishedTime` décroissant
- ✅ Thread-safe avec `ARCHIVE_LOCK`
- ✅ Ajoute `archived_at` (timestamp ISO)

## Workflow Frontend → Archive

### 1. Chargement de l'archive

Trois composables chargent l'archive :

#### useArticles.ts
```typescript
fetch('/archive.json')  // Charge depuis Front/public/
  .then(data => data.articles)
```
- Utilisé par la page **Articles**
- Tri par `publishedTime` desc
- Auto-refresh toutes les 5 minutes

#### useVideos.ts
```typescript
fetch('/archive.json')
  .then(data => data.videos)
```
- Utilisé par la page **Vidéos**
- Filtres par channel
- Auto-refresh toutes les 5 minutes

#### useArchiveFeed.ts
```typescript
fetch('/archive.json')
  .then(data => {
    articles: data.articles,
    videos: data.videos
  })
```
- Utilisé par la page **En Direct**
- Merge articles + videos
- Normalise les images (thumbnail → image)
- Filtre <24h
- Auto-refresh toutes les 5 minutes

### 2. Pages et affichage

#### /en-direct (InLiveMain.vue)
- Affiche articles + vidéos < 24h
- Overlay play icon sur les vidéos
- Refresh auto : 5 minutes

#### /articles (ArticlesMain.vue)
- Affiche tous les articles
- Recherche par titre/summary/source
- Refresh auto : 5 minutes

#### /video (VideoMain.vue)
- Affiche toutes les vidéos
- Filtres par channel
- Overlay play icon
- Refresh auto : 5 minutes

## Planification Backend (Back/scraping/api.py)

### Scheduler APScheduler

1. **Warmup** (au démarrage)
   - Scrape articles 24h
   - Scrape vidéos 24h (illimité)
   - Archive automatiquement

2. **Refresh automatique** : toutes les 15 minutes
   - `_refresh_all()` → articles + videos
   - Cache en mémoire (15 min TTL)

### Endpoints Flask

- `GET /articles` : Articles avec cache
- `GET /videos` : Vidéos avec cache
- `GET /archive` : Archive complète (pas de cache)
- `GET /stats` : Statistiques
- `POST /admin/refresh` : Force un refresh manuel

## Scripts utilitaires

### Back/scraping_all/api.py
Scraping batch sur N jours (défaut : 7)
```bash
python -m scraping_all.api
```

### Back/test_complete_workflow.py
Test complet du workflow
```bash
python Back/test_complete_workflow.py
```

### Back/test_video_scraping.py
Test rapide scraping vidéos
```bash
python Back/test_video_scraping.py
```

## Résumé du flux de données

```
┌─────────────────────────────────────────────┐
│  BACKEND (Flask + APScheduler)              │
│                                             │
│  scraping/core.py    ──┐                   │
│    ↓ RSS feeds         │                   │
│    ↓ Filtre keywords   │                   │
│    ↓ add_articles()    ├─→ archive.py      │
│                        │     ↓              │
│  scraping/video_api.py─┘     ↓              │
│    ↓ YouTube API            ↓              │
│    ↓ Per-channel           ↓              │
│    ↓ add_videos()          ↓              │
│                            ↓              │
│                     Front/public/         │
│                     archive.json          │
│                            ↑              │
└────────────────────────────┼──────────────┘
                             │
┌────────────────────────────┼──────────────┐
│  FRONTEND (Nuxt 4)         │              │
│                            │              │
│  useArticles ──────────────┤              │
│  useVideos ────────────────┼─→ fetch()    │
│  useArchiveFeed ───────────┘   /archive.json
│                                             │
│  Pages:                                    │
│    /en-direct  (articles + videos <24h)    │
│    /articles   (tous les articles)         │
│    /video      (toutes les vidéos)         │
│                                             │
│  Auto-refresh : 5 minutes                  │
└─────────────────────────────────────────────┘
```

## Points clés de la synchronisation

✅ **Un seul fichier** : `Front/public/archive.json`
✅ **Backend écrit directement** dans le public du frontend
✅ **Frontend lit via HTTP** : `/archive.json`
✅ **Pas de copie/sync** nécessaire
✅ **Add-only** : l'archive grandit, ne se vide jamais
✅ **Déduplication** : par lien (articles et vidéos)
✅ **Thread-safe** : lock pour les écritures concurrentes
✅ **Auto-refresh frontend** : 5 minutes sur toutes les pages
✅ **Auto-refresh backend** : 15 minutes via APScheduler

## Statistiques actuelles (exemple)

```
Articles: 111
Vidéos: 265
Channels: 22 (ARTE, Le Monde, BBC News, CNN, Reuters, etc.)
```

## Commandes de test

```bash
# Test workflow complet
cd Back && python test_complete_workflow.py

# Scraping batch 7 jours
cd Back && python -m scraping_all.api

# Lancer le backend Flask
cd Back && python -m scraping.api

# Lancer le frontend Nuxt
cd Front && npm run dev
```
