from utills import space, error, pembuka4

def hitung_fpb(a, b):
    while b !=0:
        a, b = b, a % b 
    return a

def hitung_kpk(a, b):
    return abs(a * b) // hitung_fpb(a, b)

def eksekusi4():
    pembuka4()
    while True:
        space()
        data_input = input("Masukkan Bilangan (Pisahkan Berdasarkan Spasi): ")
        
        angka_str = data_input.split()
        angka = [int(i) fot i in angka str]
        
        fpb = angka[0]
        kpk = angka[0]
        for i in angka[1:]:
            fpb = hitung_fpb(fpb, i)
            kpk = hitung_kpk(kpk, i)
            
        space()
        print(f"FPB dari {angka} adalah {fpb}")
        print(f"KPK dari {angka} adalah {kpk}")
        