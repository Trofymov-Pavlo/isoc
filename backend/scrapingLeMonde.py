import requests
from bs4 import BeautifulSoup

def get_articles_from_lemonde(search_query, page=1):
    url = f"https://www.lemonde.fr/recherche/?search_keywords={search_query}&start_at=&end_at=&page={page}"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/html",
        "Referer": "https://www.lemonde.fr/recherche/"
    }

    response = requests.get(url, headers=headers, timeout=20)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    articles = []

    for h3 in soup.find_all("h3"):
        a = h3.find("a")
        if not a:
            continue

        title = a.get_text(strip=True)
        link = a.get("href", "")

        if link.startswith("/"):
            link = "https://www.lemonde.fr" + link

        articles.append({"title": title, "link": link})

    return articles
