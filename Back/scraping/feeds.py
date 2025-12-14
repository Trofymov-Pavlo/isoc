# scraping/feeds.py
# -*- coding: utf-8 -*-

# ----------------- Flux RSS (France uniquement) -----------------



# python -m scraping.feeds




FR_FEEDS = {
    # --- Généralistes nationaux ---
    "Le Monde (en continu)": "https://www.lemonde.fr/rss/en_continu.xml",
    "Le Figaro (actualités)": "https://www.lefigaro.fr/rss/figaro_actualites.xml",
    "Franceinfo (fil)": "https://www.franceinfo.fr/titres.rss",
    "Libération (à la une)": "https://www.liberation.fr/arc/outboundfeeds/rss-all/",
    "Les Echos (monde)": "https://services.lesechos.fr/rss/les-echos-monde.xml",  # gardé comme demandé
    "Le Parisien (à la une)": "https://feeds.leparisien.fr/leparisien/rss/une",
    "Ouest-France (à la une)": "https://www.ouest-france.fr/rss/une",
    "TF1 News (actualité)": "http://www.metronews.fr/rss.xml",

    # --- France 24 ---
    "France 24 (France)": "https://www.france24.com/en/rss",
    "France 24 (Europe)": "https://www.france24.com/fr/europe/rss",
    "France 24 (Monde)": "https://www.france24.com/fr/rss",

    # --- RFI ---
    "RFI (France)": "https://www.rfi.fr/fr/france/rss",
    "RFI (Europe)": "https://www.rfi.fr/fr/europe/rss",
    "RFI (Monde)": "https://www.rfi.fr/fr/rss",

    # --- La Croix ---
    "La Croix (Monde)": "https://www.la-croix.com/feeds/rss/Monde/Europe.xml",
    "La Croix (Politi)": "https://www.la-croix.com/feeds/rss/politique.xml",
    "La Croix (International)": "https://www.la-croix.com/feeds/rss/international.xml",

    # --- Presse régionale ---
    "Sud Ouest (international)": "https://www.sudouest.fr/rss.xml",
    "20 Minutes (monde)": "https://www.20minutes.fr/feeds/rss-monde.xml",
    "20 Minutes (politique)": "https://www.20minutes.fr/feeds/rss-politique.xml",
    "BFM TV (monde)": "https://www.bfmtv.com/rss/news-24-7/",
    "RTL (La Une)": "https://infos.rtl.lu/rss/feed/headlines.rss",
    "Challenges (monde)": "https://www.challenges.fr/rss.xml",
    "La Dépêche (monde)": "https://www.ladepeche.fr/rss.xml",
    "Le Télégramme (monde)": "https://www.letelegramme.fr/monde/rss.xml",

    # --- Magazines ---
    "Le Point (à la une)": "https://www.lepoint.fr/rss.xml",
    "L'Express (a la une)": "https://www.lexpress.fr/arc/outboundfeeds/rss/alaune.xml",
    "L'Express (monde)": "https://www.lexpress.fr/arc/outboundfeeds/rss/monde.xml",
    "Courrier International": "https://www.courrierinternational.com/feed/all/rss.xml",
    "HuffPost France": "https://www.huffingtonpost.fr/rss/all_headline.xml",
    "France Inter (info)": "https://www.radiofrance.fr/franceinter/rss",
    "Slate France": "https://www.slate.fr/rss.xml",
    "RMC (info)": "https://rmc.bfmtv.com/rss/actualites/",
    "Alternatives Economiques": "https://www.alternatives-economiques.fr/rss.xml",
    "Numerama": "https://www.numerama.com/feed/",
    "01Net": "https://www.01net.com/feed/",
    "Futura Sciences": "https://www.futura-sciences.com/rss/actualites.xml",

    # --- Think tank OK ---
    "Fondation Jean Jaurès": "https://www.jean-jaures.org/feed/",

    # --- Régionaux ---
    "Paris-Normandie": "https://www.paris-normandie.fr/rss.xml",
    "Est Républicain": "https://www.estrepublicain.fr/rss",
    "L'Alsace": "https://www.lalsace.fr/rss",
    "Le Dauphiné": "https://www.ledauphine.com/rss",

    # --- International fiable ---
    "Kyiv Post": "https://www.kyivpost.com/feed",
    "UNIAN (Ukraine)": "https://rss.unian.net/site/news_eng.rss",
    "The Moscow Times": "https://www.themoscowtimes.com/rss/news",
    "Meduza": "https://meduza.io/rss/en/all",
    "Bellingcat": "https://www.bellingcat.com/feed/",
    "Oryx": "https://www.oryxspioenkop.com/feeds/posts/default",
    "Courrier des Balkans": "https://www.courrierdesbalkans.fr/spip.php?page=backend",
    "BBC Afrique (FR)": "https://feeds.bbci.co.uk/afrique/rss.xml",

    # --- AFRICA / AFP / ARTÉ (OK) ---
    "Africanews (FR) – Actualités": "https://fr.africanews.com/feed/rss?themes=news",
    "Africanews (FR) – Sahara occidental": "https://fr.africanews.com/feed/rss?tag=sahara-occidental",
    "AFP – Au fil de l’AFP": "https://www.afp.com/fr/actus/afp_actualite/792,31,9,7,33/feed",
    "AFP – Communiqués": "https://www.afp.com/fr/actus/afp_communique/all/feed",
    "AFP – Sur le fil": "https://feeds.acast.com/public/shows/64c3a6a885617f0011e3d14f",
    "Arte – Ukraine (YT)": "https://www.youtube.com/feeds/videos.xml?playlist_id=PLCwXWOyIR22uIyapIsBAk5uARuWHqtVM1",
    "Arte – Chaine YouTube": "https://www.youtube.com/feeds/videos.xml?channel_id=UCL_cZf5sHKQHMRIEax5o3sg",
    "Arte – 28 minutes": "https://www.youtube.com/feeds/videos.xml?channel_id=UC8EzKGkEiusTm7g0mTfkWkg",

    # --- Europe / Suisse / Belgique (fonctionnent) ---
    "Le Temps (Monde)": "https://partner-feeds.publishing.tamedia.ch/rss/24heures/monde",
    "24heures – Monde": "https://partner-feeds.publishing.tamedia.ch/rss/24heures/monde",
    "7sur7 – Monde": "https://www.7sur7.be/monde/rss.xml",
    "Actu.fr – Société": "https://actu.fr/societe/rss.xml",

    # --- Maghreb / Afrique ---
    "Atlantico – Général": "https://rss.atlantico.fr/",
    "Atlas Info – Afrique/Maghreb": "https://atlasinfo.fr/feed",
    "Algérie 360": "https://www.algerie360.com/feed/",
    "AllAfrica – Derniers titres": "https://fr.allafrica.com/tools/headlines/rdf/latest/headlines.rdf",

    # --- BBC / France24 / BFMTV internat ---
    "BBC Afrique": "https://feeds.bbci.co.uk/afrique/rss.xml",
    "BFMTV – International Afrique": "https://www.bfmtv.com/rss/international/afrique/",
    "BFMTV – International Europe (Allemagne)": "https://www.bfmtv.com/rss/international/europe/allemagne/",
    "BFMTV – International États-Unis": "https://www.bfmtv.com/rss/international/amerique-nord/etats-unis/",
    "24matins (international)": "https://www.24matins.fr/feed",
}




# ---------------------------------------------------
# Vérification automatique des flux RSS (diagnostic)
# ---------------------------------------------------
if __name__ == "__main__":
    from .http_state import new_session  # <-- réutilise les mêmes headers !
    import feedparser

    s = new_session()
    print("\n--- Vérification des flux RSS (avec headers du scraper) ---\n")

    for name, url in FR_FEEDS.items():
        try:
            r = s.get(url, timeout=10, allow_redirects=True)
            final = r.url

            if r.status_code != 200:
                print(f"❌ {name} — HTTP {r.status_code} → {url} (final: {final})")
                continue

            content = r.content or b""
            if len(content) < 80:
                print(f"⚠️ {name} — contenu très court (possible flux vide) → {final}")
                continue

            # Laisse feedparser juger la validité du flux
            parsed = feedparser.parse(content)
            if parsed.bozo:
                print(f"⚠️ {name} — XML atypique/bozo=True → {final}")
                continue
            if not parsed.entries:
                print(f"⚠️ {name} — flux OK mais aucune entrée → {final}")
                continue

            print(f"✅ {name} → {final}")

        except Exception as e:
            print(f"❌ {name} — erreur: {e} → {url}")
