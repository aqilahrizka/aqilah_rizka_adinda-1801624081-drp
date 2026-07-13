import random
from database import get_connection

# Menyimpan afirmasi yang terakhir ditampilkan
afirmasi_hari_ini = None


def tambah_data_awal():
    """
    Menambahkan data afirmasi jika tabel masih kosong.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM affirmations")
    jumlah = cursor.fetchone()[0]

    if jumlah == 0:
        data = [
            ("Aku mampu menghadapi setiap tantangan hari ini.", 1),
            ("Aku percaya pada kemampuan yang aku miliki.", 2),
            ("Aku menerima diriku apa adanya.", 3),
            ("Setiap hari adalah kesempatan untuk berkembang.", 1),
            ("Aku pantas mendapatkan hal-hal baik.", 2),
            ("Aku mampu mengendalikan pikiranku.", 3),
            ("Aku akan terus belajar dan berkembang.", 1),
            ("Aku lebih kuat daripada rasa takutku.", 3),
            ("Aku yakin bisa mencapai tujuanku.", 2)
        ]

        cursor.executemany(
            """
            INSERT INTO affirmations(text, category_id)
            VALUES (?, ?)
            """,
            data
        )

        conn.commit()

    conn.close()


def tampilkan_afirmasi_hari_ini():
    """
    Menampilkan satu afirmasi secara acak.
    """
    global afirmasi_hari_ini

    tambah_data_awal()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            affirmations.id,
            affirmations.text,
            categories.name AS category
        FROM affirmations
        JOIN categories
            ON affirmations.category_id = categories.id
        ORDER BY RANDOM()
        LIMIT 1
    """)

    afirmasi = cursor.fetchone()

    # Simpan afirmasi yang terakhir ditampilkan
    afirmasi_hari_ini = afirmasi

    print("\n===== AFIRMASI HARI INI =====")
    print(f"Kategori : {afirmasi['category']}")
    print(f'"{afirmasi["text"]}"')

    conn.close()
    