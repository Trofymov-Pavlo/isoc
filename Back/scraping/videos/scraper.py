# scraping/videos/scraper.py
# -*- coding: utf-8 -*-
"""
Système de scraping vidéo utilisant YouTube Data API v3
"""
import os
import time
import requests
from datetime import datetime, timezone
from typing import Optional
from .keywords import UA_ANCHORS, RU_ANCHORS, NATO_TERMS
from .feeds import YOUTUBE_CHANNELS

# Désactiver les warnings SSL
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_KEY = os.environ.get("YT_API_KEY", "AIzaSyDnEmmnbH3lsMtNbm-rMITQf-3bO-RQZv4")
YTB_API = "https://www.googleapis.com/youtube/v3"


def match_keywords(title: str) -> bool:
    """Vérifie si le titre contient nos mots-clés."""
    txt = title.lower()
    keywords = UA_ANCHORS + RU_ANCHORS + NATO_TERMS
    return any(k.lower() in txt for k in keywords)


def get_uploads_playlist_id(channel_id: str) -> str:
    """Récupère l'ID de la playlist 'uploads' d'une chaîne."""
    r = requests.get(f"{YTB_API}/channels", params={
        "part": "contentDetails",
        "id": channel_id,
        "key": API_KEY
    }, timeout=(5, 10), verify=False)
    r.raise_for_status()
    items = r.json().get("items", [])
    if not items:
        raise ValueError(f"Channel introuvable: {channel_id}")
    return items[0]["contentDetails"]["relatedPlaylists"]["uploads"]


def fetch_channel_videos(
    channel_name: str,
    channel_id: str,
    max_results: int = 50,
    cutoff_ms: int = 0,
) -> list:
    """
    Récupère les vidéos d'une chaîne qui matchent nos mots-clés et la fenêtre temporelle.
    Arrête la pagination dès que les vidéos sont trop anciennes pour optimiser les performances.
    
    Args:
        channel_name: Nom de la chaîne
        channel_id: ID YouTube de la chaîne
        max_results: Nombre max de vidéos à récupérer de l'API par page (50 max)
        cutoff_ms: Timestamp en millisecondes - arrête si vidéos plus anciennes (0 = pas de limite)
    
    Returns:
        Vidéos qui matchent les mots-clés et la période
    """
    try:
        uploads_id = get_uploads_playlist_id(channel_id)
    except Exception as e:
        print(f"❌ {channel_name}: impossible de récupérer uploads playlist: {e}")
        return []

    videos = []
    params = {
        "part": "snippet,contentDetails",
        "playlistId": uploads_id,
        "maxResults": max_results,
        "key": API_KEY,
    }

    page = 0
    consecutive_old = 0  # Compteur de vidéos anciennes consécutives
    MAX_CONSECUTIVE_OLD = 10  # Arrêter après 10 vidéos anciennes consécutives

    while True:
        try:
            # Timeout tuple: 5s connexion, 10s lecture pour éviter les blocages
            r = requests.get(f"{YTB_API}/playlistItems", params=params, timeout=(5, 10), verify=False)
            r.raise_for_status()
            data = r.json()

            for item in data.get("items", []):
                snippet = item.get("snippet", {})
                content = item.get("contentDetails", {})
                
                title = snippet.get("title", "")
                video_id = content.get("videoId", "")
                
                published = content.get("videoPublishedAt") or snippet.get("publishedAt")
                
                # Convertir date ISO en timestamp
                published_time = None
                if published:
                    try:
                        dt = datetime.fromisoformat(published.replace('Z', '+00:00'))
                        published_time = int(dt.timestamp() * 1000)
                    except:
                        pass
                
                # Vérifier si vidéo trop ancienne
                if cutoff_ms > 0 and published_time and published_time < cutoff_ms:
                    consecutive_old += 1
                    # Arrêter si trop de vidéos anciennes consécutives
                    if consecutive_old >= MAX_CONSECUTIVE_OLD:
                        break
                    continue  # Passer à la vidéo suivante
                
                # Réinitialiser le compteur si on trouve une vidéo récente
                consecutive_old = 0
                
                # Filtrer par mots-clés
                if not match_keywords(title):
                    continue

                thumbnail = snippet.get("thumbnails", {})
                thumb_url = (thumbnail.get("high") or thumbnail.get("default") or {}).get("url")

                videos.append({
                    "channel": channel_name,
                    "title": title,
                    "link": f"https://www.youtube.com/watch?v={video_id}",
                    "published": published,
                    "publishedTime": published_time,
                    "thumbnail": thumb_url,
                    "summary": snippet.get("description", "")[:300],
                    "type": "youtube",
                })

            # Arrêter si trop de vidéos anciennes consécutives
            if consecutive_old >= MAX_CONSECUTIVE_OLD:
                break
            
            # Pagination
            token = data.get("nextPageToken")
            if not token:
                break

            page += 1
            params["pageToken"] = token
            time.sleep(0.1)  # rate limiting gentil

        except Exception as e:
            print(f"❌ {channel_name} page {page}: {e}")
            break

    return videos


def get_all_videos(limit_per_channel: int = 50, since_hours: int = 0) -> list:
    """
    Récupère les vidéos de toutes les chaînes configurées filtrées par mots-clés et temps.
    
    Args:
        limit_per_channel: Taille de page API (max 50)
        since_hours: Filtrer les vidéos publiées dans les N dernières heures (0 = pas de filtre)
    
    Returns:
        Vidéos qui matchent les keywords dans la période définie
    """
    # Calculer le timestamp de coupure si nécessaire
    cutoff_ms = 0
    if since_hours > 0:
        from datetime import timedelta
        cutoff_time = datetime.now(timezone.utc) - timedelta(hours=since_hours)
        cutoff_ms = int(cutoff_time.timestamp() * 1000)
    
    all_videos = []
    
    for channel_name, channel_id in YOUTUBE_CHANNELS.items():
        print(f"🔍 Scraping {channel_name}...")
        # Passer cutoff_ms pour arrêter la pagination sur les vidéos anciennes
        videos = fetch_channel_videos(channel_name, channel_id, max_results=limit_per_channel, cutoff_ms=cutoff_ms)
        
        # Plus besoin de filtrer ici, c'est déjà fait dans fetch_channel_videos
        all_videos.extend(videos)
        
        if videos:
            print(f"✅ {channel_name}: {len(videos)} vidéos (filtrées par temps et mots-clés)")
        else:
            print(f"⚪ {channel_name}: 0 vidéos (aucune correspondance)")
        
        # Archivage immédiat des vidéos filtrées uniquement
        if videos:
            try:
                from scraping.archive import add_videos
                add_videos(videos)
            except Exception as e:
                print(f"⚠️ Archivage pour {channel_name} échoué: {e}")
        time.sleep(0.2)  # rate limiting entre chaînes

    # Trier par date décroissante
    all_videos.sort(key=lambda v: v.get("publishedTime") or 0, reverse=True)
    
    return all_videos


if __name__ == "__main__":
    # Test
    videos = get_all_videos(limit_per_channel=50)
    print(f"\n🎬 Total: {len(videos)} vidéos matchant les keywords")
    for v in videos[:10]:
        print(f"  - {v['channel']}: {v['title'][:60]}")
