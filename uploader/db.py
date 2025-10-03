import sqlite3
import os

DB_PATH = os.getenv("UPLOADER_DB_PATH", "data/uploader.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS uploads (
        id TEXT PRIMARY KEY,
        user_id TEXT,
        path TEXT,
        timestamp INTEGER
    )
    """)
    conn.commit()
    conn.close()

def insert_upload(id, user_id, path, timestamp):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT INTO uploads VALUES (?, ?, ?, ?)", (id, user_id, path, timestamp))
    conn.commit()
    conn.close()
