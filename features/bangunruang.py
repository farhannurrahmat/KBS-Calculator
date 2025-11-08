import re
from utills import menu5, error, space, pembuka5, info
from InputValidation import validasi_data_input

def hitung_luas_kubus():
  aaaa

def hitung_volume_kubus():
  aaaa

def hitung_luas_balok():
  aaaa

def hitung_volume_balok():
  aaaa

def hitung_luas_tabung():
  aaaa

def hitung_volume_tabung():
  aaaa

def hitung_luas_bola():
  aaaa

def hitung_volume_bola():
  aaaa

def tampilkan_menu5():
  aaaa

def menu_perhitungan():
  aaaa

def eksekusi5():
  pembuka5()
  while True:
    pilihan5 = menu5()
    match pilihan5:
        case 1:
            while True:
                info("Ketik 'back' untuk kembali")
                data_input = validasi_data_input



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

