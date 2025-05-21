import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('backup.db')
        self.create_tables()

    def create_tables(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                language TEXT DEFAULT 'en',
                is_admin BOOLEAN DEFAULT 0
            )
        ''')
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS backups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                source TEXT NOT NULL,
                target TEXT NOT NULL,
                last_run TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                interval INTEGER DEFAULT 900
            )
        ''')
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS clones (
                clone_id TEXT PRIMARY KEY,
                user_id INTEGER NOT NULL,
                registration_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

    def get_all_backups(self):
        return self.conn.execute("SELECT * FROM backups").fetchall()

    def register_clone(self, clone_id, user_id):
        self.conn.execute(
            "INSERT INTO clones (clone_id, user_id) VALUES (?, ?)",
            (clone_id, user_id)
        )
