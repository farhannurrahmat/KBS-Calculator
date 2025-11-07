def line():
    print ("=" * 64)

def space():
    print ("")

def center(text):
    print (f"| {text:^60} |")

def pembuka():
    line()
    center("!!! WELCOME !!!")
    line()
    center("KBS Calculator")
    center("-- Kalkulator Berguna Sedikit --")
    center("Dapat melakukan beberapa fungsi pilihan")
    line()

def pembuka1():
    space()
    line()
    center("~~ Operasi Sederhana ~~")
    center("Fitur ini dapat melakukan pengoperasian sederhana")
    center("dengan melakukan satu kali inputan")
    center("tetapi belum dapat pengoperasian campuran.")
    line()

def pembuka2():
    info("Anda Sekarang Masuk ke program")
    space()
    line()
    center("~~ Statisik Sederhana ~~")
    center("Fitur ini dapat menampilkan beberapa")
    center("dari statistik sederhana dari inputan.")
    line()

def pembuka4():
    space()
    line()
    center("~~ FPB dan KPK ~~")
    center("Fitur ini  dapat menampilkan FPB dan KPK")
    center("dari beberapa bilangan yang diinput")
    center("(FPB dan KPK hanya didefinisikan untuk bilangan positif)")
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

def menu1():
    while True:
        space()
        line()
        print("Silahkan memilih menu berikut:")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Kembali")
        pilihan1 = input("Masukkan pilihan anda: ")
        if pilihan1 in ("1", "2", "3", "4", "5"):
            line()
            return int(pilihan1)
        line()
        error("Inputan tidak valid. Silahkan coba lagi.")

def menu2():
    while True:
        space()
        line()
        print("Silahkan memilih menu berikut:")
        print("1. Lanjut")
        print("2. Kembali")
        pilihan1 = input("Masukkan pilihan anda: ")
        if pilihan1 in ("1", "2"):
            line()
            return int(pilihan1)
        line()
        error("Inputan tidak valid. Silahkan coba lagi.")

def menu4():
    while True:
        space()
        line()
        print("Silahkan memilih menu berikut:")
        print("1. Lanjut")
        print("2. Kembali")
        pilihan1 = input("Masukkan pilihan anda: ")
        if pilihan1 in ("1", "2"):
            line()
            return int(pilihan1)
        line()
        error("Inputan tidak valid. Silahkan coba lagi.")
        

def error(text):
    t = str(text)
    space()
    print (f"❌  {t}")

def info(text):
    t = str(text)
    space()
    print (f"ℹ️  {t}")

def penutup():
    space()
    line()
    center("Terima kasih telah menggunakan")
    center("Kalkulator Sedikit Berguna ini.")
    center("Semoga berkesan baik bagi pengguna.")
    line()
    
