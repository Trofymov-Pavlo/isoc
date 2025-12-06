# scraping/scraping.py
# -*- coding: utf-8 -*-
"""
Script mère : ne garde que le CLI et délègue tout à scraping.core.
"""

import argparse
from .feeds import FR_FEEDS
from .core import run_cli

def main():
    ap = argparse.ArgumentParser(description="Agrégateur RSS FR (personnel, compliant) + filtre Ukraine/Russie/OTAN.")
    ap.add_argument("--dump-all", dest="dump_all", action="store_true",
                    help="Affiche toutes les entrées (source, titre, lien, date) sans filtrage.")
    ap.add_argument("--since-hours", type=int, default=0,
                    help="Ne conserver que les articles publiés dans les N dernières heures (0 = désactivé).")
    ap.add_argument("--timeout", type=int, default=20, help="Timeout HTTP en secondes (par requête).")
    ap.add_argument("--include-meta", action="store_true",
                    help="Inclut author/summary (si présents) dans la sortie filtrée.")
    args = ap.parse_args()

    output = run_cli(
        FR_FEEDS,
        dump_all=args.dump_all,
        since_hours=args.since_hours,
        timeout=args.timeout,
        include_meta=args.include_meta,
    )
    print(output)

if __name__ == "__main__":
    main()
