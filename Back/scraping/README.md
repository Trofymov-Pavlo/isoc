# Module de Scraping

Module unifié de scraping pour AXIOME - Média indépendant du conflit Ukraine-Russie.

## 🎯 Fonctionnalités

- Scraping d'articles RSS depuis plusieurs sources françaises
- Scraping de vidéos YouTube depuis des chaînes sélectionnées
- Filtrage automatique par mots-clés liés au conflit Ukraine-Russie
- Ajout automatique à l'archive JSON (avec dédoublonnage)
- Support de fenêtres temporelles personnalisables

## 📦 Structure

```
scraping/
├── api.py              # Script CLI principal
├── archive.py          # Gestion de la persistence (archive.json partagée)
├── __init__.py         # Module principal
├── requirements.txt    # Dépendances Python
│
├── articles/           # 📰 Module complet de scraping RSS
│   ├── __init__.py
│   ├── core.py         # Logique de scraping RSS
│   ├── feeds.py        # Configuration des flux RSS (112 sources)
│   ├── filters.py      # Filtrage des articles
│   ├── keywords.py     # Mots-clés de filtrage
│   ├── textops.py      # Opérations sur le texte
│   ├── media_extract.py # Extraction des métadonnées
│   └── http_state.py   # Gestion des sessions HTTP + cache .rss_multi_fr_state.json
│
└── videos/             # 🎥 Module complet de scraping YouTube
    ├── __init__.py
    ├── core.py         # Interface de scraping vidéo
    ├── scraper.py      # Implémentation YouTube Data API v3
    ├── feeds.py        # Configuration des chaînes (36 chaînes)
    ├── keywords.py     # Mots-clés de filtrage
    ├── config.py       # Configuration (charge clé API depuis yt_api_key.txt)
    └── yt_api_key.txt  # Clé YouTube Data API v3 (git-ignored)
```

**Principe** : Chaque module (articles/, videos/) est autonome avec ses propres dépendances.
Seul `archive.py` est partagé pour la persistence commune.

## 🚀 Usage

### Scraping par défaut (dernières 24h)

```bash
cd Back
python -m scraping.api
```

### Scraping avec fenêtre temporelle personnalisée

```bash
# Scraper les dernières 48 heures
python -m scraping.api --hours 48

# Scraper les 7 derniers jours
python -m scraping.api --days 7

# Scraper les 3 derniers jours (équivalent à 72 heures)
python -m scraping.api --days 3
```

### Afficher l'aide

```bash
python -m scraping.api --help
```

## 📝 Comportement

1. **Filtrage optimisé** : Les filtres (temps + mots-clés) sont appliqués AVANT l'archivage pour éviter les opérations inutiles
2. **Dédoublonnage automatique** : Le module vérifie les liens existants dans `archive.json` avant d'ajouter de nouvelles entrées
3. **Ajout, pas remplacement** : Les nouveaux articles/vidéos sont ajoutés à l'archive existante (pas d'écrasement)
4. **Tri chronologique** : L'archive est automatiquement triée par date de publication (plus récent en premier)
5. **Timestamps** : Chaque entrée ajoutée reçoit un timestamp `archived_at` avec la date d'archivage

## 📍 Emplacement de l'archive

L'archive est stockée dans : `Front/public/archive.json`

Cela permet au frontend Nuxt d'accéder directement au fichier statique.

## ⚙️ Configuration

### Flux et mots-clés
- **Flux RSS** : configurés dans [articles/feeds.py](articles/feeds.py) (71 sources)
- **Chaînes YouTube** : configurées dans [videos/feeds.py](videos/feeds.py) (25 chaînes)
- **Mots-clés** : définis dans [articles/keywords.py](articles/keywords.py) et [videos/keywords.py](videos/keywords.py)

### Clé API YouTube
La clé YouTube Data API v3 est stockée dans `videos/yt_api_key.txt` (fichier git-ignoré).
Si ce fichier n'existe pas, la variable d'environnement `YT_API_KEY` est utilisée comme fallback.

### Cache HTTP
Le fichier `.rss_multi_fr_state.json` (à la racine de Back/) stocke les en-têtes ETag et Last-Modified pour optimiser les requêtes RSS (évite de retélécharger les flux non modifiés).

## 🔧 Dépendances

Voir [requirements.txt](requirements.txt) pour la liste complète des dépendances Python.

Principales librairies :
- `feedparser` : Parsing des flux RSS
- `requests` : Requêtes HTTP
- `beautifulsoup4` : Parsing HTML
- `pytube` : Interactions avec YouTube

## 🐛 Debugging

En cas d'erreur :
1. Vérifier que l'environnement virtuel est activé
2. Vérifier que toutes les dépendances sont installées : `pip install -r requirements.txt`
3. Vérifier que le fichier `Front/public/archive.json` existe et est accessible en écriture
4. Consulter les logs d'exécution pour identifier la source du problème
