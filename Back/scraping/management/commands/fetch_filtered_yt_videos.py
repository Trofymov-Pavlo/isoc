# -*- coding: utf-8 -*-
import os
import time
import json
import requests
from django.core.management.base import BaseCommand, CommandError
from scraping.keywords import UA_ANCHORS, RU_ANCHORS, NATO_TERMS

API_KEY = os.environ.get("YT_API_KEY", "AIzaSyDnEmmnbH3lsMtNbm-rMITQf-3bO-RQZv4")
YTB_API = "https://www.googleapis.com/youtube/v3"

def get_uploads_playlist_id(channel_id):
    r = requests.get(f"{YTB_API}/channels", params={
        "part": "contentDetails",
        "id": channel_id,
        "key": API_KEY
    })
    r.raise_for_status()
    items = r.json().get("items", [])
    if not items:
        raise CommandError("Channel introuvable")
    return items[0]["contentDetails"]["relatedPlaylists"]["uploads"]

def iter_all_videos(uploads_playlist_id):
    params = {
        "part": "snippet,contentDetails",
        "playlistId": uploads_playlist_id,
        "maxResults": 50,
        "key": API_KEY,
    }
    while True:
        r = requests.get(f"{YTB_API}/playlistItems", params=params)
        r.raise_for_status()
        data = r.json()

        for it in data.get("items", []):
            title = it["snippet"]["title"]
            yield {
                "videoId": it["contentDetails"]["videoId"],
                "title": title,
                "publishedAt": it["contentDetails"].get("videoPublishedAt") or it["snippet"].get("publishedAt"),
                "thumbnail": (it["snippet"].get("thumbnails", {}).get("high")
                              or it["snippet"].get("thumbnails", {}).get("default") or {}).get("url"),
                "url": f"https://www.youtube.com/watch?v={it['contentDetails']['videoId']}"
            }

        token = data.get("nextPageToken")
        if not token:
            break

        params["pageToken"] = token
        time.sleep(0.05)

def match_keywords(title: str) -> bool:
    txt = title.lower()
    keywords = UA_ANCHORS + RU_ANCHORS + NATO_TERMS
    return any(k.lower() in txt for k in keywords)

class Command(BaseCommand):
    help = "Récupère toutes les vidéos YouTube d'une chaîne et filtre selon les mots-clés Ukraine/Russie/OTAN."

    def add_arguments(self, parser):
        parser.add_argument("--channel-id", required=True)

    def handle(self, *args, **opts):
        if not API_KEY:
            raise CommandError("YT_API_KEY non défini.")

        channel_id = opts["channel_id"]
        uploads = get_uploads_playlist_id(channel_id)

        count_total = 0
        count_match = 0

        for v in iter_all_videos(uploads):
            count_total += 1
            if match_keywords(v["title"]):
                count_match += 1
                self.stdout.write(json.dumps(v, ensure_ascii=False))

        self.stdout.write(self.style.SUCCESS(
            f"{count_match}/{count_total} vidéos correspondent aux mots-clés."
        ))
