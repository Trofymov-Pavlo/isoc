# scraping/video.py
# -*- coding: utf-8 -*-
"""
Video scraping module
Utilise maintenant YouTube Data API v3 au lieu du parsing RSS
"""

from typing import List, Dict, Optional
from datetime import datetime, timezone, timedelta

from .video_api import get_all_videos


def get_videos(
    feeds_dict=None,  # Ignoré maintenant, on utilise video_api
    since_hours: int = 0,
    channel: Optional[str] = None,
    limit: int = 30
) -> List[Dict]:
    """
    Récupère les vidéos YouTube filtrées par mots-clés via API.
    
    Args:
        feeds_dict: Ignoré (rétro-compatibilité)
        since_hours: Nombre d'heures en arrière (0 = toutes les vidéos)
        channel: Filtrer par nom de chaîne (optionnel)
        limit: Nombre max de vidéos à retourner
    
    Returns:
        Liste de dicts avec: channel, title, link, published, publishedTime, thumbnail, summary, type
    """
    print(f"📹 Récupération des vidéos via YouTube API...")
    
    # Récupère les vidéos via API (max 5 par channel pour accélérer)
    all_videos = get_all_videos(limit_per_channel=50, stop_after_match=5)
    
    # Filtre par date si nécessaire
    if since_hours > 0:
        cutoff_time = datetime.now(timezone.utc) - timedelta(hours=since_hours)
        cutoff_ms = int(cutoff_time.timestamp() * 1000)
        all_videos = [v for v in all_videos if (v.get("publishedTime") or 0) >= cutoff_ms]
        print(f"✅ Après filtre {since_hours}h: {len(all_videos)} vidéos")
    
    # Filtre par chaîne si spécifié
    if channel:
        all_videos = [v for v in all_videos if v.get("channel") == channel]
        print(f"✅ Après filtre channel '{channel}': {len(all_videos)} vidéos")
    
    # Limite le nombre de résultats
    result = all_videos[:limit]
    print(f"🎬 Retour de {len(result)} vidéos (limite: {limit})")

    # Archivage immédiat
    try:
        from scraping.archive import add_videos
        add_videos(result)
    except Exception as e:
        print(f"⚠️ Archivage vidéos échoué: {e}")

    return result
