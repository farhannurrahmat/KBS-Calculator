import re
from utills import line, space, pembuka6, error, info, menu6
from InputValidation import validasi_data_input

# ===== OPERASI KONVERSI =====

def konversi_panjang(nilai, dari, ke):
    satuan = {
        "mm": 0.001,
        "cm": 0.01,
        "dm": 0.1,
        "m": 1,
        "dam": 10,
        "hm": 100,
        "km": 1000,
        "inch": 0.0254,
        "feet": 0.3048,
        "yard": 0.9144,
        "mile": 1609.34
    }
    return nilai * satuan[dari] / satuan[ke]


def konversi_massa(nilai, dari, ke):
    satuan = {
        "mg": 0.001,
        "cg": 0.01,
        "dg": 0.1,
        "g": 1,
        "dag": 10,
        "hg": 100,
        "kg": 1000,
        "ton": 1_000_000,
        "pound": 453.592,
        "ounce": 28.3495
    }
    return nilai * satuan[dari] / satuan[ke]


def konversi_waktu(nilai, dari, ke):
    satuan = {
        "milidetik": 0.001,
        "detik": 1,
        "menit": 60,
        "jam": 3600,
        "hari": 86400,
        "minggu": 604800,
        "bulan": 2_592_000,
        "tahun": 31_536_000
    }
    return nilai * satuan[dari] / satuan[ke]


def konversi_suhu(nilai, dari, ke):
    if dari == ke:
        return nilai
    match (dari, ke):
        case ("C", "F"):
            return (nilai * 9/5) + 32
        case ("F", "C"):
            return (nilai - 32) * 5/9
        case ("C", "K"):
            return nilai + 273.15
        case ("K", "C"):
            return nilai - 273.15
        case ("C", "R"):
            return nilai * 4/5
        case ("R", "C"):
            return nilai * 5/4
        case ("F", "K"):
            return (nilai - 32) * 5/9 + 273.15
        case ("K", "F"):
            return (nilai - 273.15) * 9/5 + 32
        case ("F", "R"):
            return (nilai - 32) * 4/9
        case ("R", "F"):
            return (nilai * 9/4) + 32
        case ("K", "R"):
            return (nilai - 273.15) * 4/5
        case ("R", "K"):
            return (nilai * 5/4) + 273.15
        case _:
            return None


# ===== TAMPILKAN TABEL HASIL =====

def tampilkan_tabel_konversi(judul, nilai, dari, ke, hasil):
    line()
    space()
    print("+-------------------------------------------+")
    print(f"| Jenis Konversi : {judul:<24} |")
    print("+-------------------------------------------+")
    print(f"| Nilai Awal     : {nilai:<24.4f} |")
    print(f"| Dari Satuan    : {dari:<24} |")
    print(f"| Ke Satuan      : {ke:<24} |")
    print("+-------------------------------------------+")
    print(f"| Hasil Konversi : {hasil:<24.4f} |")
    print("+-------------------------------------------+")
    space()
    line()


# ===== MENU EKSEKUSI =====

