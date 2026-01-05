# AXIOME - Guide d'installation rapide

## 📥 Cloner le projet

```bash
git clone https://github.com/Trofymov-Pavlo/isoc.git
cd isoc
```

## 📋 Installation manuelle

### 1. Backend Django (Terminal 1)

```bash
cd Back
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8000
```

### 2. Frontend Nuxt (Terminal 2)

```bash
cd Front
npm install
npm run dev
```

## 🌐 Accès

- **Frontend** : http://localhost:3000
- **Backend API** : http://localhost:8000

## 🔄 Scraping des articles

```bash
cd Back
venv\Scripts\activate

# Scraper les dernières 24h (par défaut)
python -m scraping.api

# Scraper les N dernières heures
python -m scraping.api --hours 48

# Scraper les N derniers jours
python -m scraping.api --days 7
```

Les articles sont ajoutés à `Front/public/archive.json`

## 🚀 Lancement rapide (Windows)

```bash
./start-win.sh
```

Ce script lance automatiquement le backend et le frontend.

## 📚 Documentation complète

Voir [README.md](README.md) pour la documentation détaillée.
