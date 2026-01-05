# AXIOME · Backend

Backend Django REST Framework pour la plateforme AXIOME.
**Projet étudiant ISOC531 · 2025-2026**

## Structure

```
Back/
├── accounts/              # App Django authentification
│   ├── models.py         # User model
│   ├── serializers.py    # Serializers DRF
│   ├── views.py          # API endpoints (login, register, refresh)
│   ├── urls.py           # Routes API
│   ├── throttles.py      # Rate limiting
│   └── AUTH_SYSTEM.md    # Documentation auth complète
├── django_config/         # Configuration Django
│   ├── settings.py       # Settings (CORS, JWT, DB)
│   ├── urls.py           # Routes principales
│   └── wsgi.py
├── saved_media/           # App Django favoris utilisateurs
│   ├── models.py         # SavedMedia, UserCategory
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── scraping/              # Module de scraping
│   ├── api.py            # Endpoints scraping
│   ├── archive.py        # Gestion archive.json
│   ├── articles/         # Scraping articles RSS
│   │   ├── core.py
│   │   ├── feeds.py      # 30+ sources RSS
│   │   └── filters.py
│   └── videos/           # Scraping vidéos YouTube
├── db.sqlite3             # Base de données SQLite
├── manage.py              # Django CLI
└── requirements.txt       # Dépendances Python
```

## Installation

### 1. Créer l'environnement virtuel

**Windows :**
```bash
cd Back
python -m venv venv
```

**macOS / Linux :**
```bash
cd Back
python3 -m venv venv
```

### 2. Activer l'environnement virtuel

**Windows :**
```bash
venv\Scripts\activate
```

**macOS / Linux :**
```bash
source venv/bin/activate
```

### 3. Installer les dépendances

**Windows :**
```bash
pip install -r requirements.txt
```

**macOS / Linux :**
```bash
pip install -r requirements.txt
```

### 4. Migrer la base de données

**Windows :**
```bash
python manage.py migrate
```

**macOS / Linux :**
```bash
python manage.py migrate
```

## Démarrage

### Lancer le serveur Django (port 8000)

**Windows :**
```bash
python manage.py runserver 8000
```

**macOS / Linux :**
```bash
python manage.py runserver 8000
```

✅ API disponible sur `http://localhost:8000`

### Endpoints disponibles

#### Authentification (`/api/accounts/`)

- **POST `/register`** - Inscription utilisateur
- **POST `/login`** - Connexion (retourne access + refresh tokens)
- **POST `/refresh`** - Rafraîchir access token
- **POST `/logout`** - Déconnexion
- **GET `/me`** - Informations utilisateur connecté

#### Favoris (`/api/saved-media/`)

- **GET `/saved-items`** - Liste des favoris
- **POST `/save-item`** - Ajouter aux favoris
- **DELETE `/unsave-item/<id>`** - Retirer des favoris
- **GET `/categories`** - Catégories personnalisées

#### Scraping (`/scraping/`)

- **GET `/api/articles`** - Articles agrégés
- **GET `/api/videos`** - Vidéos agrégées

Exemples :

**Windows :**
```bash
curl http://localhost:8000/api/accounts/me -H "Authorization: Bearer <token>"
```

**macOS / Linux :**
```bash
curl http://localhost:8000/api/accounts/me -H "Authorization: Bearer <token>"
```

## 🎯 Features

**Backend (Django REST Framework)**
- ✅ Authentification JWT (inscription, connexion, refresh)
- ✅ Scraping 71 flux RSS + 25 chaînes YouTube
- ✅ Filtrage multi-critères (mots-clés, sources, dates)
- ✅ Gestion favoris utilisateurs (SavedMedia)
- ✅ Archive JSON persistante (247k+ articles)
- ✅ API REST avec CORS configuré
- ✅ Rate limiting et throttling
- ✅ Sauvegarde articles/vidéos
- ✅ Catégories personnalisées
- ✅ Gestion complète (add, remove, list)
- ✅ Synchronisation avec frontend

### Scraping
- ✅ 71 flux RSS articles francophones
- ✅ 25 chaînes YouTube
- ✅ Archive JSON 247k+ articles
- ✅ Filtrage multi-critères
- ✅ Extraction images et métadonnées
- ✅ Détection doublons
- ✅ Thread-safe operations

### API
- ✅ Django REST Framework
- ✅ CORS configuré pour localhost:3000
- ✅ Documentation intégrée
- ✅ Throttling et rate limiting

## Configuration

### Sources RSS

Les flux RSS sont définis dans `scraping/articles/feeds.py` :
- **Généralistes** : Le Monde, Le Figaro, Libération, L'Express
- **Internationaux** : RFI, France 24, BBC
- **Spécialisés OSINT** : Bellingcat, Oryx, Meduza
- **Sources ukrainiennes** : Kyiv Post, UNIAN
- Et 60+ autres sources

**Total : 71 flux RSS articles**

### Chaînes YouTube
Les chaînes YouTube pour vidéos sont dans `scraping/videos/feeds.py` :
- **Français**: ARTE, Le Monde, France 24, BFM TV, Mediapart, Brut
- **International**: BBC News, DW News, Euronews, CNN, Reuters, Al Jazeera
- **Military**: Warthog Defense, Defense Updates
- **Documentary**: National Geographic, Discovery Channel

**Total : 25 chaînes YouTube**

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
