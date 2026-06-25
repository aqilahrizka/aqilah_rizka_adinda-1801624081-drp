import sqlite3

conn = sqlite3.connect("affirmation.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS afirmasi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    teks TEXT NOT NULL,
    kategori TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Database berhasil dibuat")