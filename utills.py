def line():
    print ("=" * 64)

def space():
    print ("")

def center(text):
    t = str(text)
    print (f"| {t:^60} |")

def pembuka():
    line()
    center("!!! WELCOME !!!")
    line()
    center("KBS Calculator")
    center("-- Kalkulator Berguna Sedikit --")
    center("Dapat melakukan beberapa fungsi pilihan")
    line()

def menu():
    while True:
        space()
        line()
        print("Silahkan memilih menu berikut:")
        print("1. ➕ Operasi Sederhana")
        print("2. 📊 Statistik Sederhana")
        print("3. 🧮 Operasi Faktorial")
        print("4. 🔢 FPB dan KPK")
        print("5. 📐 Bangun Ruang")
        print("6. 🔄 Konversi Satuan")
        print("7. 🚪 Keluar")
        pilihan = input("Masukkan pilihan anda: ")
        if pilihan in ("1", "2", "3", "4", "5", "6", "7"):
            line()
            return int(pilihan)
        line()
        error("Inputan tidak valid. Silahkan coba lagi.")
        

def error(text):
    t = str(text)
    space()
    print (f"❌ {t}")
    
