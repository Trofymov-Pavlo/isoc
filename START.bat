@echo off
REM Script pour démarrer AXIOME - Media indépendant

echo.
echo ========================================
echo AXIOME - Démarrage du projet
echo ========================================
echo.

REM Vérifier si Back et Front existent
if not exist "Back" (
    echo ERREUR: Dossier Back/ non trouvé
    exit /b 1
)

if not exist "Front" (
    echo ERREUR: Dossier Front/ non trouvé
    exit /b 1
)

echo [1] Démarrage du Backend (Python Flask)...
echo     Terminal 1: cd Back ^&^& venv\Scripts\activate ^&^& python -m scraping.api
echo.

echo [2] Démarrage du Frontend (Nuxt Vue)...
echo     Terminal 2: cd Front ^&^& npm run dev
echo.

echo ========================================
echo.
echo ✅ Instructions:
echo.
echo Terminal 1 (Backend):
echo    cd Back
echo    venv\Scripts\activate
echo    python -m scraping.api
echo.
echo Terminal 2 (Frontend):
echo    cd Front
echo    npm run dev
echo.
echo ✅ L'API sera sur http://127.0.0.1:5000
echo ✅ Le site sera sur http://localhost:3000
echo.
echo ========================================
echo.

pause
