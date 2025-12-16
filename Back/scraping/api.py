# api.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
from threading import Lock
import time

from scraping.core import get_articles
from scraping.feeds import FR_FEEDS, FR_VIDEO_FEEDS
from scraping.video import get_videos
from scraping.archive import add_articles, add_videos, get_archive_stats, _load_archive

# -----------------------------
# Initialisation Flask
app = Flask(__name__)
CORS(app)

# -----------------------------
# Cache + planification (15 min)
# -----------------------------
CACHE_TTL = 900  # 15 minutes en secondes
CACHE = {}       # key -> {"ts": float, "data": [...]}
LOCK = Lock()
scheduler = BackgroundScheduler(daemon=True)

def _cache_key_articles(q: str, hours: int, include_meta: bool) -> str:
    return f"articles|q={q}|h={hours}|m={1 if include_meta else 0}"

def _cache_key_videos(channel: str, hours: int, limit: int) -> str:
    return f"videos|c={channel or 'all'}|h={hours}|l={limit}"

def _get_cache(key: str):
    with LOCK:
        it = CACHE.get(key)
        if not it:
            return None
        if time.time() - it["ts"] <= CACHE_TTL:
            return it["data"]
        # expiré
        return None

def _set_cache(key: str, data):
    with LOCK:
        CACHE[key] = {"ts": time.time(), "data": data}

def _refresh_combo(q: str, hours: int, include_meta: bool):
    # Scrape et alimente le cache pour 1 combinaison
    data = get_articles(FR_FEEDS, query=q, since_hours=hours, include_meta=include_meta)
    _set_cache(_cache_key_articles(q, hours, include_meta), data)

def _refresh_all():
    """
    Liste des combinaisons à rafraîchir. Ajoute ici celles dont tu as besoin.
    """
    combos = [
        ("",24,True),  # Query vide = utilise uniquement les filtres keywords.py
    ]
    print("🔄 Refresh scraping (scheduled)…")
    for q, h, m in combos:
        try:
            _refresh_combo(q, h, m)
        except Exception as e:
            print("⚠️ refresh error:", q, h, m, e)
    
    # Scrape et met en cache (archivage maintenant géré dans core/video)
    try:
        articles = get_articles(FR_FEEDS, query="", since_hours=24, include_meta=True)  # Query vide
        if articles:
            _set_cache(_cache_key_articles("", 24, True), articles)
    except Exception as e:
        print("⚠️ Erreur rafraîchissement articles:", e)
    
    try:
        videos = get_videos(FR_VIDEO_FEEDS, since_hours=0, limit=50)
        if videos:
            _set_cache(_cache_key_videos(None, 0, 50), videos)
    except Exception as e:
        print("⚠️ Erreur rafraîchissement vidéos:", e)
    
    print("✅ Refresh OK")

# Flask 3 : before_first_request supprimé → on initialise manuellement
_scheduler_started = False

def start_scheduler_once():
    global _scheduler_started
    if _scheduler_started:
        return
    _scheduler_started = True

    try:
        _refresh_all()
    except Exception as e:
        print("⚠️ initial warmup error:", e)

    scheduler.add_job(_refresh_all, "interval", minutes=15, id="rss_refresh_15min", replace_existing=True)
    scheduler.start()
    print("⏱ APScheduler started (15 min interval)")

# --------------
# Routes Flask
# --------------
@app.get("/")
def home():
    return {"status": "OK", "message": "Backend Flask opérationnel 🎉"}

@app.get("/articles")
def articles():
    # ⇩⇩⇩ lance le warm-up (scraping immédiat) + scheduler si pas déjà fait
    start_scheduler_once()

    # paramètres côté client
    q = request.args.get("q", "")  # Query vide par défaut = utilise uniquement keywords.py
    hours = int(request.args.get("hours", 24))
    include_meta = request.args.get("meta", "1") not in ("0", "false", "False")

    key = _cache_key_articles(q, hours, include_meta)
    cached = _get_cache(key)
    if cached is not None:
        return jsonify({"articles": cached})

    try:
        data = get_articles(FR_FEEDS, query=q, since_hours=hours, include_meta=include_meta)
        _set_cache(key, data)
        return jsonify({"articles": data})
    except Exception as e:
        return jsonify({"articles": [], "_meta": {"error": str(e)}}), 500


@app.get("/videos")
def videos():
    """
    Endpoint pour récupérer les vidéos YouTube
    Paramètres:
    - hours: nombre d'heures à remonter (défaut: 48)
    - channel: filtrer par canal YouTube spécifique (optionnel)
    - limit: nombre max de vidéos (défaut: 30)
    """
    start_scheduler_once()
    
    hours = int(request.args.get("hours", 0))
    channel = request.args.get("channel", None)
    limit = int(request.args.get("limit", 30))

    cache_key = _cache_key_videos(channel, hours, limit)
    cached = _get_cache(cache_key)
    if cached is not None:
        return jsonify({"videos": cached})
    
    try:
        data = get_videos(FR_VIDEO_FEEDS, since_hours=hours, channel=channel, limit=limit)
        if data:
            _set_cache(cache_key, data)
        return jsonify({"videos": data})
    except Exception as e:
        # fallback archive si dispo
        try:
            from scraping.archive import _load_archive
            archive = _load_archive()
            fallback = archive.get("videos", [])
            if fallback:
                return jsonify({"videos": fallback, "_meta": {"error": str(e), "source": "archive"}}), 206
        except Exception:
            pass
        return jsonify({"videos": [], "_meta": {"error": str(e)}}), 500


@app.get("/archive")
def archive():
    """Retourne l'archive complète (articles et vidéos)"""
    try:
        data = _load_archive()
        return jsonify({
            "articles": data.get("articles", []),
            "videos": data.get("videos", []),
        })
    except Exception as e:
        return jsonify({"articles": [], "videos": [], "error": str(e)}), 500


@app.get("/stats")
def stats():
    """Retourne les statistiques de l'archive"""
    try:
        archive_stats = get_archive_stats()
        return jsonify(archive_stats)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# (Optionnel) endpoint manuel d’admin pour forcer un refresh immédiat
@app.post("/admin/refresh")
def admin_refresh():
    try:
        _refresh_all()
        return {"ok": True}
    except Exception as e:
        return {"ok": False, "error": str(e)}, 500

if __name__ == "__main__":
    print("🚀 Démarrage du serveur Flask...")
    
    # Démarre le scheduler pour les refresh automatiques  # Scraping différé de 5 secondes pour laisser Flask démarrer
    if not _scheduler_started:
        from datetime import datetime, timedelta
        # Démarre dans 5 secondes pour laisser Flask démarrer
        scheduler.add_job(_refresh_all, 'date', run_date=datetime.now() + timedelta(seconds=5), id="init_refresh", replace_existing=True)
        # Refresh automatiques toutes les 15 minutes
        scheduler.add_job(_refresh_all, "interval", minutes=15, id="rss_refresh_15min", replace_existing=True)
        scheduler.start()
        print("⏰ Scheduler démarré (premier scraping dans 5s, puis toutes les 15 minutes)")
    
    # 0.0.0.0 si tu veux tester depuis un autre device sur ton LAN
    print("🌐 Serveur disponible sur http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=True)
