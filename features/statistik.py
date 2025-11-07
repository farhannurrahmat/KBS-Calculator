import re
from collections import Counter
from utills import line, space, pembuka2, center, error
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


def fitur_statistik():
    pembuka2()
    while True:
        space()
        data_input = validasi_data_input(input("Masukkan bilangan (pisahkan dengan spasi): "))
        if not data_input:
            continue
        if data_input.lower() == "back":
            break

        try:
            pattern = r"^[0-9\s]+$"
            result = re.match(pattern, data_input)
            if result:
                angka_str = data_input.split()
                angka = [float(i) for i in angka_str]

                mean, median, modus, maksimum, minimum = hitung_statistik(angka)

                space()
                print(f"Mean     : {mean:.2f}")
                print(f"Median   : {median}")
                print(f"Modus    : {modus if modus is not None else 'Tidak ada'}")
                print(f"Maksimum : {maksimum}")
                print(f"Minimum  : {minimum}")
                space()
                line()
                continue
            else:
                raise ValueError
        except:
            error("Input tidak valid. Silakan coba lagi.")
            continue
