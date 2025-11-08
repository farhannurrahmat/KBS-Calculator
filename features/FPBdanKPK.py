import re
from utills import space, error, pembuka4, menu4, info
from InputValidation import validasi_data_input

def hitung_fpb(a, b):
    while b != 0:
        a, b = b, a % b 
    return a

def hitung_kpk(a, b):
    return abs(a * b) // hitung_fpb(a, b)

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
                    data_input = validasi_data_input(input("Masukkan Bilangan (Pisahkan Berdasarkan Spasi): "))
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
                            
                            # Tambahkan logika penolakan angka negatif
                            if any(i < 0 for i in angka):
                                error("Tidak boleh ada bilangan negatif. Silakan coba lagi.")
                                continue
                            
                            fpb = angka[0]
                            kpk = angka[0]
                            for i in angka[1:]:
                                fpb = hitung_fpb(fpb, i)
                                kpk = hitung_kpk(kpk, i)
                                
                            space()
                            print("+----------------------+-----------------+-----------------+")
                            print("|       Bilangan       |       FPB       |       KPK       |")
                            print("+----------------------+-----------------+-----------------+")
                            print(f"| {str(angka):^20} | {fpb:^15} | {kpk:^15} |")
                            print("+----------------------+-----------------+-----------------+")
                            break

                        else:
                            raise ValueError
                    except:
                        error("Inputan harus berupa angka. Silakan coba lagi.")
                        continue
