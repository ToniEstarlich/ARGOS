import sqlite3
from pathlib import Path


class Database:
    """Persistent SQLite database for ARGOS."""

    def __init__(self, path: str = "data/argos.db"):
        self.path = Path(path)

        # Make sure the data directory exists.
        self.path.parent.mkdir(parents=True, exist_ok=True)

        self.connection = sqlite3.connect(self.path)

    def initialize(self) -> None:
        self.connection.execute(
            """
            CREATE TABLE IF NOT EXISTS assets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                description TEXT NOT NULL,
                value REAL DEFAULT 0,
                tags TEXT DEFAULT ''
            )
            """
        )

        self.connection.commit()

    def close(self) -> None:
        self.connection.close()