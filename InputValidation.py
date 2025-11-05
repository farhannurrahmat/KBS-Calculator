import re
from utills import error

def validasi_pilihan_utama(pilihan):
    try:
        pattern = r"^[0-9]+$"
        result = re.match(pattern, pilihan)
        if result:
            return pilihan
        else:
            raise ValueError
    except:
        error("Pilihan hanya diperbolehkan menggunakan angka.")