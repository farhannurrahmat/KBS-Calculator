def line():
    print("=" * 64)

def space():
    print("")

def center(text):
    print(f" {text:^60} ")

def pembuka():
    space()
    line()
    center("✨ SELAMAT DATANG ✨")
    line()
    center("KBS CALCULATOR")
    center("Kalkulator Berguna Sedikit")
    center("Pilih fitur sesuai kebutuhanmu")
    line()

def pembuka1():
    space()
    line()
    center("➕ OPERASI SEDERHANA ➕")
    center("Hitung penjumlahan, pengurangan,")
    center("perkalian, dan pembagian dengan mudah.")
    line()

def pembuka2():
    space()
    line()
    center("📊 STATISTIK SEDERHANA 📊")
    center("Tampilkan nilai mean, median, modus,")
    center("serta data terkecil dan terbesar.")
    line()

def pembuka4():
    space()
    line()
    center("🔢 FPB & KPK 🔢")
    center("Hitung FPB dan KPK dari bilangan positif.")
    center("Gunakan untuk menyederhanakan pecahan.")
    line()

def menu():
    while True:
        space()
        line()
        center("📋 MENU UTAMA 📋")
        line()
        print("1. ➕ Operasi Sederhana")
        print("2. 📊 Statistik Sederhana")
        print("3. 🧮 Operasi Faktorial")
        print("4. 🔢 FPB dan KPK")
        print("5. 📐 Bangun Ruang")
        print("6. 🔄 Konversi Satuan")
        print("7. 🚪 Keluar")
        line()
        pilihan = input("Masukkan pilihan Anda (1-7): ")
        if pilihan in ("1", "2", "3", "4", "5", "6", "7"):
            line()
            return int(pilihan)
        error("Input tidak valid. Coba lagi.")

def menu1():
    while True:
        space()
        line()
        center("⚙️   OPERASI SEDERHANA ⚙️")
        line()
        print("1. ➕ Penjumlahan")
        print("2. ➖ Pengurangan")
        print("3. ✖️  Perkalian")
        print("4. ➗ Pembagian")
        print("5. 🔙 Kembali")
        line()
        pilihan1 = input("Pilih operasi (1-5): ")
        if pilihan1 in ("1", "2", "3", "4", "5"):
            line()
            return int(pilihan1)
        error("Input tidak valid. Coba lagi.")

def menu2():
    while True:
        space()
        line()
        center("📊 MENU STATISTIK 📊")
        line()
        print("1. ▶️ Lanjut")
        print("2. 🔙 Kembali")
        line()
        pilihan1 = input("Masukkan pilihan Anda (1-2): ")
        if pilihan1 in ("1", "2"):
            line()
            return int(pilihan1)
        error("Input tidak valid. Coba lagi.")

def menu4():
    while True:
        space()
        line()
        center("🔢 MENU FPB & KPK 🔢")
        line()
        print("1. ▶️  Lanjut")
        print("2. 🔙 Kembali")
        line()
        pilihan1 = input("Masukkan pilihan Anda (1-2): ")
        if pilihan1 in ("1", "2"):
            line()
            return int(pilihan1)
        error("Input tidak valid. Coba lagi.")

def error(text):
    space()
    print(f"❌  {text}")

def info(text):
    space()
    print(f"ℹ️  {text}")

def penutup():
    space()
    line()
    center("🙏 TERIMA KASIH 🙏")
    center("Sudah menggunakan KBS Calculator.")
    center("Sampai jumpa di kesempatan berikutnya!")
    line()
