# api.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
from threading import Lock
import time

from scraping.core import get_articles
from scraping.feeds import FR_FEEDS

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

def _cache_key(q: str, hours: int, include_meta: bool) -> str:
    return f"q={q}|h={hours}|m={1 if include_meta else 0}"

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
    _set_cache(_cache_key(q, hours, include_meta), data)

def _refresh_all():
    """
    Liste des combinaisons à rafraîchir. Ajoute ici celles dont tu as besoin.
    """
    combos = [
        ("ukraine",48,True),  # ta page principale
    ]
    print("🔄 Refresh scraping (scheduled)…")
    for q, h, m in combos:
        try:
            _refresh_combo(q, h, m)
        except Exception as e:
            print("⚠️ refresh error:", q, h, m, e)
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
    q = request.args.get("q", "ukraine")
    hours = int(request.args.get("hours", 48))
    include_meta = request.args.get("meta", "1") not in ("0", "false", "False")

    key = _cache_key(q, hours, include_meta)
    cached = _get_cache(key)
    if cached is not None:
        return jsonify({"articles": cached})

    try:
        data = get_articles(FR_FEEDS, query=q, since_hours=hours, include_meta=include_meta)
        _set_cache(key, data)
        return jsonify({"articles": data})
    except Exception as e:
        return jsonify({"articles": [], "_meta": {"error": str(e)}}), 500


# (Optionnel) endpoint manuel d’admin pour forcer un refresh immédiat
@app.post("/admin/refresh")
def admin_refresh():
    try:
        _refresh_all()
        return {"ok": True}
    except Exception as e:
        return {"ok": False, "error": str(e)}, 500

if __name__ == "__main__":
    # 0.0.0.0 si tu veux tester depuis un autre device sur ton LAN
    app.run(host="127.0.0.1", port=5000, debug=True)
