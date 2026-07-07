import csv
from datetime import datetime
from database import get_connection


def simpan_favorit():
    conn = get_connection()
    cursor = conn.cursor()

    # Menampilkan semua afirmasi
    cursor.execute("SELECT * FROM affirmations")
    data = cursor.fetchall()

    print("\n===== DAFTAR AFIRMASI =====")
    for item in data:
        print(f"{item['id']}. {item['text']} ({item['category']})")

    try:
        pilihan = int(input("\nMasukkan ID afirmasi yang ingin disimpan: "))

        cursor.execute(
            "SELECT * FROM affirmations WHERE id = ?",
            (pilihan,)
        )

        hasil = cursor.fetchone()

        if hasil is None:
            print("ID tidak ditemukan.")

        else:
            tanggal = datetime.now().strftime("%Y-%m-%d")

            cursor.execute("""
                INSERT INTO favorites (affirmation_id, saved_date)
                VALUES (?, ?)
            """, (pilihan, tanggal))

            conn.commit()
            print("Afirmasi berhasil disimpan ke favorit.")

    except ValueError:
        print("Masukkan angka yang benar.")

    conn.close()


def tampilkan_favorit():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT favorites.id,
               affirmations.text,
               affirmations.category,
               favorites.saved_date
        FROM favorites
        JOIN affirmations
        ON favorites.affirmation_id = affirmations.id
    """)

    data = cursor.fetchall()

    print("\n===== DAFTAR FAVORIT =====")

    if len(data) == 0:
        print("Belum ada favorit.")

    else:
        for item in data:
            print(f"""
ID : {item['id']}
Kategori : {item['category']}
Afirmasi : {item['text']}
Tanggal : {item['saved_date']}
------------------------------
""")

    conn.close()


def export_csv():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT affirmations.text,
               affirmations.category,
               favorites.saved_date
        FROM favorites
        JOIN affirmations
        ON favorites.affirmation_id = affirmations.id
    """)

    data = cursor.fetchall()

    if len(data) == 0:
        print("Tidak ada data favorit untuk diekspor.")
        conn.close()
        return

    with open("favorit.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Afirmasi",
            "Kategori",
            "Tanggal Disimpan"
        ])

        for item in data:
            writer.writerow([
                item["text"],
                item["category"],
                item["saved_date"]
            ])

    conn.close()

    print("Data berhasil diekspor ke favorit.csv")
    