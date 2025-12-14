# scraping/filters.py
# -*- coding: utf-8 -*-
from typing import List, Dict, Tuple
from .keywords import UA_ANCHORS, RU_ANCHORS, NATO_TERMS
from .textops import compile_regex, match_any

# Compile au chargement (comme avant dans scraping.py)
UA_RE = compile_regex(UA_ANCHORS)
RU_RE = compile_regex(RU_ANCHORS)
NATO_RE = compile_regex(NATO_TERMS)

# scraping/filters.py
def passes_filter(hay: str) -> bool:
    return (
        match_any(hay, UA_RE)
        or match_any(hay, RU_RE)
        or match_any(hay, NATO_RE)
    )


def strict_filter(entries: List[Dict], haystacks: List[str]) -> List[Dict]:
    out = []
    for entry, hay in zip(entries, haystacks):
        if not passes_filter(hay):
            continue
        item = {
            "source": entry["source"],
            "title": entry["title"],
            "link": entry["link"],
            "published": entry["published"],
            "media": entry.get("media"),
        }
        item["_meta"] = {"author": entry.get("author"), "summary": entry.get("summary")}
        out.append(item)
    return out
