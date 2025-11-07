import re
from utills import error, space

def validasi_data_input(angka1):
    while True:
        try:
            pattern = r"^[0-9\s.-A-Za-z]+$"
            result = re.match(pattern,angka1)
            if result:
                return angka1
            else:
                raise ValueError
        except:
            return error("Inputan tidak valid. Silahkan coba lagi.")