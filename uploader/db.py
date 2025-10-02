import sqlite3

DB_PATH = "uploader.db"

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
