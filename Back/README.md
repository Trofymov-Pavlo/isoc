# AXIOME - Backend

Backend Flask + Scraping RSS pour le média indépendant AXIOME dédié au conflit Ukraine-Russie.

## Structure

```
Back/
├── scraping/           # Module de scraping RSS
│   ├── __init__.py
│   ├── api.py         # API Flask avec endpoints
│   ├── core.py        # Logique de parsing RSS
│   ├── feeds.py       # Listes de flux RSS français
│   ├── filters.py     # Filtrage des articles
│   ├── keywords.py    # Mots-clés de filtrage
│   ├── media_extract.py
│   ├── textops.py
│   ├── http_state.py
│   └── scraping.py
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
- ✅ Filtrage par mots-clés Ukraine, Russie, NATO
- ✅ Cache 15 minutes des résultats
- ✅ Extraction d'images et auteurs
- ✅ Support CORS pour connexion au frontend
- ✅ Planification automatique du scraping

## Configuration

Les flux RSS sont définis dans `scraping/feeds.py` avec les meilleures sources françaises:
- Le Monde, Figaro, Franceinfo
- RFI, France 24
- La Croix, Libération
- Et 40+ autres sources
