import sqlite3
import os

DB_PATH = os.getenv("NOTIFIER_DB_PATH", "data/notifier.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS notifications (
        id TEXT PRIMARY KEY,
        user_id TEXT,
        message TEXT
    )
    """)
    conn.commit()
    conn.close()

def insert_notification(id, user_id, message):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT INTO notifications VALUES (?, ?, ?)", (id, user_id, message))
    conn.commit()
    conn.close()
