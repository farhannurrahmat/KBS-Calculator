import re
from utills import menu1, error, space, pembuka1, info, line
from InputValidation import validasi_data_input

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


def tampilkan_tabel(judul, data_input, hasil):
    angka_list = data_input.split()
    line()
    space()
    print("+-------------------------------------------+")
    print(f"| Operasi : {judul:<32}|")
    print("+-------------------------------------------+")

    for i, angka in enumerate(angka_list, start=1):
        print(f"| Angka {i:<2}: {angka:<32}|")

    print("+-------------------------------------------+")
    print(f"| Hasil   : {hasil:<32.2f}|")
    print("+-------------------------------------------+")
    space()
    line()



def eksekusi1():
    pembuka1()
    while True:
        pilihan1 = menu1()
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
                    try:
                        if re.match(r"^[0-9\s.-]+$", data_input):
                            angka = [float(i) for i in data_input.split()]
                            hasil = operasi_tambah(angka)
                            tampilkan_tabel("Penjumlahan", data_input, hasil)
                            break
                        else:
                            raise ValueError
                    except:
                        error("Inputan harus berupa angka. Silakan coba lagi.")
                        continue

            case 2:  # Pengurangan
                while True:
                    info("Ketik 'back' untuk kembali")
                    data_input = validasi_data_input(input("Masukkan bilangan (pisahkan dengan spasi): "))
                    if not data_input:
                        continue
                    if data_input.lower() == "back":
                        break
                    try:
                        if re.match(r"^[0-9\s.-]+$", data_input):
                            angka = [float(i) for i in data_input.split()]
                            hasil = operasi_kurang(angka)
                            tampilkan_tabel("Pengurangan", data_input, hasil)
                            break
                        else:
                            raise ValueError
                    except:
                        error("Inputan harus berupa angka. Silakan coba lagi.")
                        continue

            case 3:  # Perkalian
                while True:
                    info("Ketik 'back' untuk kembali")
                    data_input = validasi_data_input(input("Masukkan bilangan (pisahkan dengan spasi): "))
                    if not data_input:
                        continue
                    if data_input.lower() == "back":
                        break
                    try:
                        if re.match(r"^[0-9\s.-]+$", data_input):
                            angka = [float(i) for i in data_input.split()]
                            hasil = operasi_kali(angka)
                            tampilkan_tabel("Perkalian", data_input, hasil)
                            break
                        else:
                            raise ValueError
                    except:
                        error("Inputan harus berupa angka. Silakan coba lagi.")
                        continue

            case 4:  # Pembagian
                while True:
                    info("Ketik 'back' untuk kembali")
                    data_input = validasi_data_input(input("Masukkan bilangan (pisahkan dengan spasi): "))
                    if not data_input:
                        continue
                    if data_input.lower() == "back":
                        break
                    try:
                        if re.match(r"^[0-9\s.-]+$", data_input):
                            angka = [float(i) for i in data_input.split()]
                            if len(angka) < 2:
                                error("Masukkan minimal dua angka untuk pembagian.")
                                continue
                            hasil = operasi_bagi(angka)
                            if hasil is None:
                                error("Terjadi kesalahan: tidak bisa membagi dengan nol.")
                                continue
                            tampilkan_tabel("Pembagian", data_input, hasil)
                            break
                        else:
                            raise ValueError
                    except:
                        error("Inputan harus berupa angka. Silakan coba lagi.")
                        continue

            case 5:
                break
