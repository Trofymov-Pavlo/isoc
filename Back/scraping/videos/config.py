# -*- coding: utf-8 -*-
"""
Configuration du module YouTube.

Charge la clé API à partir des variables d'environnement (et d'un éventuel fichier .env)
sans jamais la hardcoder dans le code source.
"""
import os

try:
    # Charge les variables depuis un fichier .env si présent
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    # dotenv est optionnel; si non présent, on ignore.
    pass

# Clé API YouTube Data v3
API_KEY: str = os.environ.get("YT_API_KEY", "")

# Endpoint racine de l'API YouTube
YTB_API: str = "https://www.googleapis.com/youtube/v3"

def has_api_key() -> bool:
    """Retourne True si une clé API est configurée."""
    return bool(API_KEY)
