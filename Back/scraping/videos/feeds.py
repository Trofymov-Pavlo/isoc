# scraping/videos/feeds.py
# -*- coding: utf-8 -*-
"""
Configuration des flux YouTube pour le scraping de vidéos
"""

# YouTube Channel IDs
YOUTUBE_CHANNELS = {
    # --- Français ---
    "ARTE": "UCwI-JbGNsojunnHbFAc0M4Q",
    "Le Monde": "UCYpRDnhk5H8h16jpS84uqsA",
    "France 24": "UCCCPCZNChQdGa9EkATeye4g",
    "BFM TV": "UCXwDLMDV86ldKoFVc_g8P0g",
    "CNews": "UCXKJrYczY2_fJEZgFPGY0HQ",
    "France Inter": "UCJldRgT_D7Am-ErRHQZ90uw",
    "Mediapart": "UCdnaDhU-LDQrIEEmSIfq0-Q",
    "Brut": "UCSKdvgqdnj72_SLggp7BDTg",
    "Konbini": "UCHQda5vLxrH0Ff0I0kMq4zw",
    
    # --- International anglophone ---
    "BBC News": "UC16niRr50-MSBwiO3YDb3RA",
    "DW News": "UCknLrEdhRcp1aegoMqRaCZg",
    "Euronews": "UCW2QcKZiU8aUGg4yxCIditg",
    "CNN": "UCupvZG-5ko_eiXAupbDfxWw",
    "ABC News": "UCBi2mrWuNuyYy4gbM6fU18Q",
    "CBS News": "UC8p1vwvWtl6T73JiExfWs1g",
    "Fox News": "UCXIJgqnII2ZOINSWNOGFThA",
    "Associated Press": "UC52X5wxOL_s5yw0dQk7NtgA",
    "Al Jazeera English": "UCNye-wNBqNL5ZzHSJj3l8Bg",
    "Reuters": "UChqUTb7kYRX8-EiaN3XFrSQ",
    "Sky News": "UCoMdktPbSTixAyNGwb-UYkQ",
    
    # --- Military/Defense ---
    "Warthog Defense": "UC2JaXg63L_VqvXN4SwF4zOQ",
    "Defense Updates": "UCKNCbBWiMiXBVXUmUuu_dsQ",
    
    # --- Documentary/Nature ---
    "National Geographic": "UCpVm7bg6pXKo1Pr6k5kxG9A",
    "Discovery Channel": "UCqOoboPm3uhY_YXhvhmL-WA",
    "Discovery Channel France": "UCJ3uq_dgtGdfScO21KU08wg",
}

# Pour compatibilité avec l'ancien format RSS
FR_VIDEO_FEEDS = {
    name: f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    for name, channel_id in YOUTUBE_CHANNELS.items()
}
