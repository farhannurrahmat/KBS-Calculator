import re
import math
from utills import menu5, error, space, pembuka5, info, line
from InputValidation import validasi_data_input

def menu_bangun():
    while True:
        space()
        line()
        print("Silahkan pilih jenis bangun ruang yang mau dihitung:")
        print("1. Kubus")
        print("2. Balok")
        print("3. Tabung")
        print("4. Bola")
        pilihan5 = input("Masukkan pilihan anda: ") # IV (1) ===========================
        if pilihan5 in ("1", "2", "3", "4"):
            line()
            return int(pilihan5)
        line()
        error("Inputan tidak valid. Silahkan coba lagi.")

def menu_hitung_luasorvolume():
    return input("\nPerhitungan luas atau volume : ").lower() # IV (2) ==================

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
    "Bola": "jari-jari"}

def proses_hitung(nama_bangun, jumlah_input, hitung_luas, hitung_volume):
    while True:
        info("Ketik 'back' untuk kembali") 
        luasorvolume = menu_hitung_luasorvolume() # IV (3) ================================
        if luasorvolume.lower() == "back":
            break 
                    
        data_input = validasi_data_input(input(f"Masukkan inputan sesuai {URUTAN_INPUT[nama_bangun]} dari {nama_bangun} (pisahkan dengan spasi): ")) # IV (4) ======================================================================
        if data_input.lower() == "back":
            break 
        if not data_input.strip():
            error("Input tidak boleh kosong!")
            continue
        
        try:
            angka = [float(i) for i in data_input.split()]
        except ValueError:
            error("Input harus berupa angka!")
            continue
        if len(angka)!=jumlah_input:
            error(f"Harus memasukkan {jumlah_input} angka!")
            continue       
                     
        if luasorvolume == "luas":
            hasil = hitung_luas(*angka)
            print(f"Hasil LUAS {nama_bangun} adalah {hasil:.2f}cm^2")
            break 
        elif luasorvolume == "volume":
            hasil = hitung_volume(*angka)
            print(f"Hasil VOLUME {nama_bangun} adalah {hasil:.2f}cm^3")
            break 
        else:
            error("Pilihan harus 'luas' atau 'volume'! Silakan coba lagi")
            continue

def eksekusi5():
    pembuka5()
    while True:
        pilihan5 = menu_bangun()
        match pilihan5:
            case 1:  # Kubus
                proses_hitung("Kubus", 1, hitung_luas_kubus, hitung_volume_kubus)
            case 2:  # Balok
                proses_hitung("Balok", 3, hitung_luas_balok, hitung_volume_balok)
            case 3:  # Tabung
                proses_hitung("Tabung", 2, hitung_luas_tabung, hitung_volume_tabung)
            case 4:  # Bola
                proses_hitung("Bola", 1, hitung_luas_bola, hitung_volume_bola)