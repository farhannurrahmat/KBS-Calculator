import re
from utills import space, error, pembuka4, menu4, info, line
from InputValidation import validasi_data_input

# Fungsi bantu untuk menampilkan teks di tengah layar
def center_print(teks, width=64):
    print(teks.center(width))

def hitung_fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def hitung_kpk(a, b):
    return abs(a * b) // hitung_fpb(a, b)

def tampilkan_tabel_fpbkpk(angka, fpb, kpk):
    space()
    line()
    space()
    center_print("+-------------------------------------------+")
    center_print("| Operasi : FPB dan KPK                    |")
    center_print("+-------------------------------------------+")
    center_print(f"| Bilangan : {str(angka):<27} |")
    center_print("+-------------------------------------------+")
    center_print(f"| FPB      : {fpb:<31} |")
    center_print(f"| KPK      : {kpk:<31} |")
    center_print("+-------------------------------------------+")
    space()
    line()

def eksekusi4():
    pembuka4()
    while True:
        pilihan4 = menu4()
        match pilihan4:
            case 2:
                break
            case 1:
                while True:
                    info("Ketik 'back' untuk kembali")
                    data_input = validasi_data_input(input("Masukkan bilangan (pisahkan dengan spasi): "))
                    if not data_input:
                        continue
                    if data_input.lower() == "back":
                        break
                    try:
                        pattern = r"^[0-9\s-]+$"
                        result = re.match(pattern, data_input)
                        if result:
                            angka_str = data_input.split()
                            angka = [int(i) for i in angka_str]

                            # Cegah bilangan negatif
                            if any(i < 0 for i in angka):
                                error("Tidak boleh ada bilangan negatif.")
                                continue

                            fpb = angka[0]
                            kpk = angka[0]
                            for i in angka[1:]:
                                fpb = hitung_fpb(fpb, i)
                                kpk = hitung_kpk(kpk, i)

                            tampilkan_tabel_fpbkpk(angka, fpb, kpk)
                            break
                        else:
                            raise ValueError
                    except:
                        error("Inputan harus berupa angka.")
                        continue
