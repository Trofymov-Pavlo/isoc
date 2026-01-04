#!/usr/bin/env bash
# AXIOME - Start (macOS)
# Lance Frontend (Nuxt) + Backend (Django) + scraping automatique
# Usage: ./start-mac.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

mkdir -p logs

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

SCRAPING_FIRST_RUN="$SCRIPT_DIR/.scraping_first_run"

cleanup() {
  echo ""
  echo -e "${YELLOW}Arrêt de tous les services...${NC}"
  kill $(jobs -p) 2>/dev/null || true
  exit 0
}
trap cleanup INT TERM

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || {
    echo -e "${YELLOW}⚠ Commande manquante: $1${NC}" >&2
    exit 1
  }
}

require_cmd npm
require_cmd python3

echo -e "${BLUE}[1/3] Frontend Nuxt...${NC}"
cd Front
if [ ! -d "node_modules" ]; then
    echo -e "${YELLOW}Premier lancement : Installation des dépendances Frontend...${NC}"
    npm install
fi
npm run dev > ../logs/frontend.log 2>&1 &
FRONTEND_PID=$!
cd ..
echo -e "${GREEN}✓ Frontend (PID: $FRONTEND_PID) → http://localhost:3000${NC}"

echo -e "${BLUE}[2/3] Backend Django...${NC}"
cd Back

if [ -f "venv/bin/python" ]; then
  PYTHON_CMD=("venv/bin/python")
  echo -e "${GREEN}✓ Utilisation venv Python (macOS)${NC}"
else
  PYTHON_CMD=("python3")
  echo -e "${YELLOW}⚠ Utilisation Python système (python3)${NC}"
fi

"${PYTHON_CMD[@]}" manage.py runserver 8000 > ../logs/backend.log 2>&1 &
BACKEND_PID=$!
cd ..
echo -e "${GREEN}✓ Backend (PID: $BACKEND_PID) → http://localhost:8000${NC}"

echo -e "${BLUE}[3/3] Scraping...${NC}"
if [ ! -f "$SCRAPING_FIRST_RUN" ]; then
  echo -e "${YELLOW}Premier lancement → scraping du dernier jour${NC}"
  cd Back
  "${PYTHON_CMD[@]}" -m scraping.api --days 1 > ../logs/scraping.log 2>&1
  cd ..
  touch "$SCRAPING_FIRST_RUN"
else
  echo -e "${GREEN}✓ Scraping initial déjà effectué${NC}"
fi

echo -e "${BLUE}Scraping périodique (30 minutes)...${NC}"
cd Back
while true; do
  sleep 1800
  echo -e "${YELLOW}[$(date '+%Y-%m-%d %H:%M:%S')] Scraping (1 heure)...${NC}"
  "${PYTHON_CMD[@]}" -m scraping.api --hours 1 >> ../logs/scraping.log 2>&1
done &
cd ..

echo ""
echo -e "${GREEN}✓ Tous les services sont lancés${NC}"
echo "  • Frontend → http://localhost:3000"
echo "  • Backend  → http://localhost:8000"
echo "  • Logs     → ./logs"
echo -e "${YELLOW}Ctrl+C pour arrêter${NC}"

wait
