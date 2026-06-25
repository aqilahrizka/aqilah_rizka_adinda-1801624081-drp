import sqlite3

conn = sqlite3.connect("affirmation.db")
cursor = conn.cursor()

cursor.execute("""
SELECT kategori, COUNT(*)
FROM afirmasi
GROUP BY kategori
""")

hasil = cursor.fetchall()

print("\n=== STATISTIK AFIRMASI ===")

total = 0

for kategori, jumlah in hasil:
    print(f"{kategori}: {jumlah}")
    total += jumlah

print(f"\nTotal afirmasi: {total}")

conn.close()