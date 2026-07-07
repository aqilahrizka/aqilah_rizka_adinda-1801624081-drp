from affirmation import tampilkan_afirmasi_hari_ini
from favorit import (
    simpan_favorit,
    tampilkan_favorit,
    export_csv
)
from kategori import tampilkan_kategori
from statistik import tampilkan_statistik


def tampilkan_menu():
    print("\n" + "=" * 45)
    print("         DAILY AFFIRMATION APP")
    print("=" * 45)
    print("1. Lihat Afirmasi Hari Ini")
    print("2. Simpan Afirmasi Hari Ini ke Favorit")
    print("3. Lihat Daftar Favorit")
    print("4. Jelajahi Afirmasi Berdasarkan Kategori")
    print("5. Ekspor Daftar Favorit ke CSV")
    print("6. Lihat Statistik Afirmasi & Favorit")
    print("7. Keluar")
    print("=" * 45)


def main():
    while True:
        tampilkan_menu()

        pilihan = input("Pilih menu (1-7): ")

        if pilihan == "1":
            tampilkan_afirmasi_hari_ini()

        elif pilihan == "2":
            simpan_favorit()

        elif pilihan == "3":
            tampilkan_favorit()

        elif pilihan == "4":
            tampilkan_kategori()

        elif pilihan == "5":
            export_csv()

        elif pilihan == "6":
            tampilkan_statistik()

        elif pilihan == "7":
            print("\nTerima kasih telah menggunakan Daily Affirmation App.")
            break

        else:
            print("\nPilihan tidak valid. Silakan pilih menu 1-7.")


if __name__ == "__main__":
    main()

