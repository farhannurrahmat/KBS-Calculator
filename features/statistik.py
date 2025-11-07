from collections import Counter

# Input: masukkan angka dipisah spasi, misal "1 2 3 4 5"
angka = list(map(int, input("Masukkan kumpulan bilangan (pisahkan dengan spasi): ").split()))

def hitung_statistik(data):
    if not data:
        return None, None, None, None, None

    data.sort()
    n = len(data)

    mean = sum(data) / n
    median = (data[n // 2] if n % 2 != 0 else (data[n // 2 - 1] + data[n // 2]) / 2)

    frekuensi = Counter(data)
    max_freq = max(frekuensi.values())
    mode = [k for k, v in frekuensi.items() if v == max_freq]

    # Jika semua angka unik → tidak ada modus
    if len(mode) == n:
        mode = None

    return mean, median, mode, max(data), min(data)

mean, median, mode, maksimum, minimum = hitung_statistik(angka)

print(f"Mean      : {mean}")
print(f"Median    : {median}")
print(f"Modus     : {mode}")
print(f"Maksimum  : {maksimum}")
print(f"Minimum   : {minimum}")
