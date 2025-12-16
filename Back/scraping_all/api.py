"""Scrape articles and videos over a multi-day window and persist to archive.json."""

import argparse
from typing import Optional

from scraping.feeds import FR_FEEDS, FR_VIDEO_FEEDS
from scraping.core import get_articles
from scraping.video import get_videos
from scraping.archive import _load_archive


def scrape_window(days: int = 7, stop_after_match: Optional[int] = None, limit: int = 1000):
    hours = max(1, days) * 24
    print(f"➡️ Scraping articles for last {hours}h…")
    articles = get_articles(FR_FEEDS, query="", since_hours=hours, include_meta=True)
    print(f"✅ Articles ajoutés: {len(articles)}")

    print(f"➡️ Scraping videos for last {hours}h… (stop_after_match={'no-limit' if stop_after_match is None else stop_after_match})")
    videos = get_videos(
        FR_VIDEO_FEEDS,
        since_hours=hours,
        channel=None,
        limit=limit,
        stop_after_match=stop_after_match,
    )
    print(f"✅ Videos ajoutées: {len(videos)}")

    try:
        archive = _load_archive()
        print(f"📦 Archive maintenant: {len(archive.get('articles', []))} articles, {len(archive.get('videos', []))} vidéos")
    except Exception as exc:
        print(f"⚠️ Impossible de lire l'archive: {exc}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape les 7 derniers jours (articles + vidéos) et les archive.")
    parser.add_argument("--days", type=int, default=7, help="Fenêtre en jours (par défaut 7)")
    parser.add_argument("--stop-after", type=int, default=0, help="Arrêt après N vidéos matchantes par chaîne (0 = illimité)")
    parser.add_argument("--limit", type=int, default=1000, help="Nombre max de vidéos retournées (après agrégation)")

    args = parser.parse_args()
    stop_param = args.stop_after if args.stop_after and args.stop_after > 0 else None

    scrape_window(
        days=args.days,
        stop_after_match=stop_param,
        limit=args.limit,
    )
