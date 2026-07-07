from database import get_connection


def tampilkan_kategori():
    conn = get_connection()
    cursor = conn.cursor()

    # Mengambil semua kategori yang unik
    cursor.execute("""
        SELECT DISTINCT category
        FROM affirmations
    """)

    kategori = cursor.fetchall()

    if len(kategori) == 0:
        print("\nBelum ada data afirmasi.")
        conn.close()
        return

    print("\n===== DAFTAR KATEGORI =====")

    for i, item in enumerate(kategori, start=1):
        print(f"{i}. {item['category']}")

    try:
        pilihan = int(input("\nPilih kategori: "))

        if pilihan < 1 or pilihan > len(kategori):
            print("Pilihan tidak valid.")
            conn.close()
            return

        nama_kategori = kategori[pilihan - 1]["category"]

        cursor.execute("""
            SELECT text
            FROM affirmations
            WHERE category = ?
        """, (nama_kategori,))

        hasil = cursor.fetchall()

        print(f"\n===== {nama_kategori.upper()} =====")

        for nomor, item in enumerate(hasil, start=1):
            print(f"{nomor}. {item['text']}")

    except ValueError:
        print("Masukkan angka yang benar.")

    conn.close()
    