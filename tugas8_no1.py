# =====================================================================
# PROGRAM TUGAS 8 - SOAL 1: VISUALISASI LAYOUT PAPAN CATUR
# =====================================================================

print("=====================================================================")
print("          SOAL 1: PROGRAM VISUALISASI LAYOUT PAPAN CATUR            ")
print("=====================================================================")

# Meminta input ukuran papan catur dari user dengan validasi angka bulat
while True:
    try:
        ukuran = int(input("Masukkan ukuran papan catur yang diinginkan (contoh: 8): "))
        if ukuran > 0:
            break
        print("❌ Ukuran papan harus lebih besar dari 0!")
    except ValueError:
        print("❌ Input tidak valid! Harap masukkan angka bulat.")

print(f"\n[INFO] Menampilkan pola papan catur ukuran {ukuran}x{ukuran}:")
print("-" * 40)

# Perulangan bersarang (nested loop) untuk menggambar baris dan kolom
for baris in range(ukuran):
    for kolom in range(ukuran):
        # Logika matematika modulo untuk menentukan pola selang-seling warna
        if (baris + kolom) % 2 == 0:
            print("⬛", end="")  # Ketentuan a: Hitam diwakili emoji hitam
        else:
            print("⬜", end="")  # Ketentuan b: Putih diwakili emoji putih
            
    print()  # Pindah ke baris baru setelah perulangan kolom horizontal selesai

print("-" * 40)
print("=====================================================================")

