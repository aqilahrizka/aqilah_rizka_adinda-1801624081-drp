import csv
from datetime import datetime
from database import get_connection
import affirmation


def simpan_favorit():
    if affirmation.afirmasi_hari_ini is None:
        print("\nSilakan lihat Afirmasi Hari Ini terlebih dahulu.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    data = affirmation.afirmasi_hari_ini

    print("\n===== AFIRMASI HARI INI =====")
    print(f"Kategori : {data['category']}")
    print(f'"{data["text"]}"')

    pilih = input("\nSimpan afirmasi ini ke favorit? (y/n): ").lower()

    if pilih == "y":

        cursor.execute("""
            SELECT *
            FROM favorites
            WHERE affirmation_id = ?
        """, (data["id"],))

        if cursor.fetchone():
            print("\nAfirmasi sudah ada di daftar favorit.")

        else:
            tanggal = datetime.now().strftime("%Y-%m-%d")

            cursor.execute("""
                INSERT INTO favorites (affirmation_id, saved_date)
                VALUES (?, ?)
            """, (data["id"], tanggal))

            conn.commit()
            print("\n✓ Afirmasi berhasil disimpan ke favorit.")

    else:
        print("\nAfirmasi tidak disimpan.")

    conn.close()


def tampilkan_favorit():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            favorites.id,
            affirmations.text,
            categories.name AS category,
            favorites.saved_date
        FROM favorites
        JOIN affirmations
            ON favorites.affirmation_id = affirmations.id
        JOIN categories
            ON affirmations.category_id = categories.id
        ORDER BY favorites.id
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
        SELECT
            affirmations.text,
            categories.name AS category,
            favorites.saved_date
        FROM favorites
        JOIN affirmations
            ON favorites.affirmation_id = affirmations.id
        JOIN categories
            ON affirmations.category_id = categories.id
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

    print("\nData berhasil diekspor ke favorit.csv")