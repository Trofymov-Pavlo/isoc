# AXIOME - Média indépendant du conflit Ukraine-Russie

Architecture réstructurée avec **Backend** (Django Auth + Flask/Scraping) et **Frontend** (Nuxt 4 + Vue 3 + Vuetify).

## 📁 Structure du projet

```
ISOC/
├── Back/              # Backend Django (Auth) + Flask (Scraping)
│   ├── accounts/      # App Django pour authentification (users, JWT, tokens)
│   ├── isoc_auth/     # Config Django (settings, urls, wsgi)
│   ├── scraping/      # Module Flask de scraping (RSS, parsing, filtrage)
│   ├── venv/          # Environnement Python virtuel
│   ├── manage.py      # Django CLI
│   ├── requirements.txt
│   └── README.md
├── Front/             # Frontend Nuxt 4 + Vue 3 + Vuetify 3
│   ├── components/    # Composants Vue (auto-import)
│   ├── pages/         # Pages (routage auto)
│   ├── composables/   # Logique réutilisable (useAuthAPI, useAuthState)
│   ├── plugins/       # Plugins Vue (Vuetify, JWT)
│   ├── assets/        # Styles SCSS
│   ├── public/        # Fichiers statiques
│   ├── node_modules/  # Dépendances npm
│   ├── package.json
│   └── README.md
├── AUTH_SYSTEM.md     # Documentation complète d'authentification
├── start-auth-system.sh  # Script de démarrage
└── README.md          # Ce fichier
```

## 🚀 Démarrage rapide

### Tous les services (Bash/Git Bash)

```bash
chmod +x start-auth-system.sh
./start-auth-system.sh
```

### Ou manuellement :

#### Backend Django (Terminal 1)

```bash
cd Back
source venv/Scripts/activate    # Windows (Git Bash) ou venv\Scripts\activate (CMD)
pip install -r requirements.txt # Si première fois
python manage.py runserver 8000
```

API disponible sur `http://127.0.0.1:8000`

#### Frontend Nuxt (Terminal 2)

```bash
cd Front
npm install                     # Si première fois
npm run dev
```

Site disponible sur `http://localhost:3000`

## 📋 Prérequis

- **Python 3.8+** (pour le backend)
- **Node.js 16+** (pour le frontend)
- **npm** ou **yarn**

## 🎯 Features

### Backend
- ✅ Scraping de 50+ flux RSS français
- ✅ Filtrage par mots-clés (Ukraine, Russie, NATO)
- ✅ Cache 15 minutes des articles
- ✅ Extraction d'images et auteurs
- ✅ API REST avec CORS
- ✅ Planification automatique du scraping

### Frontend
- ✅ Page d'accueil dynamique
- ✅ Actualités en direct
- ✅ Articles à la une (scraping)
- ✅ Podcast AXIOME original
- ✅ Vidéos d'analyse
- ✅ Newsletter
- ✅ Design responsive
- ✅ Animations fluides

## 👥 Équipe éditoriale

- **Article principal**: Antoine TENA
- **Podcast**: Antoine TENA, Nathan BARRACHIN, Pavel TROFYMOV
- **Scraping/Source**: Médias français (50+ sources)

## 🔗 Connexion Backend-Frontend

L'URL de l'API est configurée dans `Front/composables/useArticles.ts`:

```typescript
const apiBase = opts?.apiBase ?? "http://127.0.0.1:5000";
```

## 📊 Flux RSS sources

Le backend récupère les articles depuis 50+ sources françaises:
- **Généralistes**: Le Monde, Figaro, Franceinfo, Libération
- **Internationaux**: RFI, France 24
- **Régionaux**: Ouest-France, Le Parisien, Sud Ouest
- **Spécialisés**: La Croix, Challenges, Les Échos
- Et bien d'autres...

Voir `Back/scraping/feeds.py` pour la liste complète.

## 📝 Commits et versioning

- Branch principale: `develop`
- Features en développement: `feature/*`

### Dernier merge
- Branche `feature/config` merge de `develop`
- Restructuration Back/Front avec Nuxt et Flask

## 🔧 Dépannage

### L'API ne répond pas?
```bash
# Vérifier que le backend est lancé
curl http://127.0.0.1:5000/articles?q=ukraine
```

### Les articles ne s'affichent pas?
1. Vérifier que le backend est en cours d'exécution
2. Vérifier la console du navigateur pour les erreurs CORS
3. Vérifier que l'URL API est correcte dans `useArticles.ts`

### Les styles Vuetify ne fonctionnent pas?
```bash
cd Front
npm install
npm run dev
```

## 📚 Documentation

- [Backend - README.md](Back/README.md)
- [Frontend - README.md](Front/README.md)

## 📄 License

Propriétaire - ISOC Media AXIOME 2025





# #2f0538