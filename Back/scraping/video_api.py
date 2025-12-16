# -*- coding: utf-8 -*-
"""
Nouveau système de scraping vidéo utilisant YouTube Data API v3
au lieu du parsing RSS.
"""
import os
import time
import requests
from datetime import datetime, timezone
from typing import Optional
from scraping.keywords import UA_ANCHORS, RU_ANCHORS, NATO_TERMS

# Désactiver les warnings SSL
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_KEY = os.environ.get("YT_API_KEY", "AIzaSyDnEmmnbH3lsMtNbm-rMITQf-3bO-RQZv4")
YTB_API = "https://www.googleapis.com/youtube/v3"

# Liste des channel IDs à scraper
YOUTUBE_CHANNELS = {
    # Français
    "ARTE": "UCwI-JbGNsojunnHbFAc0M4Q",
    "Le Monde": "UCYpRDnhk5H8h16jpS84uqsA",
    "France 24": "UCCCPCZNChQdGa9EkATeye4g",
    "BFM TV": "UCXwDLMDV86ldKoFVc_g8P0g",
    "CNews": "UCXKJrYczY2_fJEZgFPGY0HQ",
    "France Inter": "UCJldRgT_D7Am-ErRHQZ90uw",
    "Mediapart": "UCdnaDhU-LDQrIEEmSIfq0-Q",
    "Brut": "UCSKdvgqdnj72_SLggp7BDTg",
    "Konbini": "UCHQda5vLxrH0Ff0I0kMq4zw",
    # International anglophone
    "BBC News": "UC16niRr50-MSBwiO3YDb3RA",
    "DW News": "UCknLrEdhRcp1aegoMqRaCZg",
    "Euronews": "UCW2QcKZiU8aUGg4yxCIditg",
    "CNN": "UCupvZG-5ko_eiXAupbDfxWw",
    "ABC News": "UCBi2mrWuNuyYy4gbM6fU18Q",
    "CBS News": "UC8p1vwvWtl6T73JiExfWs1g",
    "Fox News": "UCXIJgqnII2ZOINSWNOGFThA",
    "Associated Press": "UC52X5wxOL_s5yw0dQk7NtgA",
    "Al Jazeera English": "UCNye-wNBqNL5ZzHSJj3l8Bg",
    "Reuters": "UChqUTb7kYRX8-EiaN3XFrSQ",
    "Sky News": "UCoMdktPbSTixAyNGwb-UYkQ",
    # Military/Defense
    "Warthog Defense": "UC2JaXg63L_VqvXN4SwF4zOQ",
    "Defense Updates": "UCKNCbBWiMiXBVXUmUuu_dsQ",
    # Documentary
    "National Geographic": "UCpVm7bg6pXKo1Pr6k5kxG9A",
    "Discovery Channel": "UCqOoboPm3uhY_YXhvhmL-WA",
    "Discovery Channel France": "UCJ3uq_dgtGdfScO21KU08wg",
}


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
) -> list:
    """
    Récupère TOUTES les vidéos d'une chaîne qui matchent nos mots-clés.
    AUCUNE limite artificielle - scrape jusqu'à épuisement des vidéos matchantes.
    
    Args:
        channel_name: Nom de la chaîne
        channel_id: ID YouTube de la chaîne
        max_results: Nombre max de vidéos à récupérer de l'API par page (50 max)
    
    Returns:
        TOUTES les vidéos qui matchent les mots-clés
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
                
                if not match_keywords(title):
                    continue

                published = content.get("videoPublishedAt") or snippet.get("publishedAt")
                thumbnail = snippet.get("thumbnails", {})
                thumb_url = (thumbnail.get("high") or thumbnail.get("default") or {}).get("url")
                
                # Convertir date ISO en timestamp
                published_time = None
                if published:
                    try:
                        dt = datetime.fromisoformat(published.replace('Z', '+00:00'))
                        published_time = int(dt.timestamp() * 1000)
                    except:
                        pass

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


def get_all_videos(limit_per_channel: int = 50) -> list:
    """
    Récupère TOUTES les vidéos de toutes les chaînes configurées.
    AUCUNE limite artificielle - seul filtre : les mots-clés.
    
    Args:
        limit_per_channel: Taille de page API (max 50)
    
    Returns:
        TOUTES les vidéos qui matchent les keywords, tous channels confondus
    """
    all_videos = []
    
    for channel_name, channel_id in YOUTUBE_CHANNELS.items():
        print(f"🔍 Scraping {channel_name}...")
        videos = fetch_channel_videos(channel_name, channel_id, max_results=limit_per_channel)
        all_videos.extend(videos)
        print(f"✅ {channel_name}: {len(videos)} vidéos matchent les mots-clés")
        # Archivage immédiat par chaîne avant de passer à la suivante
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
