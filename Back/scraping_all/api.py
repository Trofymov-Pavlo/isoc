"""Scrape articles and videos over a multi-day window and persist to archive.json."""

import argparse

from scraping.feeds import FR_FEEDS, FR_VIDEO_FEEDS
from scraping.core import get_articles
from scraping.video import get_videos
from scraping.archive import _load_archive


def scrape_window(days: int = 7):
    hours = max(1, days) * 24
    print(f"➡️ Scraping articles for last {hours}h…")
    articles = get_articles(FR_FEEDS, query="", since_hours=hours, include_meta=True)
    print(f"✅ Articles ajoutés: {len(articles)}")

    print(f"➡️ Scraping videos for last {hours}h… (NO LIMIT - all keywords matching)")
    videos = get_videos(
        FR_VIDEO_FEEDS,
        since_hours=hours,
        channel=None,
    )
    print(f"✅ Videos ajoutées: {len(videos)}")

    try:
        archive = _load_archive()
        print(f"📦 Archive maintenant: {len(archive.get('articles', []))} articles, {len(archive.get('videos', []))} vidéos")
    except Exception as exc:
        print(f"⚠️ Impossible de lire l'archive: {exc}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape articles + videos over N days and archive them.")
    parser.add_argument("--days", type=int, default=7, help="Time window in days (default 7)")

    args = parser.parse_args()

    scrape_window(
        days=args.days,
    )
