import time

# === Warna ANSI ===
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Fungsi bantu untuk menampilkan teks di tengah layar
def center_print(teks, width=64):
    print(teks.center(width))

# === Fungsi Tampilan Dasar ===
def line(color=CYAN):
    print(f"{color}{'=' * 64}{RESET}")

def space():
    print("")

def center(text, color=BLUE):
    print(f"{color}{BOLD}{text:^64}{RESET}")

# === Header dengan animasi baris demi baris ===
def pembuka():
    space()
    line(CYAN)
    time.sleep(0.3)
    center("✨ SELAMAT DATANG ✨", MAGENTA)
    time.sleep(0.3)
    line(CYAN)
    time.sleep(0.3)
    center("KBS CALCULATOR", YELLOW)
    time.sleep(0.3)
    center("Kalkulator Berguna Sedikit", CYAN)
    time.sleep(0.3)
    center("Pilih fitur sesuai kebutuhanmu", GREEN)
    time.sleep(0.3)
    line(CYAN)
    time.sleep(0.5)

# === Header Submenu (warna berbeda) ===
def sub_header(title, lines, accent_color=GREEN):
    space()
    line(accent_color)
    for t, c in lines:
        time.sleep(0.2)
        center(t, c)
    line(accent_color)
    time.sleep(0.3)

def pembuka1():
    sub_header("OPERASI SEDERHANA", [
        ("➕ OPERASI SEDERHANA ➕", YELLOW),
        ("Hitung penjumlahan, pengurangan,", WHITE),
        ("perkalian, dan pembagian dengan mudah.", WHITE)
    ])

def pembuka2():
    sub_header("STATISTIK SEDERHANA", [
        ("📊 STATISTIK SEDERHANA 📊", YELLOW),
        ("Tampilkan nilai mean, median, modus,", WHITE),
        ("serta data terkecil dan terbesar.", WHITE)
    ])

def pembuka3():
    sub_header("OPERASI FAKTORIAL", [
        ("🧮 OPERASI FAKTORIAL 🧮", YELLOW),
        ("Hitung faktorial dari setiap bilangan,", WHITE),
        ("lalu lakukan operasi sederhana (+, -, ×, ÷).", WHITE)
    ])

def pembuka4():
    sub_header("FPB & KPK", [
        ("🔢 FPB & KPK 🔢", YELLOW),
        ("Hitung FPB dan KPK dari bilangan positif.", WHITE),
        ("Gunakan untuk menyederhanakan pecahan.", WHITE)
    ])

def pembuka5():
    sub_header("Bangun Ruang", [
        ("📐 BANGUN RUANG 📐", YELLOW),
        ("Hitung volume dan luas permukaan berbagai bentuk 3D.", WHITE),
        ("Seperti kubus, balok, tabung, dan lainnya.", WHITE)
    ])

def pembuka6():
    sub_header("Konversi Satuan", [
        ("🔄 KONVERSI SATUAN 🔄", YELLOW),
        ("Ubah panjang, massa, waktu, suhu, dan lainnya.", WHITE),
        ("Masukkan nilai dan satuan asal dengan benar.", WHITE)
    ])

# === Menu Utama ===
def menu():
    while True:
        space()
        line(CYAN)
        center("📋 MENU UTAMA 📋", MAGENTA)
        line(CYAN)
        print(f"{YELLOW}1.{RESET} ➕ Operasi Sederhana")
        print(f"{YELLOW}2.{RESET} 📊 Statistik Sederhana")
        print(f"{YELLOW}3.{RESET} 🧮 Operasi Faktorial")
        print(f"{YELLOW}4.{RESET} 🔢 FPB dan KPK")
        print(f"{YELLOW}5.{RESET} 📐 Bangun Ruang")
        print(f"{YELLOW}6.{RESET} 🔄 Konversi Satuan")
        print(f"{YELLOW}7.{RESET} 🚪 Keluar")
        line(CYAN)
        pilihan = input(f"{GREEN}Masukkan pilihan Anda (1-7): {RESET}")
        if pilihan in ("1", "2", "3", "4", "5", "6", "7"):
            line(CYAN)
            return int(pilihan)
        error("Input tidak valid. Coba lagi.")

# === Submenu Operasi Sederhana ===
def menu1():
    while True:
        space()
        line(GREEN)
        center("⚙️  OPERASI SEDERHANA ⚙️", YELLOW)
        line(GREEN)
        print(f"{WHITE}1.{RESET} ➕ Penjumlahan")
        print(f"{WHITE}2.{RESET} ➖ Pengurangan")
        print(f"{WHITE}3.{RESET} ✖️  Perkalian")
        print(f"{WHITE}4.{RESET} ➗ Pembagian")
        print(f"{WHITE}5.{RESET} 🔙 Kembali")
        line(GREEN)
        pilihan1 = input(f"{YELLOW}Pilih operasi (1-5): {RESET}")
        if pilihan1 in ("1", "2", "3", "4", "5"):
            line(GREEN)
            return int(pilihan1)
        error("Input tidak valid. Coba lagi.")

