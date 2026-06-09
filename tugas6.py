from datetime import datetime

print("=== Aplikasi Manajemen Aktivitas ===")

aktivitas = input("Masukkan aktivitas (sarapan / kerja): ").lower()

# =========================
# AKTIVITAS SARAPAN
# =========================
if aktivitas == "sarapan":

    print("\nMenu tersedia:")
    print("- telur")
    print("- ikan")
    print("- nugget")
    print("- roti")
    print("- nasi goreng")

    menu = input("\nMau sarapan apa? ").lower()

    if menu == "telur":
        print("Bahan tersedia.")
        print("Silakan masak telur terlebih dahulu.")

    elif menu == "ikan":
        print("Bahan tersedia.")
        print("Silakan masak ikan terlebih dahulu.")

    elif menu == "nugget":
        print("Bahan tersedia.")
        print("Silakan masak nugget terlebih dahulu.")

    elif menu == "roti":
        print("Roti siap dimakan.")

    elif menu == "nasi goreng":
        print("Bahan tidak tersedia.")
        print("Anda harus membeli bahan terlebih dahulu.")

    else:
        print("Menu tidak ditemukan.")

# =========================
# AKTIVITAS KERJA
# =========================
elif aktivitas == "kerja":

    sekarang = datetime.now()

    jam = sekarang.hour
    menit = sekarang.minute

    print(f"\nWaktu sekarang: {jam}:{menit}")

    if jam > 8:
        print("Anda TERLAMBAT masuk kerja!")

    elif jam == 8 and menit > 0:
        print("Anda TERLAMBAT masuk kerja!")

    else:
        print("Anda belum terlambat.")
        print("Semangat bekerja!")

# =========================
# JIKA INPUT SALAH
# =========================
else:
    print("Aktivitas tidak dikenali.")
    