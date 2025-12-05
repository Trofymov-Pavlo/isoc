# -*- coding: utf-8 -*-
"""
RSS-only (médias FR), usage personnel.
- UA explicite + contact (pseudo OK si contact valide)
- If-Modified-Since / ETag par flux
- Pas d'HTML, pas de contournement
- Filtrage strict Ukraine–Russie–OTAN (noms propres) pour la sélection, mais on NE renvoie PAS les matched_terms
- Déduplication inter-sources, tri antéchronologique
- Retourne toujours le bloc media (url + description + credit si présents)
- Option --include-meta pour inclure author/summary (si présents)
"""

import os
import re
import json
import time
import argparse
from typing import List, Dict, Tuple, Optional
from datetime import datetime, timezone
import requests
import feedparser

# ----------------- Flux RSS (France uniquement) -----------------
FR_FEEDS = {
    # Généralistes nationaux
    "Le Monde (en continu)": "https://www.lemonde.fr/rss/en_continu.xml",
    "Le Figaro (actualités)": "https://www.lefigaro.fr/rss/figaro_actualites.xml",
    "Franceinfo (fil)": "https://www.francetvinfo.fr/titres.rss",
    "Libération (à la une)": "https://www.liberation.fr/arc/outboundfeeds/rss-all/",
    "Les Echos (monde)": "https://www.lesechos.fr/rss/monde.xml",
    "Le Parisien (à la une)": "https://www.leparisien.fr/une/rss.xml",
    # Presse régionale / autres
    "Ouest-France (à la une)": "https://www.ouest-france.fr/rss-en-continu.xml",

        # --- France (nationaux) ---
    "France 24 (France)": "https://www.france24.com/fr/france/rss",
    "France 24 (Europe)": "https://www.france24.com/fr/europe/rss",
    "France 24 (Monde)": "https://www.france24.com/fr/monde/rss",

    "RFI (France)": "https://www.rfi.fr/fr/france/rss",
    "RFI (Europe)": "https://www.rfi.fr/fr/europe/rss",
    "RFI (Monde)": "https://www.rfi.fr/fr/flux-de-rfi/rss",  # global

    "La Croix (Monde)": "https://www.la-croix.com/feed/rss/monde.xml",
    "La Croix (France)": "https://www.la-croix.com/feed/rss/france.xml",

    "Sud Ouest (international)": "https://www.sudouest.fr/rss.xml",
    "20 Minutes (monde)": "https://www.20minutes.fr/feeds/rss-monde.xml",
    "20 Minutes (politique)": "https://www.20minutes.fr/feeds/rss-politique.xml",

    "BFM TV (monde)": "https://rmc.bfmtv.com/rss/info/monde/",
    "BFM TV (france)": "https://rmc.bfmtv.com/rss/info/france/",

    "RTL (faits divers)": "https://www.rtl.fr/rss/actus.xml",
    "RTL (international)": "https://www.rtl.fr/rss/actus/international.xml",

    "L’Opinion (monde)": "https://www.lopinion.fr/rss.xml",
    "Challenges (monde)": "https://www.challenges.fr/rss.xml",

    # --- Presse régionale France (pertinent Ukraine / Europe selon dépêches AFP) ---
    "La Dépêche (monde)": "https://www.ladepeche.fr/rss.xml",
    "Le Télégramme (monde)": "https://www.letelegramme.fr/monde/rss.xml",
    "La Voix du Nord (monde)": "https://www.lavoixdunord.fr/rss",
    "Nice Matin (monde)": "https://www.nicematin.com/monde/rss.xml",
    "La Provence (monde)": "https://www.laprovence.com/rss/monde",

}

STATE_FILE = ".rss_multi_fr_state.json"  # ETag / Last-Modified PAR URL

# ----------------- Mots-clés: ultra-propres (noms propres) -----------------
UA_ANCHORS = [
    "ukraine","ukrainien","ukrainienne","ukrainiens",
    "zelensky","zelenskyy","volodymyr zelensky",
    "zaluzhny","zaloujny","syrskyi","syrsky","oleksandr syrskyi","budanov","kyrylo budanov",
    "kyiv","kiev","kharkiv","kherson","sumy","tchernihiv","chernihiv","mykolaiv","nikolaev",
    "odessa","odesa","dnipro","dniepr",
    "donbass","donbas","donetsk","luhansk","lugansk",
    "bakhmut","bahmut","avdiivka","kramatorsk","sloviansk","kupiansk","koupiansk",
    "svatove","izium","izioum","toretsk","vuhledar","lyman","kostyantynivka",
    "zaporizhzhia","zaporijia","enerhodar","kakhovka","nova kakhovka",
    "crimée","crimea","sevastopol","sebastopol","simferopol","pont de kertch","kerch","kerch bridge",
]
RU_ANCHORS = [
    "russie","russe","russes","moscou","kremlin",
    "poutine","vladimir poutine","putin","vladimir putin",
    "shoigu","choïgou","sergei shoigu","lavrov","prigojine","prigozhin","kadyrov",
    "wagner","groupe wagner",
]
NATO_TERMS = ["otan","nato"]

