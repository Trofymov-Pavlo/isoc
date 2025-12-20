# scraping/media_extract.py
# -*- coding: utf-8 -*-
from typing import List, Dict, Optional

def extract_author(e) -> str:
    author = getattr(e, "author", "") or ""
    if not author:
        authors = getattr(e, "authors", []) or []
        if authors and isinstance(authors, list):
            first = authors[0]
            if isinstance(first, dict):
                author = first.get("name", "") or first.get("email", "")
            else:
                author = str(first)
    if not author:
        ad = getattr(e, "author_detail", None)
        if isinstance(ad, dict):
            author = ad.get("name") or ad.get("email") or ""
    return author.strip()

def _pick_best_media(items: List[dict]) -> Optional[dict]:
    if not items:
        return None
    scored = []
    for it in items:
        if not isinstance(it, dict):
            continue
        url = it.get("url") or it.get("href")
        if not url:
            continue
        try: w = int(it.get("width") or 0)
        except Exception: w = 0
        try: h = int(it.get("height") or 0)
        except Exception: h = 0
        mtype = (it.get("type") or it.get("medium") or "").lower()
        scored.append((w*h or w or h or 1, {"url": url, "width": w or None, "height": h or None, "type": mtype or None}))
    if not scored:
        return None
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[0][1]

def extract_media_block(e) -> Optional[Dict[str, Optional[str]]]:
    best = None

    mc = getattr(e, "media_content", None)
    if isinstance(mc, list):
        best = _pick_best_media(mc)

    if not best:
        mt = getattr(e, "media_thumbnail", None)
        if isinstance(mt, list):
            best = _pick_best_media(mt)

    if not best:
        links = getattr(e, "links", []) or []
        imgs = []
        for lk in links:
            if not isinstance(lk, dict):
                continue
            rel = (lk.get("rel") or "").lower()
            typ = (lk.get("type") or "").lower()
            href = lk.get("href")
            if href and ("image" in typ or rel == "enclosure"):
                imgs.append({"url": href, "type": typ or None})
        if imgs:
            best = _pick_best_media(imgs)

    # media:description
    mdesc = getattr(e, "media_description", None)
    if isinstance(mdesc, list) and mdesc:
        mdesc = mdesc[0]
    if isinstance(mdesc, dict):
        mdesc = mdesc.get("value")
    if isinstance(mdesc, str):
        mdesc = mdesc.strip()
    else:
        mdesc = None

    # media:credit
    mcred = getattr(e, "media_credit", None)
    if isinstance(mcred, list) and mcred:
        first = mcred[0]
        if isinstance(first, dict):
            mcred = first.get("content") or first.get("value") or first.get("text")
        elif isinstance(first, str):
            mcred = first
    if isinstance(mcred, dict):
        mcred = mcred.get("content") or mcred.get("value") or mcred.get("text")
    if isinstance(mcred, str):
        mcred = mcred.strip()
    else:
        mcred = None

    if not best and not mdesc and not mcred:
        return None

    media = {"url": None, "width": None, "height": None, "type": None, "description": mdesc, "credit": mcred}
    if best:
        media.update(best)
    return media
