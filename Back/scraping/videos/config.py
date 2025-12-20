# -*- coding: utf-8 -*-
"""
Configuration du module YouTube.

Charge la clé API à partir des variables d'environnement (et d'un éventuel fichier .env)
sans jamais la hardcoder dans le code source.
"""
import os
from pathlib import Path

try:
    # Charge les variables depuis un fichier .env si présent
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    # dotenv est optionnel; si non présent, on ignore.
    pass

# Clé API YouTube Data v3
def _read_local_key() -> str:
    """Read API key from a local file in the videos folder if present."""
    try:
        key_path = Path(__file__).parent / "yt_api_key.txt"
        if key_path.exists():
            return key_path.read_text(encoding="utf-8").strip()
    except Exception:
        pass
    return ""

# Prefer env var; fallback to local file yt_api_key.txt
API_KEY: str = os.environ.get("YT_API_KEY", "") or _read_local_key()

# Endpoint racine de l'API YouTube
YTB_API: str = "https://www.googleapis.com/youtube/v3"

def has_api_key() -> bool:
    """Retourne True si une clé API est configurée."""
    return bool(API_KEY)
