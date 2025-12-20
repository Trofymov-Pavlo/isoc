"""
Scraping API - Command-line tool to scrape articles and videos.
Usage: python -m scraping.api [--days N] [--hours H]
Default: scrapes last 24 hours and adds to archive.json
"""

import argparse
import sys
import io

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from scraping.feeds import FR_FEEDS, FR_VIDEO_FEEDS
from scraping.core import get_articles
from scraping.video import get_videos
from scraping.archive import _load_archive


def scrape_window(hours: int = 24):
    """
    Scrape articles and videos for the last N hours and add them to archive.json.
    The archive module (archive.py) handles deduplication and appending.
    """
    print(f"➡️ Scraping articles for last {hours}h…")
    articles = get_articles(FR_FEEDS, query="", since_hours=hours, include_meta=True)
    print(f"✅ {len(articles)} article(s) scraped and added to archive")

    print(f"➡️ Scraping videos for last {hours}h…")
    videos = get_videos(
        FR_VIDEO_FEEDS,
        since_hours=hours,
        channel=None,
    )
    print(f"✅ {len(videos)} video(s) scraped and added to archive")

    try:
        archive = _load_archive()
        print(f"📦 Archive now contains: {len(archive.get('articles', []))} articles, {len(archive.get('videos', []))} videos")
    except Exception as exc:
        print(f"⚠️ Unable to read archive: {exc}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Scrape articles and videos and add them to archive.json",
        epilog="Examples:\n"
               "  python -m scraping.api              # Scrape last 24 hours (default)\n"
               "  python -m scraping.api --hours 48   # Scrape last 48 hours\n"
               "  python -m scraping.api --days 7     # Scrape last 7 days\n",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--days", type=int, help="Time window in days")
    parser.add_argument("--hours", type=int, help="Time window in hours (overrides --days)")

    args = parser.parse_args()

    # Determine hours to scrape
    if args.hours is not None:
        hours_to_scrape = max(1, args.hours)
    elif args.days is not None:
        hours_to_scrape = max(1, args.days) * 24
    else:
        # Default: 24 hours
        hours_to_scrape = 24

    scrape_window(hours=hours_to_scrape)
