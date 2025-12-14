# scraping/http_state.py
# -*- coding: utf-8 -*-
import os, json, time, requests
from typing import Dict, Optional

STATE_FILE = ".rss_multi_fr_state.json"  # ETag / Last-Modified PAR URL

def new_session() -> requests.Session:
    s = requests.Session()
    s.headers.update({
        "User-Agent": "DarkTornRSS/1.0 (+contact: darktorn01@gmail.com; usage: personal, RSS-only)",
        "Accept": "application/rss+xml, application/xml;q=0.9, */*;q=0.8",
        "Accept-Language": "fr-FR,fr;q=0.9",
        "Connection": "keep-alive",
        "Referer": "https://example.org/",
    })
    return s

def load_state() -> Dict[str, Dict[str, str]]:
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    return data
        except Exception:
            pass
    return {}

def save_state(state: Dict[str, Dict[str, str]]):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

def fetch_rss_once(url: str, timeout: int = 20) -> Optional[bytes]:
    """
    Télécharge un flux RSS avec ETag/Last-Modified + retries.
    - Retourne None si 304 (Not Modified)
    - Lève une exception finale si tous les essais échouent
    """
    sess = new_session()
    state = load_state()
    url_state = state.get(url, {})

    headers = {}
    if url_state.get("etag"):
        headers["If-None-Match"] = url_state["etag"]
    if url_state.get("last_modified"):
        headers["If-Modified-Since"] = url_state["last_modified"]

    attempts = 3
    backoff = 1.5

    last_err: Exception | None = None
    for i in range(attempts):
        try:
            r = sess.get(url, headers=headers, timeout=timeout)
            if r.status_code == 304:
                return None

            if r.status_code in (429, 500, 502, 503, 504):
                last_err = requests.HTTPError(f"{r.status_code} {r.reason} on {url}")
                time.sleep(backoff * (i + 1))
                continue

            r.raise_for_status()

            etag = r.headers.get("ETag")
            last_modified = r.headers.get("Last-Modified")
            state[url] = state.get(url, {})
            if etag:
                state[url]["etag"] = etag
            if last_modified:
                state[url]["last_modified"] = last_modified
            save_state(state)

            return r.content

        except (requests.Timeout, requests.ConnectionError) as e:
            last_err = e
            time.sleep(backoff * (i + 1))
            continue
        except requests.RequestException as e:
            last_err = e
            break

    raise last_err if last_err else RuntimeError(f"Unknown error while fetching {url}")
