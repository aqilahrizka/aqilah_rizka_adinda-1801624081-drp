# =====================================================================
# PROGRAM TUGAS 8 - SOAL 2: APLIKASI ASISTEN LOG AKTIVITAS HARIAN
# =====================================================================

print("=====================================================================")
print("       SOAL 2: APLIKASI ASISTEN PRODUKTIVITAS & LOG AKTIVITAS        ")
print("=====================================================================")

# Ketentuan b: Inisialisasi list kosong untuk menampung semua aktivitas harian
daftar_aktivitas = []

# Data aktivitas spesifik milik user (Template Data Bawaan)
aktivitas_bawaan = [
    {"nama": "Kuliah", "waktu": "08.00 - 16.00", "lokasi": "Kampus / Rumah"},
    {"nama": "Kerja", "waktu": "Fleksibel", "lokasi": "Rumah"},
    {"nama": "Kasih makan kucing pagi", "waktu": "08.00", "lokasi": "Rumah"},
    {"nama": "Kasih makan kucing malam", "waktu": "18.00", "lokasi": "Rumah"},
    {"nama": "Snack time kucing", "waktu": "Fleksibel", "lokasi": "Rumah"},
    {"nama": "Me Time", "waktu": "Weekend", "lokasi": "Rumah"}
]

# Menampilkan menu template aktivitas harian
print("Daftar template aktivitas harian kamu:")
for i, akt in enumerate(aktivitas_bawaan, 1):
    print(f" {i}. {akt['nama']:<25} ({akt['waktu']})")

# Perulangan while untuk meminta input dari user secara terus menerus
while True:
    print("\n--- INPUT DATA AKTIVITAS BARU ---")
    pilihan = input("Pilih nomor aktivitas (1-6) untuk dicatat: ").strip()
    
    # Validasi input pilihan nomor menu
    if pilihan in ["1", "2", "3", "4", "5", "6"]:
        indeks = int(pilihan) - 1
        data_terpilih = aktivitas_bawaan[indeks]
        
        # Ketentuan d: Meminta input tambahan berupa skala tingkat energi/fokus
        print(f"\nEstimasi Tingkat Fokus/Energi untuk [{data_terpilih['nama']}]:")
        print(" 1. Tinggi 🔥 (Butuh konsentrasi penuh)")
        print(" 2. Sedang ⚡ (Aktivitas biasa/rutinitas)")
        print(" 3. Rendah 💤 (Aktivitas ringan/santai)")
        pilihan_energi = input("Masukkan pilihan skala (1/2/3): ").strip()
        
        # Konversi pilihan angka menjadi string ber-emoji
        if pilihan_energi == "1":
            energi = "Tinggi 🔥"
        elif pilihan_energi == "2":
            energi = "Sedang ⚡"
        else:
            energi = "Rendah 💤"
        
        # Menyimpan semua data terstruktur ke dalam list utama (Ketentuan b & d)
        daftar_aktivitas.append({
            "nama_kegiatan": data_terpilih["nama"],
            "waktu_kerja": data_terpilih["waktu"],
            "lokasi_kerja": data_terpilih["lokasi"],
            "level_energi": energi
        })
        print(f"✅ Berhasil menambahkan: {data_terpilih['nama']}")
    else:
        print("❌ Pilihan tidak valid! Masukkan angka 1 sampai 6.")
        continue
    
    # Fitur interaktif untuk menghentikan atau melanjutkan perulangan input data
    lanjut = input("\nApakah ingin menambahkan aktivitas lagi? (y/n): ").lower().strip()
    if lanjut != 'y':
        break

# Ketentuan c: Cetak semua data aktivitas dari list dengan format tabel kustom
print("\n" + "=" * 85)
print("                    REKAPITULASI DAFTAR AKTIVITAS HARIAN                     ")
print("===========================================================================")
print(f"{'NO':<4} | {'NAMA AKTIVITAS':<25} | {'WAKTU':<15} | {'LOKASI':<15} | {'ENERGI':<10}")
print("-" * 85)

# Perulangan for untuk membongkar dan mencetak semua data di dalam list ke console
for index, item in enumerate(daftar_aktivitas, 1):
    print(
        f"{index:<4} | "
        f"{item['nama_kegiatan']:<25} | "
        f"{item['waktu_kerja']:<15} | "
        f"{item['lokasi_kerja']:<15} | "
        f"{item['level_energi']:<10}"
    )

print("=" * 85)
print(f"Sukses mendata total: {len(daftar_aktivitas)} aktivitas harian kamu.")
print("===========================================================================")