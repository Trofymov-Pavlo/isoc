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
    since_hours: int = 24,
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
    
    # Récupère toutes les vidéos via API
    all_videos = get_all_videos(limit_per_channel=100)
    
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
    
    return result
                except Exception:
                    pass
            
            # Utilise une description/summary si disponible
            summary = getattr(entry, 'summary', '').strip()
            
            # Construit l'item vidéo
            video_item = {
                "channel": channel_name,
                "title": title,
                "link": link,
                "published": published_iso,
                "thumbnail": thumbnail,
                "summary": summary,
                "type": "youtube",
            }
            
            items.append(video_item)
            hay.append(norm_text(title, summary))
        
        return items, hay
    
    except Exception as e:
        print(f"❌ Erreur parsing feed YouTube {channel_name}: {e}")
        return [], []


def fetch_all_videos(feeds: Dict[str, str], timeout: int = 20) -> Tuple[List[Dict], List[str]]:
    """
    Récupère toutes les vidéos de tous les flux YouTube fournis
    Retourne une liste de vidéos et une liste de textes de recherche (hay)
    """
    all_videos = []
    all_hay = []
    
    for channel_name, url in feeds.items():
        try:
            xml = fetch_rss_once(url, timeout=timeout)
            if xml is None:
                continue
            
            videos, hay = parse_youtube_feed(xml, channel_name)
            all_videos.extend(videos)
            all_hay.extend(hay)
        
        except Exception as ex:
            all_videos.append({
                "channel": channel_name,
                "title": f"[AVERTISSEMENT] Échec de lecture du flux YouTube: {channel_name}",
                "link": url,
                "published": "",
                "type": "youtube",
                "error": str(ex),
                "summary": "",
                "thumbnail": None,
            })
            all_hay.append("")
    
    # Filtre par mots-clés (mêmes règles que les articles)
    if all_hay:
        filtered = []
        for v, hay in zip(all_videos, all_hay):
            if passes_filter(hay):
                filtered.append(v)
        all_videos = filtered

    # Tri par date de publication (plus récentes d'abord)
    all_videos = sorted(all_videos, key=lambda v: v.get("published", ""), reverse=True)
    
    return all_videos, all_hay


def deduplicate_videos(videos: List[Dict]) -> List[Dict]:
    """Supprime les vidéos en doublon (par lien YouTube)"""
    seen_links = set()
    out = []
    
    for v in videos:
        link = (v.get("link") or "").strip()
        if link:
            if link in seen_links:
                continue
            seen_links.add(link)
        out.append(v)
    
    return out


def within_hours_videos(videos: List[Dict], hours: int) -> List[Dict]:
    """Filtre les vidéos pour ne garder que celles publiées dans les N dernières heures"""
    if hours <= 0:
        return videos
    
    cutoff = datetime.now(timezone.utc).timestamp() - hours * 3600
    out = []
    
    for v in videos:
        iso = v.get("published", "")
        try:
            if iso:
                dt = datetime.fromisoformat(iso)
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                if dt.timestamp() >= cutoff:
                    out.append(v)
            else:
                out.append(v)
        except Exception:
            out.append(v)
    
    return out


def collect_videos(
    feeds: Dict[str, str],
    since_hours: int = 24,
    channel: str = None,
    limit: int = 30,
) -> List[Dict]:
    """
    Récupère et filtre les vidéos
    Paramètres:
    - since_hours: ne garder que les vidéos des N dernières heures
    - channel: filtrer par canal YouTube spécifique
    - limit: nombre maximum de vidéos à retourner
    """
    videos, _ = fetch_all_videos(feeds, timeout=20)
    
    if since_hours and since_hours > 0:
        videos = within_hours_videos(videos, since_hours)
    
    videos = deduplicate_videos(videos)
    
    if channel:
        videos = [v for v in videos if v.get("channel") == channel]
    
    if limit and limit > 0:
        videos = videos[:limit]
    
    # Ajoute publishedTime en millisecondes (compatible avec le frontend)
    for v in videos:
        pub = v.get("published")
        try:
            if pub:
                dt = datetime.fromisoformat(pub)
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                v["publishedTime"] = int(dt.timestamp() * 1000)
            else:
                v["publishedTime"] = None
        except Exception:
            v["publishedTime"] = None
    
    return videos


def get_videos(
    feeds: Dict[str, str],
    since_hours: int = 24,
    channel: str = None,
    limit: int = 30,
) -> List[Dict]:
    """Alias pour collect_videos (API compatible)"""
    return collect_videos(feeds, since_hours=since_hours, channel=channel, limit=limit)
