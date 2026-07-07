import sqlite3

DATABASE = "affirmation.db"


def get_connection():
    """
    Membuat koneksi ke database SQLite.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn
