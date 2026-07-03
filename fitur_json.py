import json

# FITUR EXPORT: Menggabungkan dan menyimpan semua list data ke file JSON
def export_ke_json(data_motivasi, data_percaya_diri, data_mental, nama_file="data_afirmasi.json"):
    try:
        # Satukan data ke dalam satu struktur dictionary induk
        data_gabungan = {
            "motivasi": data_motivasi,
            "percaya_diri": data_percaya_diri,
            "mental": data_mental
        }
        with open(nama_file, 'w') as file:
            json.dump(data_gabungan, file, indent=4)
        print(f"\n[Berhasil] Semua data afirmasi telah diexport ke file '{nama_file}'!")
    except Exception as e:
        print(f"\nGagal melakukan export data: {e}")

# FITUR IMPORT: Membaca file JSON dan mengembalikannya ke program
def import_dari_json(nama_file):
    try:
        with open(nama_file, 'r') as file:
            data_terbaca = json.load(file)
        print(f"\n[Berhasil] Data dari file '{nama_file}' berhasil dibaca.")
        return data_terbaca
    except FileNotFoundError:
        print("\n[Error] File tidak ditemukan! Periksa kembali nama file Anda.")
        return None
    except Exception as e:
        print(f"\nGagal melakukan import data: {e}")
        return None
