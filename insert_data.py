import sqlite3

conn = sqlite3.connect("affirmation.db")
cursor = conn.cursor()

data = [
    ("Saya mampu mencapai tujuan saya.", "motivasi"),
    ("Saya berkembang setiap hari.", "motivasi"),
    ("Saya memiliki potensi besar.", "motivasi"),
    ("Saya percaya pada kemampuan saya.", "percaya_diri"),
    ("Saya berharga dan bernilai.", "percaya_diri"),
    ("Saya mampu menghadapi tantangan.", "percaya_diri"),
    ("Saya berhak merasa tenang.", "mental"),
    ("Saya menerima diri saya apa adanya.", "mental"),
    ("Saya menjaga kesehatan mental saya.", "mental")
]

cursor.executemany(
    "INSERT INTO afirmasi (teks, kategori) VALUES (?, ?)",
    data
)

conn.commit()
conn.close()

print("Data berhasil ditambahkan")