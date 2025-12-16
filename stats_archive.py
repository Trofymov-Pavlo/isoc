#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Stats de l'archive en temps réel
"""

import json
from pathlib import Path
from datetime import datetime, timezone

ARCHIVE_PATH = Path(__file__).parent / 'Front' / 'public' / 'archive.json'

def main():
    with open(ARCHIVE_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    articles = data.get('articles', [])
    videos = data.get('videos', [])
    
    print("=" * 60)
    print("STATISTIQUES DE L'ARCHIVE")
    print("=" * 60)
    print(f"\nFichier: {ARCHIVE_PATH}")
    print(f"Taille: {ARCHIVE_PATH.stat().st_size / 1024:.1f} Ko")
    
    print(f"\n📰 Articles: {len(articles)}")
    print(f"🎬 Vidéos: {len(videos)}")
    print(f"📊 Total: {len(articles) + len(videos)}")
    
    # Stats vidéos par channel
    channels = {}
    for v in videos:
        ch = v.get('channel', 'Unknown')
        channels[ch] = channels.get(ch, 0) + 1
    
    print(f"\n🎥 Vidéos par channel ({len(channels)} channels):")
    for ch, count in sorted(channels.items(), key=lambda x: -x[1])[:10]:
        print(f"   {ch:25s} : {count:3d} vidéos")
    
    # Stats articles par source
    sources = {}
    for a in articles:
        src = a.get('source', 'Unknown')
        sources[src] = sources.get(src, 0) + 1
    
    print(f"\n📰 Articles par source (top 10):")
    for src, count in sorted(sources.items(), key=lambda x: -x[1])[:10]:
        print(f"   {src:25s} : {count:3d} articles")
    
    # Stats temporelles
    now = datetime.now(timezone.utc).timestamp() * 1000
    cutoff_24h = now - (24 * 60 * 60 * 1000)
    cutoff_48h = now - (48 * 60 * 60 * 1000)
    cutoff_7d = now - (7 * 24 * 60 * 60 * 1000)
    
    videos_24h = sum(1 for v in videos if (v.get('publishedTime') or 0) >= cutoff_24h)
    videos_48h = sum(1 for v in videos if (v.get('publishedTime') or 0) >= cutoff_48h)
    videos_7d = sum(1 for v in videos if (v.get('publishedTime') or 0) >= cutoff_7d)
    
    articles_24h = sum(1 for a in articles if (a.get('publishedTime') or 0) >= cutoff_24h)
    articles_48h = sum(1 for a in articles if (a.get('publishedTime') or 0) >= cutoff_48h)
    articles_7d = sum(1 for a in articles if (a.get('publishedTime') or 0) >= cutoff_7d)
    
    print(f"\n⏰ Contenu récent:")
    print(f"   Dernières 24h : {articles_24h:3d} articles, {videos_24h:3d} vidéos")
    print(f"   Dernières 48h : {articles_48h:3d} articles, {videos_48h:3d} vidéos")
    print(f"   Derniers 7j   : {articles_7d:3d} articles, {videos_7d:3d} vidéos")
    
    # Exemples récents
    recent_videos = [v for v in videos if (v.get('publishedTime') or 0) >= cutoff_24h]
    recent_articles = [a for a in articles if (a.get('publishedTime') or 0) >= cutoff_24h]
    
    if recent_videos:
        print(f"\n🎬 Vidéos récentes (<24h) - exemples:")
        for v in sorted(recent_videos, key=lambda x: x.get('publishedTime', 0), reverse=True)[:5]:
            print(f"   {v.get('channel', 'Unknown'):20s} | {v.get('title', '')[:50]}")
    
    if recent_articles:
        print(f"\n📰 Articles récents (<24h) - exemples:")
        for a in sorted(recent_articles, key=lambda x: x.get('publishedTime', 0), reverse=True)[:5]:
            print(f"   {a.get('source', 'Unknown'):20s} | {a.get('title', '')[:50]}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
