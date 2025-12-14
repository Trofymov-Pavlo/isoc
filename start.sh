#!/bin/bash

# Script pour démarrer AXIOME - Média indépendant

echo ""
echo "========================================"
echo "AXIOME - Démarrage du projet"
echo "========================================"
echo ""

# Vérifier si Back et Front existent
if [ ! -d "Back" ]; then
    echo "ERREUR: Dossier Back/ non trouvé"
    exit 1
fi

if [ ! -d "Front" ]; then
    echo "ERREUR: Dossier Front/ non trouvé"
    exit 1
fi

echo "[1] Démarrage du Backend (Python Flask)..."
echo "    Terminal 1: cd Back && source venv/bin/activate && python -m scraping.api"
echo ""

echo "[2] Démarrage du Frontend (Nuxt Vue)..."
echo "    Terminal 2: cd Front && npm run dev"
echo ""

echo "========================================"
echo ""
echo "✅ Instructions:"
echo ""
echo "Terminal 1 (Backend):"
echo "   cd Back"
echo "   source venv/bin/activate"
echo "   python -m scraping.api"
echo ""
echo "Terminal 2 (Frontend):"
echo "   cd Front"
echo "   npm run dev"
echo ""
echo "✅ L'API sera sur http://127.0.0.1:5000"
echo "✅ Le site sera sur http://localhost:3000"
echo ""
echo "========================================"
echo ""
