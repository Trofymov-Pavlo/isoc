# AXIOME - Frontend

Frontend Nuxt 4 + Vue 3 + Vuetify pour le média indépendant AXIOME dédié au conflit Ukraine-Russie.

## Structure

```
Front/
├── components/        # Composants Vue réutilisables
│   ├── header/       # En-tête et navigation
│   ├── footer/       # Pied de page
│   ├── HomePage/     # Sections de la page d'accueil
│   └── inLive/       # Composants actualités en direct
├── pages/            # Pages Nuxt (routage automatique)
├── layouts/          # Layouts Nuxt
├── composables/      # Composables Vue (logique réutilisable)
├── plugins/          # Plugins Vue (Vuetify)
├── assets/           # Styles SCSS et ressources
├── public/           # Fichiers statiques
├── types/            # Types TypeScript
├── app.vue           # Root component
├── nuxt.config.ts    # Configuration Nuxt
├── tsconfig.json     # Configuration TypeScript
└── package.json      # Dépendances npm
```

## Installation

### 1. Installer les dépendances

```bash
npm install
```

### 2. Lancer le serveur de développement

```bash
npm run dev
```

Le site sera disponible sur `http://localhost:3000`

### 3. Build pour la production

```bash
npm run build
```

### 4. Prévisualiser la build

```bash
npm run preview
```

## Configuration

### API Backend

L'application se connecte à l'API backend Flask sur `http://127.0.0.1:5000`

La configuration est dans [composables/useArticles.ts](composables/useArticles.ts):
```typescript
const apiBase = opts?.apiBase ?? "http://127.0.0.1:5000";
```

## Pages principales

- **/** - Accueil (page d'accueil principale)
- **/inLivePage** - Actualités en direct
- **/Contact** - Page de contact

## Sections de la page d'accueil

- **HeroSection** - En-tête avec présentation AXIOME
- **AlertBar** - Barre alertes actualités en direct
- **FeaturedArticle** - Article principal par Antoine TENA
- **HighlightedArticles** - Articles à la une (scraping)
- **PodcastSection** - Podcast AXIOME (TENA, BARRACHIN, TROFYMOV)
- **LiveUpdates** - Actualités en temps réel
- **VideoSection** - Vidéos d'analyse (scraping)
- **NewsletterSection** - Inscription newsletter

## Styles

- Framework CSS: **Vuetify 3**
- Préprocesseur: **SCSS**
- Palette: Violet/Pourpre (#2f0538, #4b2faa) et rouge (#ff6b6b)

## Composables

- **useArticles()** - Gestion des articles depuis l'API backend

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
