from flask import Flask, request, jsonify
from flask_cors import CORS
from scraping.scraping import get_articles


app = Flask(__name__)
CORS(app)

@app.get("/")
def home():
    return {"status": "OK", "message": "Backend Flask opérationnel 🎉"}

@app.get("/articles")
def articles():
    q = request.args.get("q", "ukraine")
    hours = int(request.args.get("hours", 24))
    meta = request.args.get("meta", "1")  # "1" / "0"
    include_meta = (meta != "0")

    data = get_articles(query=q, since_hours=hours, include_meta=include_meta)
    return jsonify(data)

if __name__ == "__main__":
    # 0.0.0.0 si tu veux tester depuis un autre device sur ton LAN
    app.run(host="127.0.0.1", port=5000, debug=True)
