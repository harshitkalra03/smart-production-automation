import sqlite3
from pathlib import Path


class DatabaseManager:

    def __init__(self):

        self.project_root = Path(__file__).resolve().parent.parent.parent

        self.db_path = self.project_root / "data" / "production.db"

    def create_database(self):

        conn = sqlite3.connect(self.db_path)

        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT NOT NULL,
            model TEXT NOT NULL UNIQUE,
            tank_type TEXT,
            shape TEXT,
            power TEXT,
            active TEXT DEFAULT 'Y'
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS production_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            production_date TEXT,
            month TEXT,
            year TEXT,
            production_line TEXT,

            category TEXT,

            brand TEXT,
            model TEXT,

            capacity TEXT,
            power TEXT,
            tank_type TEXT,
            shape TEXT,

            fitting INTEGER,
            packaging INTEGER,

            remarks TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        conn.commit()
        conn.close()

        print("Database Created Successfully")
        print(self.db_path)


if __name__ == "__main__":
    DatabaseManager().create_database()