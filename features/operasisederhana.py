# KBS Calculator - Operasi Sederhana
# Oleh: Vivien

def operasi_tambah(angka_list):
    return sum(angka_list)

def operasi_kurang(angka_list):
    hasil = angka_list[0]
    for a in angka_list[1:]:
        hasil -= a
    return hasil

def operasi_kali(angka_list):
    hasil = 1
    for a in angka_list:
        hasil *= a
    return hasil

def operasi_bagi(angka_list):
    hasil = angka_list[0]
    for a in angka_list[1:]:
        if a == 0:
            return "Error: Tidak bisa dibagi dengan nol!"
        hasil /= a
    return hasil

def menu_operasi():
    print("=== MENU OPERASI SEDERHANA ===")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Keluar")
    print("==============================")

while True:
    menu_operasi()
    pilihan = input("Pilih operasi (1-5): ")

    if pilihan == '5':
        print("Terima kasih telah menggunakan KBS Calculator!")
        break

    angka_input = input("Masukkan angka-angka (pisahkan dengan spasi): ")
    angka_list = list(map(float, angka_input.split()))

    if pilihan == '1':
        hasil = operasi_tambah(angka_list)
        simbol = '+'
    elif pilihan == '2':
        hasil = operasi_kurang(angka_list)
        simbol = '-'
    elif pilihan == '3':
        hasil = operasi_kali(angka_list)
        simbol = '*'
    elif pilihan == '4':
        hasil = operasi_bagi(angka_list)
        simbol = '/'
    else:
        print("Pilihan tidak valid!")
        continue

    print(f"Hasil dari operasi {simbol} adalah: {hasil}\n")
