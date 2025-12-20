# scraping/articles/core.py
# -*- coding: utf-8 -*-
import json
from typing import List, Dict, Tuple, Optional
from datetime import datetime, timezone

import feedparser

from ..http_state import fetch_rss_once
from .textops import to_iso, norm_text
from .media_extract import extract_author, extract_media_block
from ..filters import strict_filter
from ..keywords import UA_ANCHORS, RU_ANCHORS, NATO_TERMS



# ----------------- Fetch + parse pour un flux -----------------
def parse_feed_bytes(xml_bytes: bytes, source_name: str) -> Tuple[List[Dict], List[str]]:
    feed = feedparser.parse(xml_bytes)
    if feed.bozo:
        raise RuntimeError(f"Flux RSS mal formé (bozo=True) pour {source_name}.")

    items, hay = [], []
    for e in feed.entries:
        title = getattr(e, "title", "").strip()
        link = getattr(e, "link", "").strip()
        summary = getattr(e, "summary", "").strip()
        categories = [getattr(t, "term", "") for t in getattr(e, "tags", []) if getattr(t, "term", "")]
        dt_struct = getattr(e, "published_parsed", None) or getattr(e, "updated_parsed", None)
        published_iso = to_iso(dt_struct) if dt_struct else ""

        author = extract_author(e)
        media = extract_media_block(e)

        items.append({
            "source": source_name,
            "title": title,
            "link": link,
            "summary": summary,
            "categories": categories,
            "published": published_iso,
            "author": author or None,
            "media": media,
        })
        hay.append(norm_text(title, summary, " ".join(categories)))

    return items, hay


def deduplicate(entries: List[Dict]) -> List[Dict]:
    seen_links = set()
    seen_titles = set()
    out = []
    for e in entries:
        link = (e.get("link") or "").strip()
        title_key = norm_text(e.get("title", ""))
        if link:
            if link in seen_links:
                continue
            seen_links.add(link)
        else:
            if title_key in seen_titles:
                continue
            seen_titles.add(title_key)
        out.append(e)
    return out


def sort_by_published_desc(entries: List[Dict]) -> List[Dict]:
    return sorted(entries, key=lambda e: e.get("published") or "", reverse=True)


def within_hours(entries: List[Dict], hours: int) -> List[Dict]:
    if hours <= 0:
        return entries
    cutoff = datetime.now(timezone.utc).timestamp() - hours * 3600
    out = []
    for e in entries:
        iso = e.get("published", "")
        try:
            dt = datetime.fromisoformat(iso)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            if dt.timestamp() >= cutoff:
                out.append(e)
        except Exception:
            out.append(e)
    return out


# ----------------- Orchestration -----------------
def fetch_all(feeds: Dict[str, str], timeout: int = 8) -> Tuple[List[Dict], List[str]]:
    all_items: List[Dict] = []
    all_hay: List[str] = []
    for name, url in feeds.items():
        try:
            print(f"➡️ RSS {name} ...", flush=True)
            xml = fetch_rss_once(url, timeout=timeout)
            if xml is None:
                continue
            items, hay = parse_feed_bytes(xml, name)
            all_items.extend(items)
            all_hay.extend(hay)
        except Exception as ex:
            print(f"⚠️ RSS erreur {name}: {ex}", flush=True)
            all_items.append({
                "source": name,
                "title": f"[AVERTISSEMENT] Échec de lecture du flux: {name}",
                "link": url,
                "published": "",
                "error": str(ex),
                "media": None,
                "author": None,
                "summary": "",
                "categories": [],
            })
            all_hay.append("")
    order = sorted(range(len(all_items)), key=lambda i: all_items[i].get("published", ""), reverse=True)
    all_items = [all_items[i] for i in order]
    all_hay = [all_hay[i] for i in order]
    return all_items, all_hay


# ----------------- Façades “haute-niveau” -----------------
def run_cli(feeds: Dict[str, str], *, dump_all: bool, since_hours: int, timeout: int, include_meta: bool) -> str:
    """Retourne la **chaine JSON** à afficher (dump_all ou filtrée)."""
    entries, hay_full = fetch_all(feeds, timeout=timeout)

    if since_hours and since_hours > 0:
        entries = within_hours(entries, since_hours)
        hay_full = [norm_text(e.get("title",""), e.get("summary","")) for e in entries]

    entries = deduplicate(entries)
    entries = sort_by_published_desc(entries)

    if dump_all:
        safe = [
            {
                "source": e.get("source"),
                "title": e.get("title"),
                "link": e.get("link"),
                "published": e.get("published"),
                "media": e.get("media"),
            }
            for e in entries
        ]
        return json.dumps(safe, ensure_ascii=False, indent=2)

    if not hay_full or len(hay_full) != len(entries):
        hay_full = [norm_text(e.get("title",""), e.get("summary","")) for e in entries]

    filtered = strict_filter(entries, hay_full)

    # Gestion meta
    for it in filtered:
        meta = it.pop("_meta", {}) or {}
        if include_meta:
            if meta.get("author"):
                it["author"] = meta["author"]
            if meta.get("summary"):
                it["summary"] = meta["summary"]

    return json.dumps(filtered, ensure_ascii=False, indent=2)


