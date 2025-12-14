#!/bin/bash
# Script de démarrage complet ISOC Auth System

echo "╔══════════════════════════════════════════════════════════╗"
echo "║        ISOC Authentication System - Startup Script       ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# Vérifier si on est à la racine du projet
if [ ! -d "Back" ] || [ ! -d "Front" ]; then
  echo "❌ Erreur: Exécutez ce script depuis la racine du projet ISOC"
  exit 1
fi

# ============ BACKEND ============
echo "📦 Backend Django..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ ! -d "Back/venv" ]; then
  echo "Création de l'environnement virtuel..."
  cd Back
  python -m venv venv
  if [ $? -eq 0 ]; then
    echo "✅ venv créé"
  else
    echo "❌ Erreur venv"
    exit 1
  fi
else
  echo "✅ venv existe"
fi

# Activation de venv
if [ -f "Back/venv/Scripts/activate" ]; then
  # Windows (Git Bash)
  source Back/venv/Scripts/activate
elif [ -f "Back/venv/bin/activate" ]; then
  # macOS/Linux
  source Back/venv/bin/activate
fi

# Installer les dépendances
echo "Installation des dépendances Django..."
pip install -r Back/requirements.txt -q
if [ $? -eq 0 ]; then
  echo "✅ Dépendances Django installées"
else
  echo "⚠️  Erreur lors de l'installation des dépendances"
fi

# Migrations
echo "Applying migrations..."
cd Back
python manage.py migrate -q 2>/dev/null
if [ $? -eq 0 ]; then
  echo "✅ Migrations appliquées"
else
  echo "⚠️  Migrations déjà appliquées (ou erreur mineur)"
fi

echo ""
echo "🚀 Démarrage du serveur Django sur http://127.0.0.1:8000"
echo "   (Appuyez sur Ctrl+C pour arrêter)"
echo ""
python manage.py runserver 8000 &
DJANGO_PID=$!

cd ..

# ============ FRONTEND ============
echo ""
echo "📦 Frontend Nuxt..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

cd Front

if [ ! -d "node_modules" ]; then
  echo "Installation des dépendances npm..."
  npm install -q
  if [ $? -eq 0 ]; then
    echo "✅ Dépendances npm installées"
  else
    echo "❌ Erreur npm install"
    kill $DJANGO_PID
    exit 1
  fi
else
  echo "✅ node_modules existe"
fi

echo ""
echo "🚀 Démarrage du serveur Nuxt sur http://localhost:3000"
echo "   (Appuyez sur Ctrl+C pour arrêter)"
echo ""
npm run dev &
NUXT_PID=$!

cd ..

# ============ AFFICHAGE FINAL ============
echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║                 ✅ SYSTEME DEMARRÉ                       ║"
echo "╠══════════════════════════════════════════════════════════╣"
echo "║  Backend API:   http://127.0.0.1:8000                   ║"
echo "║  Admin Django:  http://127.0.0.1:8000/admin             ║"
echo "║    (User: admin, Pass: admin123)                         ║"
echo "║                                                          ║"
echo "║  Frontend:      http://localhost:3000                    ║"
echo "║  Connexion:     http://localhost:3000/connexion          ║"
echo "║  Signup:        http://localhost:3000/signup             ║"
echo "║  Support:       http://localhost:3000/support (pwd reset)║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""
echo "Test utilisateur de démo:"
echo "  Email: test@isoc.local"
echo "  Password: testpass123456"
echo ""

# Attendre Ctrl+C
trap "kill $DJANGO_PID $NUXT_PID 2>/dev/null; echo ''; echo 'Arrêté.'; exit 0" SIGINT

wait
