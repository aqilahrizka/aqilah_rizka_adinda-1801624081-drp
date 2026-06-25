import sqlite3

conn = sqlite3.connect("affirmation.db")
cursor = conn.cursor()

cursor.execute("""
UPDATE afirmasi
SET teks = ?
WHERE id = ?
""", ("Saya semakin percaya diri setiap hari.", 4))

conn.commit()

print("Data berhasil diupdate")

conn.close()