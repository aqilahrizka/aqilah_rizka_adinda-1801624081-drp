import sqlite3

def tampilkan_statistik():
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


if __name__ == "__main__":
    tampilkan_statistik()
    