# scraping/videos/__init__.py
"""Module de scraping de vidéos YouTube"""

from .core import get_videos
from .feeds import YOUTUBE_CHANNELS, FR_VIDEO_FEEDS

__all__ = ['get_videos', 'YOUTUBE_CHANNELS', 'FR_VIDEO_FEEDS']
