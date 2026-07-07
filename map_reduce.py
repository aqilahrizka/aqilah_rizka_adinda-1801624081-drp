from functools import reduce
from database import get_connection


def tampilkan_pengolahan_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT text FROM affirmations")
    data = cursor.fetchall()

    conn.close()

    if len(data) == 0:
        print("Belum ada data afirmasi.")
        return

    # Mengambil seluruh teks afirmasi
    daftar_afirmasi = list(map(lambda item: item["text"], data))

    # Menghitung jumlah kata setiap afirmasi
    jumlah_kata = list(map(lambda teks: len(teks.split()), daftar_afirmasi))

    # Menghitung total seluruh kata
    total_kata = reduce(lambda x, y: x + y, jumlah_kata)

    print("\n===== PENGOLAHAN DATA MAP & REDUCE =====")

    for i, teks in enumerate(daftar_afirmasi):
        print(f"{i+1}. {teks}")
        print(f"   Jumlah kata : {jumlah_kata[i]}")

    print("\nTotal seluruh kata :", total_kata)
    