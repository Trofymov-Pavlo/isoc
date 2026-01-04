#!/usr/bin/env bash
# AXIOME - Script de démarrage (macOS/Linux)
# Lance Frontend (Nuxt), Backend (Django) + scraping automatique

set -euo pipefail

echo "=========================================="
echo "  AXIOME · Information & Analyse"
echo "  Démarrage de tous les services"
echo "=========================================="
echo ""

# Couleurs pour les logs
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

mkdir -p logs

# Fichier pour tracker si c'est le premier lancement du scraping
SCRAPING_FIRST_RUN="$SCRIPT_DIR/.scraping_first_run"

# Fonction pour arrêter tous les process à la sortie
cleanup() {
    echo ""
    echo -e "${YELLOW}Arrêt de tous les services...${NC}"
    kill $(jobs -p) 2>/dev/null || true
    exit 0
}

trap cleanup INT TERM

require_cmd() {
    command -v "$1" >/dev/null 2>&1 || {
        echo -e "${YELLOW}⚠ Commande manquante: $1${NC}"
        echo "Installez-la puis relancez le script." >&2
        exit 1
    }
}

require_cmd npm

# 1. Frontend Nuxt (port 3000)
echo -e "${BLUE}[1/3] Lancement Frontend Nuxt...${NC}"
cd Front
if [ ! -d "node_modules" ]; then
    echo -e "${YELLOW}Premier lancement : Installation des dépendances Frontend...${NC}"
    npm install
fi
npm run dev > ../logs/frontend.log 2>&1 &
FRONTEND_PID=$!
cd ..
echo -e "${GREEN}✓ Frontend lancé (PID: $FRONTEND_PID) → http://localhost:3000${NC}"
echo ""

# 2. Backend Django (port 8000)
echo -e "${BLUE}[2/3] Lancement Backend Django...${NC}"
cd Back

# Déterminer l'interpréteur Python à utiliser
if [ -f "venv/Scripts/python.exe" ]; then
    PYTHON_CMD="venv/Scripts/python.exe"
    echo -e "${GREEN}✓ Utilisation venv Python (Windows)${NC}"
elif [ -f "venv/bin/python" ]; then
    PYTHON_CMD="venv/bin/python"
    echo -e "${GREEN}✓ Utilisation venv Python (Unix)${NC}"
else
        if command -v python3 >/dev/null 2>&1; then
            PYTHON_CMD="python3"
        else
            PYTHON_CMD="python"
        fi
        echo -e "${YELLOW}⚠ Utilisation Python système ($PYTHON_CMD)${NC}"
fi

require_cmd "$PYTHON_CMD"

# Lancement Django avec l'interpréteur du venv
$PYTHON_CMD manage.py runserver 8000 > ../logs/backend.log 2>&1 &
BACKEND_PID=$!
cd ..
echo -e "${GREEN}✓ Backend Django lancé (PID: $BACKEND_PID) → http://localhost:8000${NC}"
echo ""

# 3. Scraping automatique
echo -e "${BLUE}[3/3] Configuration du scraping automatique...${NC}"

# Premier lancement : scraping 1 jour
if [ ! -f "$SCRAPING_FIRST_RUN" ]; then
    echo -e "${YELLOW}Premier lancement détecté → Scraping du dernier jour${NC}"
    cd Back
    $PYTHON_CMD -m scraping.api --days 1 > ../logs/scraping.log 2>&1
    cd ..
    touch "$SCRAPING_FIRST_RUN"
    echo -e "${GREEN}✓ Scraping initial terminé (1 jour)${NC}"
else
    echo -e "${GREEN}✓ Premier lancement déjà effectué${NC}"
fi

# Boucle de scraping toutes les 30 minutes
echo -e "${BLUE}Lancement du scraping périodique (30 minutes)...${NC}"
cd Back
while true; do
    sleep 1800  # 30 minutes
    echo -e "${YELLOW}[$(date '+%Y-%m-%d %H:%M:%S')] Scraping automatique (1 heure)...${NC}"
    $PYTHON_CMD -m scraping.api --hours 1 >> ../logs/scraping.log 2>&1
    echo -e "${GREEN}✓ Scraping terminé${NC}"
done &
SCRAPING_PID=$!
cd ..

echo ""
echo "=========================================="
echo -e "${GREEN}✓ Tous les services sont lancés !${NC}"
echo "=========================================="
echo ""
echo "Services actifs :"
echo "  • Frontend Nuxt    → http://localhost:3000"
echo "  • Backend Django   → http://localhost:8000"
echo "  • Scraping auto    → Toutes les 30 minutes"
echo ""
echo "Logs disponibles dans /logs/"
echo "  • frontend.log"
echo "  • backend.log"
echo "  • scraping.log"
echo ""
echo -e "${YELLOW}Appuyez sur Ctrl+C pour arrêter tous les services${NC}"
echo ""

# Attendre indéfiniment (les process tournent en arrière-plan)
wait
