"""Lightweight profile storage for login/signup flows.

Uses SQLite (stdlib) and stores salted SHA-256 password hashes.
This is a minimal placeholder and not a full auth solution.
"""

from __future__ import annotations

import sqlite3
from hashlib import sha256
from pathlib import Path
from typing import Dict, Optional

DB_PATH = Path(__file__).with_name("profiles.db")


def init_db(db_path: Path = DB_PATH) -> None:
  conn = sqlite3.connect(db_path)
  try:
    conn.execute(
      """
      CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        full_name TEXT,
        password_hash TEXT NOT NULL,
        salt TEXT NOT NULL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
      )
      """
    )
    conn.commit()
  finally:
    conn.close()


def _hash_password(password: str, salt: str) -> str:
  return sha256(f"{salt}{password}".encode("utf-8")).hexdigest()


def create_user(email: str, password: str, full_name: str = "") -> bool:
  init_db()
  salt = sha256(email.encode("utf-8")).hexdigest()[:12]
  pw_hash = _hash_password(password, salt)
  conn = sqlite3.connect(DB_PATH)
  try:
    conn.execute(
      "INSERT INTO users (email, full_name, password_hash, salt) VALUES (?, ?, ?, ?)",
      (email.lower(), full_name, pw_hash, salt),
    )
    conn.commit()
    return True
  except sqlite3.IntegrityError:
    return False
  finally:
    conn.close()


def get_user(email: str) -> Optional[Dict[str, str]]:
  init_db()
  conn = sqlite3.connect(DB_PATH)
  conn.row_factory = sqlite3.Row
  try:
    row = conn.execute(
      "SELECT email, full_name, password_hash, salt, created_at FROM users WHERE email = ?",
      (email.lower(),),
    ).fetchone()
    if not row:
      return None
    return dict(row)
  finally:
    conn.close()


def verify_user(email: str, password: str) -> bool:
  user = get_user(email)
  if not user:
    return False
  candidate = _hash_password(password, user["salt"])
  return candidate == user["password_hash"]


if __name__ == "__main__":
  init_db()
  print("Profile database ready at", DB_PATH)
