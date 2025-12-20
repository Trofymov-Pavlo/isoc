# scraping/videos/core.py
# -*- coding: utf-8 -*-
"""
Video scraping module
Utilise YouTube Data API v3
"""

from typing import List, Dict, Optional
from datetime import datetime, timezone, timedelta

from .api import get_all_videos


def get_videos(
    feeds_dict=None,  # Ignoré maintenant, on utilise video_api
    since_hours: int = 24,
    channel: Optional[str] = None,
) -> List[Dict]:
    """
    Récupère TOUTES les vidéos YouTube filtrées par mots-clés via API.
    AUCUNE limite artificielle - seuls filtres: keywords + 24h par défaut.
    
    Args:
        feeds_dict: Ignoré (rétro-compatibilité)
        since_hours: Nombre d'heures en arrière (défaut: 24h)
        channel: Filtrer par nom de chaîne (optionnel)
    
    Returns:
        TOUTES les vidéos qui matchent les keywords dans la période
    """
    print(f"📹 Récupération des vidéos via YouTube API (dernières {since_hours}h)...")
    
    # Récupère les vidéos déjà filtrées par temps et mots-clés
    all_videos = get_all_videos(limit_per_channel=50, since_hours=since_hours)
    
    # Filtre par chaîne si spécifié
    if channel:
        all_videos = [v for v in all_videos if v.get("channel") == channel]
        print(f"✅ Après filtre channel '{channel}': {len(all_videos)} vidéos")
    
    print(f"🎬 {len(all_videos)} vidéos retournées (AUCUNE limite)")
    return all_videos


def backfill_all_videos(limit_per_channel: int = 50) -> List[Dict]:
    """Scrape toutes les vidéos disponibles et les archive."""
    videos = get_all_videos(limit_per_channel=limit_per_channel)
    try:
        from scraping.archive import add_videos
        add_videos(videos)
    except Exception as e:
        print(f"⚠️ Archivage backfill échoué: {e}")
    return videos


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Scraping vidéo YouTube (dernières 24h)")
    parser.add_argument("--hours", type=int, default=24, help="Nombre d'heures en arrière (défaut: 24)")
    parser.add_argument("--per-channel", type=int, default=50, help="Taille de page API (max 50)")

    args = parser.parse_args()

    videos = get_videos(since_hours=args.hours)
    print(f"\n🎬 Total: {len(videos)} vidéos matchant les keywords")
    for v in videos[:10]:
        print(f"  - {v['channel']}: {v['title'][:80]}")
    
    print(f"\n💾 Vidéos automatiquement archivées dans Front/public/archive.json")
