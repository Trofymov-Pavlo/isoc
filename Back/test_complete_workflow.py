#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test complet du workflow:
1. Vérifier le chemin de l'archive
2. Tester le scraping articles
3. Tester le scraping vidéos
4. Vérifier que tout est bien ajouté à l'archive unique
"""

import json
from pathlib import Path
from scraping.archive import ARCHIVE_FILE, get_archive_stats

def main():
    print("=" * 60)
    print("TEST COMPLET DU WORKFLOW")
    print("=" * 60)
    
    # 1. Vérifier le chemin de l'archive
    print(f"\n1. Chemin de l'archive:")
    print(f"   {ARCHIVE_FILE}")
    print(f"   Existe: {ARCHIVE_FILE.exists()}")
    
    if not ARCHIVE_FILE.exists():
        print("   ❌ L'archive n'existe pas!")
        return
    
    # 2. Stats initiales
    print(f"\n2. État initial de l'archive:")
    stats = get_archive_stats()
    print(f"   Articles: {stats['total_articles']}")
    print(f"   Vidéos: {stats['total_videos']}")
    initial_articles = stats['total_articles']
    initial_videos = stats['total_videos']
    
    # 3. Tester le scraping articles (dernières 24h, max 5)
    print(f"\n3. Test scraping articles (24h, max 5)...")
    try:
        from scraping.core import get_articles
        from scraping.feeds import FR_FEEDS
        
        articles = get_articles(FR_FEEDS, query="", since_hours=24, include_meta=True)
        print(f"   ✅ {len(articles)} articles récupérés")
        if articles:
            print(f"   Exemple: {articles[0].get('title', '')[:60]}...")
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
    
    # 4. Tester le scraping vidéos (dernières 24h, TOUTES les vidéos matchantes)
    print(f"\n4. Test scraping vidéos (24h, SANS LIMITE)...")
    try:
        from scraping.video import get_videos
        
        videos = get_videos(since_hours=24)
        print(f"   ✅ {len(videos)} vidéos récupérées (TOUTES celles qui matchent)")
        if videos:
            print(f"   Exemple: {videos[0].get('channel')} - {videos[0].get('title', '')[:60]}...")
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
    
    # 5. Vérifier l'archive après scraping
    print(f"\n5. État final de l'archive:")
    stats = get_archive_stats()
    print(f"   Articles: {stats['total_articles']} (avant: {initial_articles})")
    print(f"   Vidéos: {stats['total_videos']} (avant: {initial_videos})")
    
    # 6. Vérifier que c'est bien le même fichier que le front va lire
    frontend_path = Path(__file__).parent.parent / 'Front' / 'public' / 'archive.json'
    print(f"\n6. Vérification du chemin frontend:")
    print(f"   Backend ARCHIVE_FILE: {ARCHIVE_FILE}")
    print(f"   Frontend public path: {frontend_path}")
    print(f"   Même fichier: {ARCHIVE_FILE.resolve() == frontend_path.resolve()}")
    
    # 7. Vérifier le contenu
    print(f"\n7. Vérification du contenu de l'archive:")
    try:
        with open(ARCHIVE_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        articles_data = data.get('articles', [])
        videos_data = data.get('videos', [])
        
        print(f"   Structure JSON: OK")
        print(f"   Clé 'articles': {len(articles_data)} entrées")
        print(f"   Clé 'videos': {len(videos_data)} entrées")
        
        # Vérifier les champs requis
        if articles_data:
            a = articles_data[0]
            required = ['title', 'link', 'published', 'publishedTime']
            missing = [f for f in required if f not in a]
            if missing:
                print(f"   ⚠️ Champs manquants dans articles: {missing}")
            else:
                print(f"   ✅ Articles ont tous les champs requis")
        
        if videos_data:
            v = videos_data[0]
            required = ['channel', 'title', 'link', 'published', 'publishedTime', 'thumbnail']
            missing = [f for f in required if f not in v]
            if missing:
                print(f"   ⚠️ Champs manquants dans videos: {missing}")
            else:
                print(f"   ✅ Vidéos ont tous les champs requis")
        
        # Channels
        if videos_data:
            channels = set(v.get('channel', 'unknown') for v in videos_data)
            print(f"   Channels présents: {len(channels)}")
            print(f"   Exemples: {', '.join(sorted(channels)[:5])}")
        
    except Exception as e:
        print(f"   ❌ Erreur lecture: {e}")
    
    print("\n" + "=" * 60)
    print("✅ TEST TERMINÉ")
    print("=" * 60)

if __name__ == "__main__":
    main()
