import sqlite3
import os

DB_PATH = os.getenv("PROCESSOR_DB_PATH", "data/processor.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS processed (
        id TEXT PRIMARY KEY,
        user_id TEXT,
        status TEXT,
        result TEXT
    )
    """)
    conn.commit()
    conn.close()

def insert_processed(id, user_id, status, result):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT INTO processed VALUES (?, ?, ?, ?)", (id, user_id, status, result))
    conn.commit()
    conn.close()
