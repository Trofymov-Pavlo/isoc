# Règles de structuration du projet (Nuxt + Vue)

Ces règles visent à aligner le projet sur des standards professionnels Nuxt 3/4.

## Arborescence
- `Front/` : application Nuxt (pages, components, layouts, assets, plugins, public, types, composables, nuxt.config.ts).
- `Back/` : scripts et utilitaires backend (scraping, helpers). Pas de code Nuxt ici.
- `public/` (dans Front) : fichiers statiques servis tels quels (`robots.txt`, `rss.xml`).
- `pages/` : routes. Chaque fichier page ne doit rendre qu’un seul composant principal.
- `components/` : UI réutilisable, groupée par domaine. Chaque dossier a un composant `mainX.vue` orchestrateur.
- `layouts/` : templates globaux (ex. `default.vue`).
- `assets/` : styles SASS/CSS et médias importés au build.
- `plugins/` : initialisation de librairies (ex. `vuetify.ts`).
- `composables/` : utilitaires réactifs (`useX.ts`).

## Conventions pages → components
- Dans `Front/pages/*`, le contenu est minimal et **rend uniquement** son composant principal correspondant, ex. `pages/video.vue` rend `<MainVideo />` depuis `components/video/mainVideo.vue`.
- Importer via alias `~/components/...`.
- Nom du composant principal : `MainX` dans code, fichier `mainX.vue`.

## Nommage et structure
- Dossiers `components/` en `camelCase` s’ils contiennent des mots composés (ex. `aPropos`, `inLive`).
- Pages nommées selon la route attendue (`pages/connexion.vue`, `pages/support.vue`).
- Éviter les espaces et majuscules dans chemins (gardez conventions Nuxt).

## Liens et navigation
- Les liens de l’en-tête et du pied de page doivent pointer vers des routes existantes sous `pages/`.
- Les liens statiques (RSS, robots) sont sous `/rss.xml` et `/robots.txt` via `Front/public/`.
- Utiliser `NuxtLink` pour les routes internes.

## Nuxt et TypeScript
- Fichiers Vue en `<script setup lang="ts">` lorsque possible.
- Types partagés sous `Front/types/`.
- Configurer les plugins dans `Front/plugins/` et référencés par `nuxt.config.ts`.

## Backend
- `Back/` ne doit pas contenir de serveur web Nuxt; réserver aux scripts (scraping, DB helpers).
- Communication API : à définir (Nitro server/route ou API externe). Actuellement, pas de couplage direct.

## Qualité et branches
- Chaque fonctionnalité sur une branche dédiée depuis `develop`. Merge puis suppression de la branche.
- Pages ne contiennent pas de logique complexe; déplacer l’UI dans `components/`.

## Tests rapides
- `npm run dev` depuis `Front/` pour vérifier le rendu.
- Vérifier les routes : `/`, `/video`, `/inLivePage`, `/podcast`, `/Contact`, `/connexion`, `/signup`, `/liked`, `/archive`, `/rss`, `/aPropos`, `/support`.
