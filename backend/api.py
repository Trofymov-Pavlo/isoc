from flask import Flask, request, jsonify
from scrapingLeMonde import get_articles_from_lemonde
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/")
def home():
    return {"status": "OK", "message": "Backend Flask opérationnel 🎉"}

@app.get("/articles")
def articles():
    q = request.args.get("q", "ukraine")  # paramètre "q"
    page = int(request.args.get("page", 1))  # paramètre "page"
    data = get_articles_from_lemonde(q, page)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
