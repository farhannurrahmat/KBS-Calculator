import re
from utills import menu1, error, space, pembuka1
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

def eksekusi1():
    pembuka1()
    while True:
        pilihan1 = menu1()
        match pilihan1:
            case 1:  # Penjumlahan
                while True:
                    space()
                    data_input = validasi_data_input(input("Masukkan bilangan (pisahkan dengan spasi): "))
                    if not data_input:
                        continue
                    if data_input.lower() == "back":
                        break
                    try:
                        if re.match(r"^[0-9\s.-]+$", data_input):
                            angka = [float(i) for i in data_input.split()]
                            hasil = operasi_tambah(angka)
                            space()
                            print(f"Hasilnya adalah {hasil:.3f}")
                            break
                        else:
                            raise ValueError
                    except:
                        error("Input tidak valid. Silakan coba lagi.")
                        continue

            case 2:  # Pengurangan
                while True:
                    space()
                    data_input = validasi_data_input(input("Masukkan bilangan (pisahkan dengan spasi): "))
                    if not data_input:
                        continue
                    if data_input.lower() == "back":
                        break
                    try:
                        if re.match(r"^[0-9\s.-]+$", data_input):
                            angka = [float(i) for i in data_input.split()]
                            hasil = operasi_kurang(angka)
                            space()
                            print(f"Hasilnya adalah {hasil:.3f}")
                            break
                        else:
                            raise ValueError
                    except:
                        error("Input tidak valid. Silakan coba lagi.")
                        continue

            case 3:  # Perkalian
                while True:
                    space()
                    data_input = validasi_data_input(input("Masukkan bilangan (pisahkan dengan spasi): "))
                    if not data_input:
                        continue
                    if data_input.lower() == "back":
                        break
                    try:
                        if re.match(r"^[0-9\s.-]+$", data_input):
                            angka = [float(i) for i in data_input.split()]
                            hasil = operasi_kali(angka)
                            space()
                            print(f"Hasilnya adalah {hasil:.3f}")
                            break
                        else:
                            raise ValueError
                    except:
                        error("Input tidak valid. Silakan coba lagi.")
                        continue

            case 4:  # Pembagian
                while True:
                    space()
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
                            space()
                            print(f"Hasilnya adalah {hasil:.3f}")
                            break
                        else:
                            raise ValueError
                    except:
                        error("Input tidak valid. Silakan coba lagi.")
                        continue

            case 5:  # Keluar
                break
