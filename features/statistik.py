from collections import Counter

def hitung_statistik(data):
    """Fungsi untuk menghitung mean, median, modus, maksimum, dan minimum."""
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
    """Fungsi utama fitur statistik (dipanggil di menu utama)."""
    print("\n=== FITUR STATISTIK SEDERHANA ===")
   
    angka = list(map(int, input("Masukkan kumpulan bilangan (pisahkan dengan spasi): ").split()))
    mean, median, modus, maksimum, minimum = hitung_statistik(angka)

    print("\n=== HASIL STATISTIK SEDERHANA===")
    print(f"Mean      : {mean:.2f}")
    print(f"Median    : {median}")
    print(f"Modus     : {modus if modus is not None else 'Tidak ada'}")
    print(f"Maksimum  : {maksimum}")
    print(f"Minimum   : {minimum}\n")
