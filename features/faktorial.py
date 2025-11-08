import re
from utills import menu3, error, space, pembuka3, info, line
from InputValidation import validasi_data_input

def faktorial(n):
    if n < 0 or not float(n).is_integer():
        return None
    hasil = 1
    for i in range(1, int(n) + 1):
        hasil *= i
    return hasil

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
            return None
        hasil /= a
    return hasil

def proses_input(data_input):
    if re.match(r"^[0-9\s.-]+$", data_input):
        return [float(i) for i in data_input.split()]
    else:
        return None

def konversi_faktorial(angka_list):
    hasil_faktorial = []
    for a in angka_list:
        f = faktorial(a)
        if f is None:
            error("Faktorial hanya untuk bilangan bulat positif.")
            return None
        hasil_faktorial.append(f)
    return hasil_faktorial

def tampilkan_tabel_faktorial(judul, angka_asli, angka_faktorial, hasil):
    line()
    space()
    print("+-------------------------------------------+")
    print(f"| Operasi : {judul:<31} |")
    print("+-------------------------------------------+")
    for i, (asal, fakt) in enumerate(zip(angka_asli, angka_faktorial), start=1):
        print(f"| Angka {i:<2}: {int(asal):<3}! = {int(fakt):<24} |")
    print("+-------------------------------------------+")
    print(f"| Hasil   : {hasil:<31.2f} |")
    print("+-------------------------------------------+")
    space()
    line()

def eksekusi3():
    pembuka3()
    while True:
        pilihan1 = menu3()
        match pilihan1:
            case 1:  # Penjumlahan
                while True:
                    info("Ketik 'back' untuk kembali")
                    data_input = validasi_data_input(input("Masukkan bilangan (pisahkan dengan spasi): "))
                    space()
                    if not data_input:
                        continue
                    if data_input.lower() == "back":
                        break
                    angka = proses_input(data_input)
                    if angka is None:
                        error("Inputan harus berupa angka.")
                        continue
                    angka_faktorial = konversi_faktorial(angka)
                    if angka_faktorial is None:
                        continue
                    hasil = operasi_tambah(angka_faktorial)
                    tampilkan_tabel_faktorial("Penjumlahan Faktorial", angka, angka_faktorial, hasil)
                    break

            case 2:  # Pengurangan
                while True:
                    info("Ketik 'back' untuk kembali")
                    data_input = validasi_data_input(input("Masukkan bilangan (pisahkan dengan spasi): "))
                    space()
                    if not data_input:
                        continue
                    if data_input.lower() == "back":
                        break
                    angka = proses_input(data_input)
                    if angka is None:
                        error("Inputan harus berupa angka.")
                        continue
                    angka_faktorial = konversi_faktorial(angka)
                    if angka_faktorial is None:
                        continue
                    hasil = operasi_kurang(angka_faktorial)
                    tampilkan_tabel_faktorial("Pengurangan Faktorial", angka, angka_faktorial, hasil)
                    break

            case 3:  # Perkalian
                while True:
                    info("Ketik 'back' untuk kembali")
                    data_input = validasi_data_input(input("Masukkan bilangan (pisahkan dengan spasi): "))
                    space()
                    if not data_input:
                        continue
                    if data_input.lower() == "back":
                        break
                    angka = proses_input(data_input)
                    if angka is None:
                        error("Inputan harus berupa angka.")
                        continue
                    angka_faktorial = konversi_faktorial(angka)
                    if angka_faktorial is None:
                        continue
                    hasil = operasi_kali(angka_faktorial)
                    tampilkan_tabel_faktorial("Perkalian Faktorial", angka, angka_faktorial, hasil)
                    break

            case 4:  # Pembagian
                while True:
                    info("Ketik 'back' untuk kembali")
                    data_input = validasi_data_input(input("Masukkan bilangan (pisahkan dengan spasi): "))
                    space()
                    if not data_input:
                        continue
                    if data_input.lower() == "back":
                        break
                    angka = proses_input(data_input)
                    if angka is None or len(angka) < 2:
                        error("Masukkan minimal dua angka untuk pembagian.")
                        continue
                    angka_faktorial = konversi_faktorial(angka)
                    if angka_faktorial is None:
                        continue
                    hasil = operasi_bagi(angka_faktorial)
                    if hasil is None:
                        error("Terjadi kesalahan: tidak bisa membagi dengan nol.")
                        continue
                    tampilkan_tabel_faktorial("Pembagian Faktorial", angka, angka_faktorial, hasil)
                    break

            case 5:
                break
