#!/usr/bin/env bash
# AXIOME - Start (Windows via Git Bash)
# Suit les étapes du README (Backend puis Frontend)
# Usage: ./start-win.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

mkdir -p logs

RUN_TS="$(date '+%Y%m%d-%H%M%S')"
FRONTEND_LOG="$SCRIPT_DIR/logs/frontend-$RUN_TS.log"
BACKEND_LOG="$SCRIPT_DIR/logs/backend-$RUN_TS.log"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

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

if command -v python >/dev/null 2>&1; then
  PYTHON_BASE=("python")
elif command -v py >/dev/null 2>&1; then
  PYTHON_BASE=("py" "-3")
else
  echo -e "${YELLOW}⚠ Python introuvable (installe Python 3.8+)${NC}" >&2
  exit 1
fi

VENV_PY="$SCRIPT_DIR/Back/venv/Scripts/python.exe"

echo -e "${BLUE}[1/2] Backend Django...${NC}"
cd Back

if [ ! -f "$VENV_PY" ]; then
  echo -e "${YELLOW}venv absent → création (README: python -m venv venv)${NC}"
  "${PYTHON_BASE[@]}" -m venv venv
fi

echo -e "${BLUE}Dépendances (README: pip install -r requirements.txt)${NC}"
"$VENV_PY" -m pip install -r requirements.txt

echo -e "${BLUE}Migration (README: python manage.py migrate)${NC}"
"$VENV_PY" manage.py migrate

echo -e "${BLUE}Démarrage (README: python manage.py runserver 8000)${NC}"
"$VENV_PY" manage.py runserver 8000 > "$BACKEND_LOG" 2>&1 &
BACKEND_PID=$!
cd ..
echo -e "${GREEN}✓ Backend (PID: $BACKEND_PID) → http://localhost:8000${NC}"

echo -e "${BLUE}[2/2] Frontend Nuxt...${NC}"
cd Front

if [ ! -d node_modules ]; then
  echo -e "${YELLOW}node_modules absent → npm install (README)${NC}"
  npm install
fi

npm run dev > "$FRONTEND_LOG" 2>&1 &
FRONTEND_PID=$!
cd ..
echo -e "${GREEN}✓ Frontend (PID: $FRONTEND_PID) → http://localhost:3000${NC}"

echo ""
echo -e "${GREEN}✓ Tous les services sont lancés${NC}"
echo "  • Frontend → http://localhost:3000"
echo "  • Backend  → http://localhost:8000"
echo "  • Logs     → ./logs"
echo "    - $FRONTEND_LOG"
echo "    - $BACKEND_LOG"
echo -e "${YELLOW}Ctrl+C pour arrêter${NC}"

wait
