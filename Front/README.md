# AXIOME · Frontend

Frontend Nuxt 4 + Vue 3 + Vuetify 3 pour la plateforme d'agrégation AXIOME.
**Projet étudiant ISOC531 · 2025-2026**

## Structure

```
Front/
├── components/           # Composants Vue réutilisables
│   ├── a-propos/        # Page À propos
│   ├── articles/        # Composants articles
│   ├── compte/          # Page Mon compte
│   ├── contact/         # Page Contact
│   ├── explorer/        # Page Explorer
│   ├── footer/          # Footer avec liens standards
│   ├── header/          # Header et navigation
│   ├── home/            # Sections page d'accueil
│   ├── in-live/         # Actualités en direct
│   ├── liked/           # Page Mes favoris
│   ├── shared/          # Composants partagés
│   └── video/           # Composants vidéos
├── pages/               # Pages Nuxt (routage auto)
├── composables/         # Logique réutilisable
│   ├── useAuthAPI.ts   # API authentification
│   ├── useAuthState.ts # État authentification
│   ├── useSavedMedia.ts # Gestion favoris
│   └── ...
├── plugins/             # Plugins (Vuetify)
├── assets/styles/       # Styles SCSS globaux
├── public/              # Fichiers statiques
│   ├── rss.xml         # Flux RSS
│   ├── sitemap.xml     # Plan du site
│   ├── robots.txt      # Directives robots
│   ├── humans.txt      # Équipe projet
│   ├── ads.txt         # Pas de publicité
│   ├── archive.json    # Archive articles (247k+)
│   └── .well-known/
│       └── security.txt
├── app.vue              # Root component
├── nuxt.config.ts       # Configuration Nuxt
└── package.json         # Dépendances
```

## Installation

### 1. Installer les dépendances

**Windows :**
```bash
cd Front
npm install
```

**macOS / Linux :**
```bash
cd Front
npm install
```

### 2. Lancer le serveur de développement

**Windows :**
```bash
npm run dev
```

**macOS / Linux :**
```bash
npm run dev
```

✅ Site disponible sur `http://localhost:3000`

### 3. Build pour la production

**Windows :**
```bash
npm run build
npm run preview
```

**macOS / Linux :**
```bash
npm run build
npm run preview
```

## Configuration

### API Backend

L'application se connecte à l'API Django REST sur `http://localhost:8000`

Configuration dans [nuxt.config.ts](nuxt.config.ts) :
```typescript
runtimeConfig: {
  public: {
    apiBase: process.env.NUXT_PUBLIC_API_BASE || 'http://localhost:8000/api/accounts',
    apiScraper: process.env.NUXT_PUBLIC_SCRAPER_BASE || 'http://localhost:8000',
  }
}
```

## Pages principales

- **/** - Accueil (hero + sections principales)
- **/en-direct** - Actualités en temps réel
- **/explorer** - Recherche et filtrage avancé
- **/liked** - Mes favoris (authentification requise)
- **/mon-compte** - Gestion du compte utilisateur
- **/contact** - Formulaire de contact
- **/a-propos** - Mission, méthodologie, équipe
- **/connexion** - Authentification
- **/signup** - Inscription
- **/forgot-password** - Réinitialisation du mot de passe
- **/conditions** - Conditions générales d'utilisation
- **/mentions** - Mentions légales
- **/cookies** - Politique cookies

## Sections de la page d'accueil

- **HeroMain** - Hero avec slogan AXIOME
- **LiveArticlesSection** - Actualités en direct
- **ExplorerSection** - Accès à l'exploration
- **AboutSection** - À propos rapide
- **ContactSection** - Formulaire de contact

## Styles

- Framework CSS : **Vuetify 3**
- Préprocesseur : **SCSS**
- Palette de couleurs :
  - Violet foncé : `#2f0538`
  - Violet clair : `#4b2faa`
  - Gris : `#f3f4f6`, `#e5e5e5`
- Typographie : 32-48px titres, font-weight 600-800
- Design : Hero avec gradients, bordures subtiles

## Composables

- **useAuthAPI()** - API authentification (login, register, refresh)
- **useAuthState()** - État authentification (isAuthenticated, user)
- **useSavedMedia()** - Gestion favoris (like, unlike, getSavedItems)
- **useArticles()** - Récupération articles depuis archive.json
- **useVideos()** - Récupération vidéos
- **useArchiveFeed()** - Chargement archive JSON
- **useSearchBar()** - Gestion recherche
- **usePagination()** - Pagination des résultats
- **useTheme()** - Gestion thème Vuetify
- **useRateLimit()** - Gestion rate limiting

## Installation des dépendances

```json
{
  "dependencies": {
    "vue": "^3.5.22",
    "nuxt": "^4.1.3",
    "vuetify": "^3.10.5",
    "vue-router": "^4.5.1",
    "@mdi/font": "^7.4.47",
    "vite-plugin-vuetify": "^2.1.2",
    "sass": "^1.93.2"
  }
}
```

## Important

**L'API backend (Back/) doit être en cours d'exécution pour que le site fonctionne correctement !**

Consultez [../Back/README.md](../Back/README.md) pour les instructions de démarrage du backend.
