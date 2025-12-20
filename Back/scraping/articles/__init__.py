# scraping/articles/__init__.py
"""Module de scraping d'articles RSS"""

from .core import get_articles
from .feeds import FR_FEEDS

__all__ = ['get_articles', 'FR_FEEDS']