def eksekusi6():
    pembuka6()
    while True:
        pilihan6 = menu6()
        match pilihan6:
            case 1:  # Panjang
                while True:
                    info("Ketik 'back' untuk kembali")
                    data_input = validasi_data_input(input("Masukkan nilai: "))
                    if not data_input:
                        continue
                    if data_input.lower() == "back":
                        break
                    if not re.match(r"^[0-9.]+$", data_input):
                        error("Masukkan hanya angka.")
                        continue
                    nilai = float(data_input)

                    print("\nSatuan tersedia:")
                    print("mm, cm, dm, m, dam, hm, km, inch, feet, yard, mile")
                    while True:
                        space()
                        dari = input("Dari satuan: ").lower()
                        if not dari in ("mm", "cm", "dm", "m", "dam", "hm", "km", "inch", "feet", "yard", "mile"):
                            error("Inputan tidak valid. Silahkan coba lagi.")
                            continue
                        break
                    while True:
                        space()
                        ke = input("Ke satuan: ").lower()
                        if not ke in ("mm", "cm", "dm", "m", "dam", "hm", "km", "inch", "feet", "yard", "mile"):
                            error("Inputan tidak valid. Silahkan coba lagi.")
                            continue
                        break

                    if dari in ["mm","cm","dm","m","dam","hm","km","inch","feet","yard","mile"] and ke in ["mm","cm","dm","m","dam","hm","km","inch","feet","yard","mile"]:
                        hasil = konversi_panjang(nilai, dari, ke)
                        tampilkan_tabel_konversi("Panjang", nilai, dari, ke, hasil)
                        break
                    else:
                        error("Satuan tidak dikenal.")

            case 2:  # Massa
                while True:
                    info("Ketik 'back' untuk kembali")
                    data_input = validasi_data_input(input("Masukkan nilai: "))
                    space()
                    if not data_input:
                        continue
                    if data_input.lower() == "back":
                        break
                    if not re.match(r"^[0-9.]+$", data_input):
                        error("Masukkan hanya angka.")
                        continue
                    nilai = float(data_input)

                    print("\nSatuan tersedia:")
                    print("mg, cg, dg, g, dag, hg, kg, ton, pound, ounce")
                    while True:
                        space()
                        dari = input("Dari satuan: ").lower()
                        if not dari in ("mg","cg","dg","g","dag","hg","kg","ton","pound","ounce"):
                            error("Inputan tidak valid. Silahkan coba lagi.")
                            continue
                        break
                    while True:
                        space()
                        ke = input("Ke satuan: ").lower()
                        if not ke in ("mg","cg","dg","g","dag","hg","kg","ton","pound","ounce"):
                            error("Inputan tidak valid. Silahkan coba lagi.")
                            continue
                        break

                    if dari in ["mg","cg","dg","g","dag","hg","kg","ton","pound","ounce"] and ke in ["mg","cg","dg","g","dag","hg","kg","ton","pound","ounce"]:
                        hasil = konversi_massa(nilai, dari, ke)
                        tampilkan_tabel_konversi("Massa", nilai, dari, ke, hasil)
                        break
                    else:
                        error("Satuan tidak dikenal.")

            case 3:  # Waktu
                while True:
                    info("Ketik 'back' untuk kembali")
                    data_input = validasi_data_input(input("Masukkan nilai: "))
                    space()
                    if not data_input:
                        continue
                    if data_input.lower() == "back":
                        break
                    if not re.match(r"^[0-9.]+$", data_input):
                        error("Masukkan hanya angka.")
                        continue
                    nilai = float(data_input)

                    print("\nSatuan tersedia:")
                    print("milidetik, detik, menit, jam, hari, minggu, bulan, tahun")
                    while True:
                        space()
                        dari = input("Dari satuan: ").lower()
                        if not dari in ("milidetik","detik","menit","jam","hari","minggu","bulan","tahun"):
                            error("Inputan tidak valid. Silahkan coba lagi")
                            continue
                        break
                    while True:
                        space()
                        ke = input("Ke satuan: ").lower()
                        if not ke in ("milidetik","detik","menit","jam","hari","minggu","bulan","tahun"):
                            error("Inputan tidak valid. Silahkan coba lagi")
                            continue
                        break

                    if dari in ["milidetik","detik","menit","jam","hari","minggu","bulan","tahun"] and ke in ["milidetik","detik","menit","jam","hari","minggu","bulan","tahun"]:
                        hasil = konversi_waktu(nilai, dari, ke)
                        tampilkan_tabel_konversi("Waktu", nilai, dari, ke, hasil)
                        break
                    else:
                        error("Satuan tidak dikenal.")

            case 4:  # Suhu
                while True:
                    info("Ketik 'back' untuk kembali")
                    data_input = validasi_data_input(input("Masukkan nilai: "))
                    space()
                    if not data_input:
                        continue
                    if data_input.lower() == "back":
                        break
                    if not re.match(r"^[0-9.-]+$", data_input):
                        error("Masukkan hanya angka.")
                        continue
                    nilai = float(data_input)

                    print("\nSatuan tersedia:")
                    print("C, F, K, R")
                    while True:
                        space()
                        dari = input("Dari satuan: ").upper()
                        if not dari in ("C", "F", "K", "R"):
                            error("Inputan tidak valid. Silahkan coba lagi.")
                            continue
                        break
                    while True:
                        space()
                        ke = input("Ke satuan: ").upper()
                        if not ke in ("C", "F", "K", "R"):
                            error("Inputan tidak valid. Silahkan coba lagi.")
                            continue
                        break

                    match (dari, ke):
                        case ("C"|"F"|"K"|"R", "C"|"F"|"K"|"R"):
                            hasil = konversi_suhu(nilai, dari, ke)
                            tampilkan_tabel_konversi("Suhu", nilai, dari, ke, hasil)
                            break

            case 5:
                break

            case _:
                error("Input tidak valid. Coba lagi.")
