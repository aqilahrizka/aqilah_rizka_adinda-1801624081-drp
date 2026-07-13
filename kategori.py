from datetime import datetime
from database import get_connection


def tampilkan_kategori():
    conn = get_connection()
    cursor = conn.cursor()

    # Mengambil semua kategori
    cursor.execute("""
        SELECT *
        FROM categories
        ORDER BY id
    """)

    kategori = cursor.fetchall()

    if len(kategori) == 0:
        print("\nBelum ada data kategori.")
        conn.close()
        return

    print("\n===== DAFTAR KATEGORI =====")

    for item in kategori:
        print(f"{item['id']}. {item['name']}")

    try:
        pilihan = int(input("\nPilih kategori: "))

        cursor.execute("""
            SELECT
                affirmations.id,
                affirmations.text
            FROM affirmations
            JOIN categories
                ON affirmations.category_id = categories.id
            WHERE categories.id = ?
        """, (pilihan,))

        hasil = cursor.fetchall()

        if len(hasil) == 0:
            print("\nKategori tidak ditemukan.")
            conn.close()
            return

        cursor.execute("""
            SELECT name
            FROM categories
            WHERE id = ?
        """, (pilihan,))

        nama_kategori = cursor.fetchone()["name"]

        print(f"\n===== {nama_kategori.upper()} =====")

        for nomor, item in enumerate(hasil, start=1):
            print(f"{nomor}. {item['text']}")

        pilih = int(input("\nMasukkan nomor afirmasi yang ingin disimpan (0 untuk kembali): "))

        if pilih == 0:
            conn.close()
            return

        if pilih < 1 or pilih > len(hasil):
            print("Nomor tidak valid.")
            conn.close()
            return

        afirmasi = hasil[pilih - 1]

        # Cek apakah sudah ada di favorit
        cursor.execute("""
            SELECT *
            FROM favorites
            WHERE affirmation_id = ?
        """, (afirmasi["id"],))

        if cursor.fetchone():
            print("\nAfirmasi sudah ada di daftar favorit.")
        else:
            tanggal = datetime.now().strftime("%Y-%m-%d")

            cursor.execute("""
                INSERT INTO favorites (affirmation_id, saved_date)
                VALUES (?, ?)
            """, (afirmasi["id"], tanggal))

            conn.commit()
            print("\n✓ Afirmasi berhasil disimpan ke favorit.")

    except ValueError:
        print("Masukkan angka yang benar.")

    conn.close()