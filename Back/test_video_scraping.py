#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test rapide du scraping vidéo"""

import json
from scraping.video import get_videos

print("Lancement du test de scraping video...")
print("Ceci peut prendre 1-2 minutes...")

try:
    videos = get_videos(since_hours=0, limit=100)
    print(f"\n{len(videos)} videos recuperees par get_videos()")
    
    # Vérifier l'archive
    with open('scraping/archive.json', encoding='utf-8') as f:
        archive = json.load(f)
    
    print(f"Archive contient maintenant: {len(archive['videos'])} videos totales")
    print(f"Archive contient: {len(archive['articles'])} articles")
    
    if archive['videos']:
        print(f"\nExemple de video archivee:")
        v = archive['videos'][0]
        print(f"   Channel: {v.get('channel')}")
        print(f"   Title: {v.get('title', '')[:60]}...")
        print(f"   Link: {v.get('link')}")
    
    print("\nTEST REUSSI !")
    
except Exception as e:
    print(f"\nERREUR: {e}")
    import traceback
    traceback.print_exc()
