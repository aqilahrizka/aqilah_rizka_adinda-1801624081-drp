from affirmation import tampil_afirmasi
from kategori import tampil_kategori
from favorit import tampil_favorit

while True:
    print("\n=== DAILY AFFIRMATION ===")
    print("1. Lihat Afirmasi Hari Ini")
    print("2. Lihat Kategori")
    print("3. Lihat Favorit")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tampil_afirmasi()

    elif pilihan == "2":
        tampil_kategori()

    elif pilihan == "3":
        tampil_favorit()

    elif pilihan == "4":
        print("Terima kasih telah menggunakan aplikasi.")
        break

    else:
        print("Pilihan tidak valid.")