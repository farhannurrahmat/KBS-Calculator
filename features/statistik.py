import re
from collections import Counter
from utills import line, space, pembuka2, center, error, menu2, info
from InputValidation import validasi_data_input

def hitung_statistik(data):
    if not data:
        return None, None, None, None, None
    
    data.sort()
    n = len(data)

    mean = sum(data) / n
    median = data[n // 2] if n % 2 != 0 else (data[n // 2 - 1] + data[n // 2]) / 2

    frekuensi = Counter(data)
    max_freq = max(frekuensi.values())
    modus = [k for k, v in frekuensi.items() if v == max_freq]

    if len(modus) == n:
        modus = None
    elif len(modus) == 1:
        modus = modus[0]

    return mean, median, modus, max(data), min(data)


def tampilkan_tabel(mean, median, modus, maksimum, minimum):
    space()
    print("+-----------------+---------------------+")
    print("|    Statistik    |        Nilai        |")
    print("+-----------------+---------------------+")
    print(f"| Mean            | {mean:<20.2f}|")
    print(f"| Median          | {median:<20}|")
    print(f"| Modus           | {modus if modus is not None else 'Tidak ada':<20}|")
    print(f"| Maksimum        | {maksimum:<20}|")
    print(f"| Minimum         | {minimum:<20}|")
    print("+-----------------+---------------------+")
    space()
    line()


def fitur_statistik():
    pembuka2()
    while True:
        pilihan2 = menu2()
        match pilihan2:
            case 2:
                break
            case 1:
                while True:
                    info("Ketik 'back' untuk kembali.")
                    data_input = validasi_data_input(input("Masukkan bilangan (pisahkan dengan spasi): "))
                    if not data_input:
                        continue
                    if data_input.lower() == "back":
                        break

                    try:
                        pattern = r"^[0-9\s.-]+$"
                        result = re.match(pattern, data_input)
                        if result:
                            angka_str = data_input.split()
                            angka = [float(i) for i in angka_str]

                            mean, median, modus, maksimum, minimum = hitung_statistik(angka)
                            tampilkan_tabel(mean, median, modus, maksimum, minimum)
                            break
                        else:
                            raise ValueError
                    except:
                        error("Inputan harus berupa angka. Silakan coba lagi.")
                        continue
