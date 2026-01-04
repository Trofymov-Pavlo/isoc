# AXIOME · Information & Analyse

Plateforme d'agrégation multi-sources sur le conflit Ukraine-Russie.
**Projet étudiant ISOC531 · 2025-2026**

Architecture full-stack : **Backend Django** (Auth + Scraping) + **Frontend Nuxt 4**

## 📁 Structure du projet

```
isoc/
├── Back/                  # Backend Django REST Framework
│   ├── accounts/         # Authentification JWT (users, tokens)
│   ├── django_config/    # Configuration Django (settings, urls)
│   ├── saved_media/      # Gestion favoris utilisateurs
│   ├── scraping/         # Module scraping RSS (articles, vidéos)
│   ├── db.sqlite3        # Base de données SQLite
│   ├── manage.py         # Django CLI
│   └── requirements.txt
├── Front/                 # Frontend Nuxt 4 + Vue 3 + Vuetify 3
│   ├── components/       # Composants Vue (auto-import)
│   ├── pages/            # Pages (routage automatique)
│   ├── composables/      # Logique réutilisable (useAuthAPI, useSavedMedia)
│   ├── plugins/          # Plugins Vue (Vuetify)
│   ├── assets/           # Styles SCSS
│   ├── public/           # Fichiers statiques (RSS, robots.txt, sitemap.xml)
│   ├── package.json
│   └── README.md
└── README.md              # Ce fichier
```

## 🚀 Démarrage rapide

### Backend Django (Terminal 1)

**Windows :**
```bash
cd Back
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8000
```

**macOS / Linux :**
```bash
cd Back
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8000
```

✅ API disponible sur `http://localhost:8000`

### Frontend Nuxt (Terminal 2)

**Windows :**
```bash
cd Front
npm install
npm run dev
```

**macOS / Linux :**
```bash
cd Front
npm install
npm run dev
```

✅ Site disponible sur `http://localhost:3000`

## 📋 Prérequis

- **Python 3.8+** (pour le backend)
- **Node.js 16+** (pour le frontend)
- **npm** ou **yarn**

## 🎯 Features

### Backend (Django REST Framework)
- ✅ Authentification JWT (inscription, connexion, refresh)
- ✅ Scraping automatique 30+ sources RSS francophones
- ✅ Filtrage multi-critères (mots-clés, sources, dates)
- ✅ Gestion favoris utilisateurs (SavedMedia)
- ✅ Archive JSON persistante (247k+ articles)
- ✅ API REST avec CORS configuré
- ✅ Rate limiting et throttling

### Frontend (Nuxt 4 + Vue 3 + Vuetify 3)
- ✅ Pages : Accueil, En Direct, Explorer, Mes Favoris
- ✅ Authentification complète avec JWT
- ✅ Système de favoris avec like/unlike
- ✅ Pages légales complètes (CGU, Mentions, Cookies)
- ✅ Standards du web (RSS, sitemap.xml, robots.txt, humans.txt, security.txt)
- ✅ Design moderne responsive
- ✅ Hero sections avec gradients

## 👥 Équipe ISOC531

- **Chef de projet & Développeur** : Antoine TENA (architecture, dev full-stack, article désinformation)
- **Analyste juridique** : Nathan BARRACHIN (article enjeux juridiques)
- **Analyste militaire & Designer** : Hiba EL HAYANI (article technologies militaires, UI/UX)
- **Contributeur** : Pavel TROFYMOV (recherche)
- **Présentation** : Co-rédigée par toute l'équipe

## 🔗 Configuration Backend-Frontend

L'URL de l'API est configurée dans `Front/nuxt.config.ts` :

```typescript
apiBase: process.env.NUXT_PUBLIC_API_BASE || 'http://localhost:8000/api/accounts'
```

## 📊 Sources d'information

Le backend agrège 30+ sources francophones :
- **Généralistes** : Le Monde, Le Figaro, Libération, L'Express
- **Internationaux** : RFI, France 24, TV5 Monde
- **Régionaux** : Sud Ouest, La Dépêche, Ouest-France
- **Anglophones** : Kyiv Post, BBC, Reuters

Voir `Back/scraping/articles/feeds.py` pour la liste complète.

## 🔧 Dépannage

### L'API ne répond pas ?

**Windows :**
```bash
curl http://localhost:8000/api/accounts/health
```

**macOS / Linux :**
```bash
curl http://localhost:8000/api/accounts/health
```

### Les articles ne s'affichent pas ?
1. Vérifier que le backend Django tourne sur le port 8000
2. Vérifier la console navigateur pour erreurs CORS
3. Vérifier `archive.json` existe dans `Front/public/`

### Erreur d'authentification ?
1. Vérifier que `db.sqlite3` existe et est migré
2. Tester avec `python manage.py createsuperuser`
3. Vérifier les tokens JWT dans localStorage

## 📚 Documentation

- [Backend - README.md](Back/README.md)
- [Frontend - README.md](Front/README.md)
- [Auth System - AUTH_SYSTEM.md](Back/accounts/AUTH_SYSTEM.md)

## 🌐 Standards du web

Le projet respecte les standards du web :
- **RSS 2.0** : `/rss.xml` - Flux RSS professionnel
- **Sitemap** : `/sitemap.xml` - Plan du site XML
- **Robots.txt** : `/robots.txt` - Directives pour robots
- **Humans.txt** : `/humans.txt` - Équipe et stack technique
- **Security.txt** : `/.well-known/security.txt` - Contact sécurité (RFC 9116)
- **Ads.txt** : `/ads.txt` - Pas de publicité (projet académique)

## 🎨 Design

**Palette de couleurs :**
- Violet foncé : `#2f0538`
- Violet clair : `#4b2faa`
- Gris : `#f3f4f6`

**Typographie :**
- Titres : 32-48px, font-weight 600-800
- Hero sections avec gradients subtils

## 📄 License

© 2025-2026 AXIOME · Projet étudiant ISOC531
Tous droits réservés - Usage académique uniquement