# ----------------- HTTP session: UA explicite + contact -----------------
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
    - Lève une exception finale si tous les essais échouent (fetch_all s'en charge)
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
            # 304: cache OK
            if r.status_code == 304:
                return None

            # 429 / 5xx : on retente (dans la limite des attempts)
            if r.status_code in (429, 500, 502, 503, 504):
                last_err = requests.HTTPError(f"{r.status_code} {r.reason} on {url}")
                # backoff léger
                time.sleep(backoff * (i + 1))
                continue

            r.raise_for_status()

            # MAJ ETag / Last-Modified
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
            # autres erreurs HTTP (4xx, etc.) -> on ne réessaie pas sauf 429/5xx gérées plus haut
            last_err = e
            break

    # Si on est ici, tout a échoué : laisser fetch_all() gérer l'avertissement
    raise last_err if last_err else RuntimeError(f"Unknown error while fetching {url}")


# ----------------- Normalisation / matching -----------------
def to_iso(dt_struct) -> str:
    if not dt_struct:
        return ""
    ts = int(time.mktime(dt_struct))
    return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()

TRANSLIT_MAP = str.maketrans(
    "àâäçéèêëîïôöùûüÿœæÀÂÄÇÉÈÊËÎÏÔÖÙÛÜŸŒÆ",
    "aaaceeeeii oouuuyoeAAACEEEEIIOOUUUYOE".replace(" ", "")
)

def norm_text(*parts: str) -> str:
    return " ".join([p or "" for p in parts]).translate(TRANSLIT_MAP).lower()

def compile_regex(words: List[str]) -> List[tuple[str, re.Pattern]]:
    regs: List[Tuple[str, re.Pattern]] = []
    for w in sorted(set(w.strip() for w in words if w.strip())):
        w_norm = norm_text(w)
        regs.append((w, re.compile(r"\b" + re.escape(w_norm) + r"\b")))
    return regs

UA_RE = compile_regex(UA_ANCHORS)
RU_RE = compile_regex(RU_ANCHORS)
NATO_RE = compile_regex(NATO_TERMS)

def match_any(hay: str, regs: List[tuple[str, re.Pattern]]) -> bool:
    # on ne veut plus renvoyer les termes, juste un bool pour filtrer
    for _, rgx in regs:
        if rgx.search(hay):
            return True
    return False

# ----------------- Extract helpers (author / media) -----------------
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
        try:
            w = int(it.get("width") or 0)
        except Exception:
            w = 0
        try:
            h = int(it.get("height") or 0)
        except Exception:
            h = 0
        mtype = (it.get("type") or it.get("medium") or "").lower()
        scored.append((w*h or w or h or 1, {"url": url, "width": w or None, "height": h or None, "type": mtype or None}))
    if not scored:
        return None
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[0][1]

def extract_media_block(e) -> Optional[Dict[str, Optional[str]]]:
    """
    Essaie d'attraper:
      - url (+ width/height/type) depuis media:content / media:thumbnail / enclosures
      - description depuis media:description
      - credit depuis media:credit (souvent texte "Auteur / Agence")
    """
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
        # parfois liste d’objets
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
        # feedparser peut renvoyer liste de dicts/strings
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
        media = extract_media_block(e)  # <-- url + description + credit

        items.append({
            "source": source_name,
            "title": title,
            "link": link,
            "summary": summary,          # ⚠️ usage perso; éviter republication publique
            "categories": categories,    # idem
            "published": published_iso,
            "author": author or None,
            "media": media,              # dict ou None
        })
        hay.append(norm_text(title, summary, " ".join(categories)))

    return items, hay

# ----------------- Merge / tri / filtre -----------------
def passes_filter(hay: str) -> bool:
    # garder si on voit au moins 1 terme Ukraine.
    if match_any(hay, UA_RE):
        return True
    # (pas de "russie/otan seuls" sans Ukraine)
    return False

def strict_filter(entries: List[Dict], haystacks: List[str]) -> List[Dict]:
    out = []
    for entry, hay in zip(entries, haystacks):
        if not passes_filter(hay):
            continue
        # On renvoie sans matched_terms (demande utilisateur)
        item = {
            "source": entry["source"],
            "title": entry["title"],
            "link": entry["link"],
            "published": entry["published"],
            "media": entry.get("media"),  # contient url/description/credit si présents
        }
        # _meta gardera author/summary si on l’active plus bas
        item["_meta"] = {"author": entry.get("author"), "summary": entry.get("summary")}
        out.append(item)
    return out

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
def fetch_all(feeds: Dict[str, str], timeout: int = 20) -> Tuple[List[Dict], List[str]]:
    all_items: List[Dict] = []
    all_hay: List[str] = []
    for name, url in feeds.items():
        try:
            xml = fetch_rss_once(url, timeout=timeout)
            if xml is None:
                continue
            items, hay = parse_feed_bytes(xml, name)
            all_items.extend(items)
            all_hay.extend(hay)
        except Exception as ex:
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
    # tri rapide par date (desc)
    order = sorted(range(len(all_items)), key=lambda i: all_items[i].get("published", ""), reverse=True)
    all_items = [all_items[i] for i in order]
    all_hay = [all_hay[i] for i in order]
    return all_items, all_hay

# ----------------- CLI -----------------
def main():
    ap = argparse.ArgumentParser(description="Agrégateur RSS FR (personnel, compliant) + filtre Ukraine/Russie/OTAN.")
    ap.add_argument("--dump-all", dest="dump_all", action="store_true",
                    help="Affiche toutes les entrées (source, titre, lien, date) sans filtrage (usage perso; éviter la republication).")
    ap.add_argument("--since-hours", type=int, default=0,
                    help="Ne conserver que les articles publiés dans les N dernières heures (0 = désactivé).")
    ap.add_argument("--timeout", type=int, default=20, help="Timeout HTTP en secondes (par requête).")
    ap.add_argument("--include-meta", action="store_true",
                    help="Inclut author/summary (si présents) dans la sortie filtrée.")
    args = ap.parse_args()

    entries, hay_full = fetch_all(FR_FEEDS, timeout=args.timeout)

    if args.since_hours and args.since_hours > 0:
        entries = within_hours(entries, args.since_hours)
        hay_full = [norm_text(e.get("title",""), e.get("summary","")) for e in entries]

    entries = deduplicate(entries)
    entries = sort_by_published_desc(entries)

    if args.dump_all:
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
        print(json.dumps(safe, ensure_ascii=False, indent=2))
        return

    if not hay_full or len(hay_full) != len(entries):
        hay_full = [norm_text(e.get("title",""), e.get("summary","")) for e in entries]

    filtered = strict_filter(entries, hay_full)

    # Gestion meta
    for it in filtered:
        meta = it.pop("_meta", {}) or {}
        if args.include_meta:
            if meta.get("author"):
                it["author"] = meta["author"]
            if meta.get("summary"):
                it["summary"] = meta["summary"]

    print(json.dumps(filtered, ensure_ascii=False, indent=2))

# --- API helper (à appeler depuis Flask) ---
def collect_articles(
    since_hours: int = 36,
    include_meta: bool = True,
    q: str | None = None,
    source: str | None = None,
    limit: int | None = 30,
) -> list[dict]:
    """
    Retourne une liste d’articles filtrés (Ukraine/Russie/OTAN).
    - since_hours: fenêtre temporelle en heures (0 = pas de filtre)
    - include_meta: inclut meta (auteur, media url/description/crédit) si dispo dans le RSS
    - q: filtre additionnel “contient q” sur le titre (optionnel)
    - source: ne garder que cette source (exacte, cf. clés FR_FEEDS)
    - limit: tronque le résultat à N items
    """
    entries, _hay = fetch_all(FR_FEEDS, timeout=20)

    # fenêtre temporelle
    if since_hours and since_hours > 0:
        entries = within_hours(entries, since_hours)

    # dédup + tri
    entries = deduplicate(entries)
    entries = sort_by_published_desc(entries)

    # filtrage thématique (Ukraine/Russie/OTAN)
    hay_min = [norm_text(e.get("title", "")) for e in entries]
    filtered = strict_filter(entries, hay_min)

    # filtre source optionnel
    if source:
        filtered = [e for e in filtered if (e.get("source") == source)]

    # filtre texte optionnel sur le titre
    if q:
        qn = norm_text(q)
        filtered = [e for e in filtered if qn in norm_text(e.get("title", ""))]

    # drop méta si demandé
    if not include_meta:
        for e in filtered:
            e.pop("author", None)
            e.pop("media", None)        # media: {url,width,height,description,credit}
            e.pop("summary", None)
            e.pop("categories", None)

    # limite
    if limit and limit > 0:
        filtered = filtered[:limit]

    return filtered


if __name__ == "__main__":
    main()


# --- Helper pour l'API Flask ---
def get_articles(query: str = "ukraine", since_hours: int = 36,include_meta: bool = True):
    """Retourne une liste d'articles filtrés, prête pour JSON."""
    from datetime import timezone, datetime
    entries, _hay = fetch_all(FR_FEEDS, timeout=20)
    entries = deduplicate(sort_by_published_desc(entries))
    if since_hours and since_hours > 0:
        entries = within_hours(entries, since_hours)
    # filtre strict (on ne republie pas summary/cats)
    hay_min = [norm_text(e.get("title","")) for e in entries]
    filtered = strict_filter(entries, hay_min)

    # (optionnel) re-filtre par mot-clé supplémentaire q (très simple)
    qn = norm_text(query) if query else ""
    if qn:
        filtered = [e for e in filtered if qn in norm_text(e.get("title","")) or qn in norm_text(e.get("source",""))]

    # si include_meta=False, on enlève media/author
    if not include_meta:
        for e in filtered:
            e.pop("media", None)
            e.pop("author", None)
            e.pop("categories", None)
    return filtered
