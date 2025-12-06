# scraping/feeds.py
# -*- coding: utf-8 -*-

# ----------------- Flux RSS (France uniquement) -----------------
FR_FEEDS = {
    # Généralistes nationaux
    "Le Monde (en continu)": "https://www.lemonde.fr/rss/en_continu.xml",
    "Le Figaro (actualités)": "https://www.lefigaro.fr/rss/figaro_actualites.xml",
    "Franceinfo (fil)": "https://www.francetvinfo.fr/titres.rss",
    "Libération (à la une)": "https://www.liberation.fr/arc/outboundfeeds/rss-all/",
    "Les Echos (monde)": "https://services.lesechos.fr/rss/les-echos-monde.xml?_gl=1*2md6lc*_gcl_au*MjEwNTU4MzY1OC4xNzY0OTY5NTk5",
    "Le Parisien (à la une)": "https://www.leparisien.fr/une/rss.xml",
    # Presse régionale / autres
    "Ouest-France (à la une)": "https://www.ouest-france.fr/rss-en-continu.xml",

    # --- France (nationaux) ---
    "France 24 (France)": "https://www.france24.com/fr/france/rss",
    "France 24 (Europe)": "https://www.france24.com/fr/europe/rss",
    "France 24 (Monde)": "https://www.france24.com/fr/monde/rss",

    "RFI (France)": "https://www.rfi.fr/fr/france/rss",
    "RFI (Europe)": "https://www.rfi.fr/fr/europe/rss",
    "RFI (Monde)": "https://www.rfi.fr/fr/flux-de-rfi/rss",

    "La Croix (Monde)": "https://www.la-croix.com/feeds/rss/Monde/Europe.xml",
    "La Croix (Politi)": "https://www.la-croix.com/feeds/rss/politique.xml",
    "La Croix (International)": "https://www.la-croix.com/feeds/rss/international.xml",

    "Sud Ouest (international)": "https://www.sudouest.fr/rss.xml",
    "20 Minutes (monde)": "https://www.20minutes.fr/feeds/rss-monde.xml",
    "20 Minutes (politique)": "https://www.20minutes.fr/feeds/rss-politique.xml",

    "BFM TV (monde)": "https://rmc.bfmtv.com/rss/info/monde/",
    "BFM TV (france)": "https://rmc.bfmtv.com/rss/info/france/",

    "RTL (faits divers)": "https://www.rtl.fr/rss/actus.xml",
    "RTL (international)": "https://www.rtl.fr/rss/actus/international.xml",

    "L’Opinion (monde)": "https://www.lopinion.fr/rss.xml",
    "Challenges (monde)": "https://www.challenges.fr/rss.xml",

    # --- Presse régionale France ---
    "La Dépêche (monde)": "https://www.ladepeche.fr/rss.xml",
    "Le Télégramme (monde)": "https://www.letelegramme.fr/monde/rss.xml",
    "Nice Matin (monde)": "https://www.nicematin.com/monde/rss.xml",
    "La Provence (monde)": "https://www.laprovence.com/rss/monde",
}