# --- API helpers (réutilisables par Flask) ---
def collect_articles(
    feeds: Dict[str, str],
    since_hours: int = 24,
    include_meta: bool = True,
    q: Optional[str] = None,
    source: Optional[str] = None,
    limit: Optional[int] = 30,
    timeout: int = 8,
) -> list[dict]:
    entries, _hay = fetch_all(feeds, timeout=timeout)

    if since_hours and since_hours > 0:
        entries = within_hours(entries, since_hours)

    entries = deduplicate(entries)
    entries = sort_by_published_desc(entries)

    hay_min = [norm_text(e.get("title", "")) for e in entries]
    filtered = strict_filter(entries, hay_min)

    if source:
        filtered = [e for e in filtered if (e.get("source") == source)]

    if q:
        qn = norm_text(q)
        filtered = [e for e in filtered if qn in norm_text(e.get("title", ""))]

    if not include_meta:
        for e in filtered:
            e.pop("author", None)
            e.pop("media", None)
            e.pop("summary", None)
            e.pop("categories", None)

    if limit and limit > 0:
        filtered = filtered[:limit]

    # Déplier les meta (author/summary) vers le niveau racine si demandé
    for e in filtered:
        meta = e.pop("_meta", {}) or {}
        if include_meta:
            if meta.get("author"):
                e["author"] = meta.get("author")
            if meta.get("summary"):
                e["summary"] = meta.get("summary")

        # publishedTime en ms pour le frontend
        pub = e.get("published")
        try:
            if pub:
                dt = datetime.fromisoformat(pub)
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                e["publishedTime"] = int(dt.timestamp() * 1000)
            else:
                e["publishedTime"] = None
        except Exception:
            e["publishedTime"] = None

    # Archivage immédiat
    try:
        from scraping.archive import add_articles
        add_articles(filtered)
    except Exception as e:
        print(f"⚠️ Archivage articles (collect_articles) échoué: {e}")

    return filtered


def get_articles(
    feeds: Dict[str, str],
    query: str = "ukraine",
    since_hours: int = 24,
    include_meta: bool = True,
    timeout: int = 8,
) -> list[dict]:
    # 1) Récupération + tri + fenêtre temporelle
    entries, _hay = fetch_all(feeds, timeout=timeout)
    entries = deduplicate(sort_by_published_desc(entries))
    if since_hours and since_hours > 0:
        entries = within_hours(entries, since_hours)

    # 2) Filtre “strict” (Ukraine/Russie/OTAN) sur titre (et normalisation)
    hay_min = [norm_text(e.get("title", "")) for e in entries]
    filtered = strict_filter(entries, hay_min)

    # 3) Filtre mots-clés additionnels (keywords.py) + query libre (OR logique)
    from scraping.keywords import UA_ANCHORS, RU_ANCHORS, NATO_TERMS
    KEYWORDS = UA_ANCHORS + RU_ANCHORS + NATO_TERMS
    qn = norm_text(query) if query else ""

    def _matches_any_kw(txt: str) -> bool:
        nt = norm_text(txt)
        return any(k in nt for k in KEYWORDS) or (qn and (qn in nt))

    filtered = [
        e for e in filtered
        if _matches_any_kw(e.get("title", "")) 
        or _matches_any_kw(e.get("summary", "")) 
        or _matches_any_kw(e.get("source", ""))
    ]

    # 4) Gestion des meta optionnelles
    if not include_meta:
        for e in filtered:
            e.pop("author", None)
            e.pop("summary", None)
            e.pop("categories", None)
            # On NE touche pas à 'media' ici : il sert à construire l'image

    # 5) Image / thumbnail unifié pour le front (Vue attend 'image')
    for e in filtered:
        img = None

        # a) via bloc media normalisé (préféré)
        media = e.get("media")
        if isinstance(media, dict):
            img = media.get("url") or media.get("thumbnail") or media.get("image")

        # b) fallback: champs feedparser éventuels (si media_extract n'a rien trouvé)
        if not img and "media_thumbnail" in e:
            try:
                mt = e["media_thumbnail"]
                if isinstance(mt, list) and mt:
                    img = mt[0].get("url")
            except Exception:
                pass
        if not img and "media_content" in e:
            try:
                mc = e["media_content"]
                if isinstance(mc, list) and mc:
                    img = mc[0].get("url")
            except Exception:
                pass
        if not img and isinstance(e.get("image"), dict):
            img = e["image"].get("href") or e["image"].get("url")

        if img:
            e["image"] = img      # utilisé par le template Vue
            e.setdefault("thumb", img)  # alias pratique

    # Déplier les meta (author/summary) vers le niveau racine si demandé
    for e in filtered:
        meta = e.pop("_meta", {}) or {}
        if include_meta:
            if meta.get("author"):
                e["author"] = meta.get("author")
            if meta.get("summary"):
                e["summary"] = meta.get("summary")

        # publishedTime en ms pour le frontend
        pub = e.get("published")
        try:
            if pub:
                dt = datetime.fromisoformat(pub)
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                e["publishedTime"] = int(dt.timestamp() * 1000)
            else:
                e["publishedTime"] = None
        except Exception:
            e["publishedTime"] = None

    # Archivage immédiat
    try:
        from scraping.archive import add_articles
        add_articles(filtered)
    except Exception as e:
        print(f"⚠️ Archivage articles (get_articles) échoué: {e}")

    return filtered
