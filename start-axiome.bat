@echo off
REM AXIOME - Script de demarrage complet (Windows)
REM Lance Frontend, Backend Django et Scraping automatique

setlocal enabledelayedexpansion

echo ==========================================
echo   AXIOME · Information ^& Analyse
echo   Demarrage de tous les services
echo ==========================================
echo.

REM Creer le dossier logs s'il n'existe pas
if not exist logs mkdir logs

REM Fichier pour tracker si c'est le premier lancement
set SCRAPING_FIRST_RUN=.scraping_first_run

echo [1/3] Lancement Frontend Nuxt...
cd Front
start /B npm run dev > ..\logs\frontend.log 2>&1
cd ..
echo [OK] Frontend lance -^> http://localhost:3000
echo.

echo [2/3] Lancement Backend Django...
cd Back

REM Activation environnement virtuel
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
    echo [OK] Environnement virtuel active
) else (
    echo [!] Pas d'environnement virtuel trouve
)

REM Lancement Django
start /B python manage.py runserver 8000 > ..\logs\backend.log 2>&1
cd ..
echo [OK] Backend Django lance -^> http://localhost:8000
echo.

echo [3/3] Configuration du scraping automatique...

REM Premier lancement : scraping 7 jours
if not exist %SCRAPING_FIRST_RUN% (
    echo Premier lancement detecte -^> Scraping du dernier jour
    cd Back
    python -m scraping.api --days 1 > ..\logs\scraping.log 2>&1
    cd ..
    echo. > %SCRAPING_FIRST_RUN%
    echo [OK] Scraping initial termine ^(1 jour^)
) else (
    echo [OK] Premier lancement deja effectue
)

echo Lancement du scraping periodique ^(30 minutes^)...
echo.

echo ==========================================
echo [OK] Tous les services sont lances !
echo ==========================================
echo.
echo Services actifs :
echo   * Frontend Nuxt    -^> http://localhost:3000
echo   * Backend Django   -^> http://localhost:8000
echo   * Scraping auto    -^> Toutes les 30 minutes
echo.
echo Logs disponibles dans /logs/
echo   * frontend.log
echo   * backend.log
echo   * scraping.log
echo.
echo Appuyez sur Ctrl+C pour arreter tous les services
echo.

REM Boucle de scraping toutes les 30 minutes
:loop
timeout /t 1800 /nobreak >nul
echo [%date% %time%] Scraping automatique ^(1 heure^)...
cd Back
python -m scraping.api --hours 1 >> ..\logs\scraping.log 2>&1
cd ..
echo [OK] Scraping termine
goto loop