# === Submenu Statistik ===
def menu2():
    while True:
        space()
        line(GREEN)
        center("📊 MENU STATISTIK 📊", YELLOW)
        line(GREEN)
        print(f"{WHITE}1.{RESET} ▶️  Lanjut")
        print(f"{WHITE}2.{RESET} 🔙 Kembali")
        line(GREEN)
        pilihan2 = input(f"{YELLOW}Masukkan pilihan Anda (1-2): {RESET}")
        if pilihan2 in ("1", "2"):
            line(GREEN)
            return int(pilihan2)
        error("Input tidak valid. Coba lagi.")

# === Submenu Faktorial ===
def menu3():
    while True:
        space()
        line(GREEN)
        center("🧮 OPERASI FAKTORIAL 🧮", YELLOW)
        line(GREEN)
        print(f"{WHITE}1.{RESET} ➕ Penjumlahan Faktorial")
        print(f"{WHITE}2.{RESET} ➖ Pengurangan Faktorial")
        print(f"{WHITE}3.{RESET} ✖️ Perkalian Faktorial")
        print(f"{WHITE}4.{RESET} ➗ Pembagian Faktorial")
        print(f"{WHITE}5.{RESET} ❗ Faktorial Tunggal")
        print(f"{WHITE}6.{RESET} 🔙 Kembali")
        line(GREEN)
        pilihan3 = input(f"{YELLOW}Pilih operasi (1-5): {RESET}")
        if pilihan3 in ("1", "2", "3", "4", "5", "6"):
            line(GREEN)
            return int(pilihan3)
        error("Input tidak valid. Coba lagi.")

# === Submenu FPB & KPK ===
def menu4():
    while True:
        space()
        line(GREEN)
        center("🔢 MENU FPB & KPK 🔢", YELLOW)
        line(GREEN)
        print(f"{WHITE}1.{RESET} ▶️  Lanjut")
        print(f"{WHITE}2.{RESET} 🔙 Kembali")
        line(GREEN)
        pilihan4 = input(f"{YELLOW}Masukkan pilihan Anda (1-2): {RESET}")
        if pilihan4 in ("1", "2"):
            line(GREEN)
            return int(pilihan4)
        error("Input tidak valid. Coba lagi.")

# === Submenu Bangun Ruang ===
def menu5():
    while True:
        space()
        line(GREEN)
        center("📐 BANGUN RUANG 📐", YELLOW)
        line(GREEN)
        print(f"{WHITE}1.{RESET} Kubus")
        print(f"{WHITE}2.{RESET} Balok")
        print(f"{WHITE}3.{RESET} Tabung")
        print(f"{WHITE}4.{RESET} Bola")
        print(f"{WHITE}5.{RESET} Kembali")
        line(GREEN)
        pilihan5 = input(f"{YELLOW}Pilih bangun ruang (1-5): {RESET}")
        if pilihan5 in ("1", "2", "3", "4", "5"):
            line(GREEN)
            return int(pilihan5)
        error("Input tidak valid. Coba lagi.")

def menu_hitung_luasorvolume():
    while True:
        space()
        line(GREEN)
        center_print("PILIH PERHITUNGAN")
        line(GREEN)
        print("1. Luas")
        print("2. Volume")
        print("3. Kembali")
        line(GREEN)
        pilihan = input("Masukkan pilihan (1-3): ").strip()
        line(GREEN)

        match pilihan:
            case "1":
                return "luas"
            case "2":
                return "volume"
            case "3":
                return "back"
            case _:
                error("Inputan tidak valid. Silahkan coba lagi")

# === Submenu Konversi Satuan ===
def menu6():
    while True:
        space()
        line(GREEN)
        center("🔄 KONVERSI SATUAN 🔄", YELLOW)
        line(GREEN)
        print(f"{WHITE}1.{RESET} Panjang")
        print(f"{WHITE}2.{RESET} Massa")
        print(f"{WHITE}3.{RESET} Waktu")
        print(f"{WHITE}4.{RESET} Suhu")
        print(f"{WHITE}5.{RESET} Kembali")
        line(GREEN)
        pilihan6 = input(f"{YELLOW}Pilih bangun ruang (1-5): {RESET}")
        if pilihan6 in ("1", "2", "3", "4", "5"):
            line(GREEN)
            return int(pilihan6)
        error("Input tidak valid. Coba lagi.")

# === Pesan Sistem ===
def error(text):
    space()
    print(f"{RED}❌  {text}{RESET}")

def info(text):
    space()
    print(f"{CYAN}ℹ️  {text}{RESET}")

# === Penutup ===
def penutup():
    space()
    line(MAGENTA)
    center("🙏 TERIMA KASIH 🙏", YELLOW)
    time.sleep(0.2)
    center("Sudah menggunakan KBS Calculator.", WHITE)
    time.sleep(0.2)
    center("Sampai jumpa di kesempatan berikutnya!", GREEN)
    time.sleep(0.2)
    line(MAGENTA)
