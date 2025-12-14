# AXIOME - Média indépendant du conflit Ukraine-Russie

Architecture réstructurée avec **Backend** (Flask/Scraping) et **Frontend** (Nuxt/Vue).

## 📁 Structure du projet

```
ISOC/
├── Back/              # Backend Flask + Scraping RSS
│   ├── scraping/      # Module de scraping (RSS, parsing, filtrage)
│   ├── venv/          # Environnement Python virtuel
│   ├── requirements.txt
│   └── README.md
├── Front/             # Frontend Nuxt + Vue + Vuetify
│   ├── components/    # Composants Vue
│   ├── pages/         # Pages (routage auto)
│   ├── composables/   # Logique réutilisable
│   ├── plugins/       # Plugins Vue (Vuetify)
│   ├── assets/        # Styles SCSS
│   ├── public/        # Fichiers statiques
│   ├── node_modules/  # Dépendances npm
│   ├── package.json
│   └── README.md
└── README.md          # Ce fichier
```

## 🚀 Démarrage rapide

### Backend (Terminal 1)

```bash
cd Back
source venv/Scripts/activate    # Windows
pip install -r requirements.txt # Si première fois
python -m scraping.api
```

L'API sera disponible sur `http://127.0.0.1:5000`

### Frontend (Terminal 2)

```bash
cd Front
npm install                     # Si première fois
npm run dev
```

Le site sera disponible sur `http://localhost:3000`

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