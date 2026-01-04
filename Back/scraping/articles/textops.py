# scraping/textops.py
# -*- coding: utf-8 -*-
import re, time
from typing import List, Tuple
from datetime import datetime, timezone

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

def compile_regex(words: List[str]) -> List[Tuple[str, re.Pattern]]:
    regs: List[Tuple[str, re.Pattern]] = []
    for w in sorted(set(w.strip() for w in words if w.strip())):
        w_norm = norm_text(w)
        regs.append((w, re.compile(r"\b" + re.escape(w_norm) + r"\b")))
    return regs

def match_any(hay: str, regs: List[Tuple[str, re.Pattern]]) -> bool:
    for _, rgx in regs:
        if rgx.search(hay):
            return True
    return False
