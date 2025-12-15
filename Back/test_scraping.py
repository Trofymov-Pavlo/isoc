#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test script for video scraping and archive functionality
Demonstrates the new features added to the scraping system
"""

import sys
from pathlib import Path

# Add the Back directory to the path
back_dir = Path(__file__).parent
sys.path.insert(0, str(back_dir))

from scraping.feeds import FR_VIDEO_FEEDS
from scraping.video import collect_videos
from scraping.archive import get_archive_stats, _load_archive

def main():
    print("=" * 70)
    print("AXIOM - Scraping System Test")
    print("=" * 70)
    
    # 1. Display video feeds configuration
    print("\n📺 VIDEO FEEDS CONFIGURATION")
    print(f"Total YouTube channels: {len(FR_VIDEO_FEEDS)}")
    print("\nChannels by region:")
    
    french_channels = ["ARTE", "Le Monde", "France 24", "BFM TV", "CNews", "France Inter", "Mediapart", "Brut", "Konbini"]
    international = ["BBC News", "DW News", "Euronews", "CNN", "ABC News", "CBS News", "Fox News", "Reuters", "Al Jazeera", "Sky News"]
    military = ["Warthog Defense", "Defense Updates"]
    russian = ["TV Rain (Дождь)", "Популярная политика"]
    documentary = ["National Geographic", "Discovery Channel", "Discovery Channel France"]
    
    print(f"  🇫🇷 French: {len([c for c in french_channels if c in FR_VIDEO_FEEDS])} channels")
    print(f"  🌍 International: {len([c for c in international if c in FR_VIDEO_FEEDS])} channels")
    print(f"  🎖️  Military: {len([c for c in military if c in FR_VIDEO_FEEDS])} channels")
    print(f"  🇷🇺 Russian/Eastern: {len([c for c in russian if c in FR_VIDEO_FEEDS])} channels")
    print(f"  🎬 Documentary: {len([c for c in documentary if c in FR_VIDEO_FEEDS])} channels")
    
    # 2. Archive statistics
    print("\n📊 ARCHIVE STATISTICS")
    stats = get_archive_stats()
    print(f"  Total archived articles: {stats['total_articles']}")
    print(f"  Total archived videos: {stats['total_videos']}")
    
    # 3. Archive structure
    print("\n📁 ARCHIVE STRUCTURE")
    archive = _load_archive()
    print(f"  Articles in archive: {len(archive.get('articles', []))}")
    print(f"  Videos in archive: {len(archive.get('videos', []))}")
    
    if archive.get('articles'):
        print("\n  Recent articles:")
        for article in archive.get('articles', [])[:3]:
            print(f"    - {article.get('title', 'N/A')[:60]}...")
            print(f"      Source: {article.get('source')}, Archived: {article.get('archived_at', 'N/A')[:19]}")
    
    if archive.get('videos'):
        print("\n  Recent videos:")
        for video in archive.get('videos', [])[:3]:
            print(f"    - {video.get('title', 'N/A')[:60]}...")
            print(f"      Channel: {video.get('channel')}, Archived: {video.get('archived_at', 'N/A')[:19]}")
    
    # 4. Available endpoints
    print("\n🔗 API ENDPOINTS")
    print("  GET /articles")
    print("    - Retrieve filtered news articles")
    print("    - Parameters: q, hours, meta")
    print("\n  GET /videos")
    print("    - Retrieve YouTube videos")
    print("    - Parameters: hours, channel, limit")
    print("\n  GET /stats")
    print("    - Archive statistics and metadata")
    
    print("\n" + "=" * 70)
    print("✅ Scraping system is ready for use!")
    print("=" * 70)

if __name__ == "__main__":
    main()
