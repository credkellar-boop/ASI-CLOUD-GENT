import sqlite3
import time

DB_PATH = "storage_data/cold_archive.db"

def initialize_cold_database():
    """Sets up local physical relational schemas for cold storage offloading."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS system_archives (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp REAL,
                bucket TEXT,
                action TEXT,
                payload TEXT
            )
        ''')
        conn.commit()

def archive_record_to_disk(bucket: str, action: str, raw_payload: str):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO system_archives (timestamp, bucket, action, payload) VALUES (?, ?, ?, ?)",
            (time.time(), bucket, action, raw_payload)
        )
        conn.commit()
