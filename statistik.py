from database import get_connection
from functools import reduce


def tampilkan_statistik():
    conn = get_connection()
    cursor = conn.cursor()

    # ==========================
    # Total afirmasi
    # ==========================
    cursor.execute("SELECT COUNT(*) FROM affirmations")
    total_afirmasi = cursor.fetchone()[0]

    # ==========================
    # Total favorit
    # ==========================
    cursor.execute("SELECT COUNT(*) FROM favorites")
    total_favorit = cursor.fetchone()[0]

    # ==========================
    # Statistik per kategori
    # ==========================
    cursor.execute("""
        SELECT
            categories.name AS category,
            COUNT(*) AS jumlah
        FROM affirmations
        JOIN categories
            ON affirmations.category_id = categories.id
        GROUP BY categories.name
    """)

    kategori = cursor.fetchall()

    # ==========================
    # Mengambil seluruh afirmasi
    # ==========================
    cursor.execute("""
        SELECT text
        FROM affirmations
    """)

    data = cursor.fetchall()

    # ==========================
    # MAP
    # Mengubah setiap afirmasi menjadi panjang karakter
    # ==========================
    panjang_afirmasi = list(
        map(lambda x: len(x["text"]), data)
    )

    # ==========================
    # REDUCE
    # Menjumlahkan seluruh karakter
    # ==========================
    total_karakter = reduce(
        lambda a, b: a + b,
        panjang_afirmasi
    )

    # ==========================
    # Rata-rata panjang afirmasi
    # ==========================
    rata_rata = total_karakter / len(panjang_afirmasi)

    # ==========================
    # REDUCE
    # Mencari afirmasi terpanjang
    # ==========================
    afirmasi_terpanjang = reduce(
        lambda a, b: a if len(a["text"]) > len(b["text"]) else b,
        data
    )

    print("\n========== STATISTIK ==========")
    print(f"Total Afirmasi : {total_afirmasi}")
    print(f"Total Favorit  : {total_favorit}")

    print("\nJumlah Afirmasi per Kategori")
    print("-" * 30)

    for item in kategori:
        print(f"{item['category']} : {item['jumlah']}")

    print("\nPengolahan Data (map & reduce)")
    print("-" * 30)
    print(f"Total karakter afirmasi      : {total_karakter}")
    print(f"Rata-rata panjang afirmasi   : {rata_rata:.2f} karakter")
    print(f"Afirmasi terpanjang          :")
    print(f"\"{afirmasi_terpanjang['text']}\"")

    print("=" * 30)

    conn.close()
    