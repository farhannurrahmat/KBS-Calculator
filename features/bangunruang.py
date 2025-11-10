import re
import math
from utills import menu5, error, space, pembuka5, info, line, menu_hitung_luasorvolume
from InputValidation import validasi_data_input

# Fungsi bantu untuk menampilkan teks di tengah layar
def center_print(teks, width=64):
    print(teks.center(width))

# ===== Rumus Luas dan Volume setiap Bangun Ruang =====
def hitung_luas_kubus(sisi):
    return 6 * sisi**2
def hitung_volume_kubus(sisi):
    return sisi**3
def hitung_luas_balok(p, l, t):
    return 2*(p*l+p*t+l*t)
def hitung_volume_balok(p, l, t):
    return p*l*t
def hitung_luas_tabung(r, t): 
    return 2*math.pi*r*(r+t)
def hitung_volume_tabung(r, t): 
    return math.pi*r**2*t
def hitung_luas_bola(r): 
    return 4*math.pi*r**2
def hitung_volume_bola(r): 
    return 4/3*math.pi*r**3

URUTAN_INPUT = {
    "Kubus": "sisi",
    "Balok": "panjang, lebar, tinggi",
    "Tabung": "jari-jari, tinggi",
    "Bola": "jari-jari"
}

def proses_hitung(nama_bangun, jumlah_input, hitung_luas, hitung_volume):
    while True:
        luasorvolume = menu_hitung_luasorvolume()
        if luasorvolume == "back":
            break 
                    
        while True:
            info("Ketik 'back' untuk kembali")
            data_input = validasi_data_input(
                input(f"Masukkan {URUTAN_INPUT[nama_bangun]} dari {nama_bangun} (pisahkan dengan spasi): ")
            )
            if not data_input:
                continue
            if data_input.lower() == "back":
                break 
        
            try:
                angka = [float(i) for i in data_input.split()]
            except ValueError:
                error("Input harus berupa angka!")
                continue

            if len(angka) != jumlah_input:
                error(f"Harus memasukkan {jumlah_input} angka!")
                continue       

            if any(a <= 0 for a in angka):
                error("Nilai tidak boleh negatif atau nol!")
                continue
                        
            # ======= Perhitungan =======
            if luasorvolume == "luas":
                hasil = hitung_luas(*angka)
                satuan = "cm²"
                jenis = "LUAS"
            elif luasorvolume == "volume":
                hasil = hitung_volume(*angka)
                satuan = "cm³"
                jenis = "VOLUME"
            else:
                error("Pilihan harus 'luas' atau 'volume'! Silakan coba lagi")
                continue

            # ======= TAMPILKAN TABEL HASIL =======
            kolom1 = 24
            kolom2 = 27
            total = kolom1 + kolom2 + 3
            garis = "+" + "-" * (total+2) + "+"

            space()
            center_print(garis)
            center_print(f"| {'HASIL PERHITUNGAN':^{total}} |")
            center_print(garis)
            center_print(f"| {'Bangun Ruang':<{kolom1}} | {nama_bangun:<{kolom2}} |")
            center_print(f"| {'Jenis Perhitungan':<{kolom1}} | {jenis:<{kolom2}} |")
            center_print(f"| {'Nilai Input':<{kolom1}} | {', '.join(map(str, angka)):<{kolom2}} |")
            center_print(f"| {'Hasil':<{kolom1}} | {f'{hasil:.2f} {satuan}':<{kolom2}} |")
            center_print(garis)
            break


def eksekusi5():
    pembuka5()
    while True:
        pilihan5 = menu5()
        match pilihan5:
            case 1:
                proses_hitung("Kubus", 1, hitung_luas_kubus, hitung_volume_kubus)
            case 2:
                proses_hitung("Balok", 3, hitung_luas_balok, hitung_volume_balok)
            case 3:
                proses_hitung("Tabung", 2, hitung_luas_tabung, hitung_volume_tabung)
            case 4:
                proses_hitung("Bola", 1, hitung_luas_bola, hitung_volume_bola)
            case 5:
                break
