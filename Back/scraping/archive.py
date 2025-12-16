# scraping/archive.py
# -*- coding: utf-8 -*-
"""
Archive persistence module
Gère la sauvegarde permanente des articles et vidéos scrapés dans archive.json
"""

import json
import os
from typing import List, Dict
from datetime import datetime, timezone
from pathlib import Path
import threading

# Chemin vers le fichier archive dans Front/public pour que Nuxt puisse le lire
ARCHIVE_FILE = Path(__file__).parent.parent.parent / "Front" / "public" / "archive.json"
ARCHIVE_LOCK = threading.Lock()


def _get_archive_path():
    """Retourne le chemin du fichier archive.json"""
    return ARCHIVE_FILE


def _load_archive() -> Dict[str, List[Dict]]:
    """Charge le contenu actuel de l'archive"""
    archive_path = _get_archive_path()
    
    if not archive_path.exists():
        return {"articles": [], "videos": []}
    
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Assure que les clés existent
            if "articles" not in data:
                data["articles"] = []
            if "videos" not in data:
                data["videos"] = []
            data["articles"] = _sort_entries(data.get("articles", []))
            data["videos"] = _sort_entries(data.get("videos", []))
            return data
    except Exception as e:
        print(f"⚠️ Erreur lors de la lecture de l'archive: {e}")
        return {"articles": [], "videos": []}


def _save_archive(data: Dict[str, List[Dict]]):
    """Sauvegarde l'archive"""
    archive_path = _get_archive_path()
    
    try:
        with open(archive_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde de l'archive: {e}")


def _to_timestamp(entry: Dict) -> int:
    """Retourne un timestamp (ms) basé sur published/publishedTime/archived_at."""
    if not entry:
        return 0

    try:
        pt = entry.get("publishedTime")
        if pt is not None:
            return int(pt)
    except Exception:
        pass

    for key in ("published", "archived_at", "archivedAt"):
        iso = entry.get(key)
        if not iso:
            continue
        try:
            dt = datetime.fromisoformat(str(iso).replace("Z", "+00:00"))
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return int(dt.timestamp() * 1000)
        except Exception:
            continue

    return 0


def _sort_entries(entries: List[Dict]) -> List[Dict]:
    """Trie les entrées par date décroissante sans supprimer les anciens éléments."""
    return sorted(entries, key=_to_timestamp, reverse=True)


def _is_duplicate(item: Dict, existing_list: List[Dict]) -> bool:
    """Vérifie si un item existe déjà dans la liste (par lien)"""
    item_link = (item.get("link") or "").strip()
    if item_link:
        for existing in existing_list:
            if (existing.get("link") or "").strip() == item_link:
                return True
    return False


def add_articles(articles: List[Dict]):
    """
    Ajoute les nouveaux articles à l'archive
    Évite les doublons basés sur le lien
    """
    if not articles:
        return
    
    with ARCHIVE_LOCK:
        archive = _load_archive()
        existing_articles = archive.get("articles", [])
        
        added_count = 0
        for article in articles:
            # Évite les doublons
            if not _is_duplicate(article, existing_articles):
                # Ajoute un timestamp de sauvegarde
                article_copy = article.copy()
                article_copy["archived_at"] = datetime.now(timezone.utc).isoformat()
                existing_articles.append(article_copy)
                added_count += 1
        
        archive["articles"] = _sort_entries(existing_articles)
        _save_archive(archive)
        
        if added_count > 0:
            print(f"✅ {added_count} article(s) ajouté(s) à l'archive")


def add_videos(videos: List[Dict]):
    """
    Ajoute les nouvelles vidéos à l'archive
    Évite les doublons basés sur le lien YouTube
    """
    if not videos:
        return
    
    with ARCHIVE_LOCK:
        archive = _load_archive()
        existing_videos = archive.get("videos", [])
        
        added_count = 0
        for video in videos:
            # Évite les doublons
            if not _is_duplicate(video, existing_videos):
                # Ajoute un timestamp de sauvegarde
                video_copy = video.copy()
                video_copy["archived_at"] = datetime.now(timezone.utc).isoformat()
                existing_videos.append(video_copy)
                added_count += 1
        
        archive["videos"] = _sort_entries(existing_videos)
        _save_archive(archive)
        
        if added_count > 0:
            print(f"✅ {added_count} vidéo(s) ajoutée(s) à l'archive")


def get_archive_stats() -> Dict:
    """Retourne les statistiques de l'archive"""
    with ARCHIVE_LOCK:
        archive = _load_archive()
        return {
            "total_articles": len(archive.get("articles", [])),
            "total_videos": len(archive.get("videos", [])),
            "last_update": datetime.now(timezone.utc).isoformat(),
        }
