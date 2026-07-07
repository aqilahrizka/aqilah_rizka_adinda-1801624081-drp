import random
from database import get_connection


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
            ("Aku mampu menghadapi setiap tantangan hari ini.", "Motivasi"),
            ("Aku percaya pada kemampuan yang aku miliki.", "Percaya Diri"),
            ("Aku menerima diriku apa adanya.", "Mental"),
            ("Setiap hari adalah kesempatan untuk berkembang.", "Motivasi"),
            ("Aku pantas mendapatkan hal-hal baik.", "Percaya Diri"),
            ("Aku mampu mengendalikan pikiranku.", "Mental"),
            ("Aku akan terus belajar dan berkembang.", "Motivasi"),
            ("Aku lebih kuat daripada rasa takutku.", "Mental"),
            ("Aku yakin bisa mencapai tujuanku.", "Percaya Diri")
        ]

        cursor.executemany(
            "INSERT INTO affirmations(text, category) VALUES (?, ?)",
            data
        )

        conn.commit()

    conn.close()


def tampilkan_afirmasi_hari_ini():
    """
    Menampilkan satu afirmasi secara acak.
    """
    tambah_data_awal()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM affirmations
        ORDER BY RANDOM()
        LIMIT 1
    """)

    afirmasi = cursor.fetchone()

    print("\n===== AFIRMASI HARI INI =====")
    print(f"\nKategori : {afirmasi['category']}")
    print(f'\n"{afirmasi["text"]}"')

    conn.close()
    