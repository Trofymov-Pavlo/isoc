# scraping/video.py
# -*- coding: utf-8 -*-
"""
Video scraping module
Gère le scraping des vidéos YouTube via les flux RSS
"""

import json
from typing import List, Dict, Tuple
from datetime import datetime, timezone
import feedparser

from .http_state import fetch_rss_once
from .textops import to_iso, norm_text


def parse_youtube_feed(xml_bytes: bytes, channel_name: str) -> Tuple[List[Dict], List[str]]:
    """
    Parse un flux RSS YouTube et extrait les vidéos
    Les flux YouTube retournent la structure suivante:
    - title: titre de la vidéo
    - link: URL de la vidéo
    - published: date de publication
    - media:thumbnail: image de la vidéo (en tant qu'attribut du media namespace)
    """
    try:
        feed = feedparser.parse(xml_bytes)
        if feed.bozo:
            raise RuntimeError(f"Flux YouTube mal formé pour {channel_name}")
        
        items = []
        hay = []
        
        for entry in feed.entries:
            title = getattr(entry, 'title', '').strip()
            link = getattr(entry, 'link', '').strip()
            published_struct = getattr(entry, 'published_parsed', None)
            published_iso = to_iso(published_struct) if published_struct else ""
            
            # Extrait la miniature YouTube
            # YouTube fournit media_thumbnail dans les flux RSS
            thumbnail = None
            if hasattr(entry, 'media_thumbnail'):
                try:
                    if isinstance(entry.media_thumbnail, list) and len(entry.media_thumbnail) > 0:
                        thumbnail = entry.media_thumbnail[0].get('url')
                    elif isinstance(entry.media_thumbnail, dict):
                        thumbnail = entry.media_thumbnail.get('url')
                except Exception:
                    pass
            
            # Fallback: utilise le premier media_content s'il existe
            if not thumbnail and hasattr(entry, 'media_content'):
                try:
                    if isinstance(entry.media_content, list) and len(entry.media_content) > 0:
                        thumbnail = entry.media_content[0].get('url')
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
                print(f"⚠️ Flux YouTube {channel_name}: aucune réponse")
                continue
            
            videos, hay = parse_youtube_feed(xml, channel_name)
            all_videos.extend(videos)
            all_hay.extend(hay)
            print(f"✅ {channel_name}: {len(videos)} vidéo(s) récupérée(s)")
        
        except Exception as ex:
            print(f"❌ Erreur lecture flux {channel_name}: {ex}")
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
    since_hours: int = 48,
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
    since_hours: int = 48,
    channel: str = None,
    limit: int = 30,
) -> List[Dict]:
    """Alias pour collect_videos (API compatible)"""
    return collect_videos(feeds, since_hours=since_hours, channel=channel, limit=limit)
