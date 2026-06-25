import sqlite3

conn = sqlite3.connect("affirmation.db")
cursor = conn.cursor()

cursor.execute("""
DELETE FROM afirmasi
WHERE id = ?
""", (9,))

conn.commit()

print("Data berhasil dihapus")

conn.close()