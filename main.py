from utills import pembuka, menu, error, space
from features.FPBdanKPK import eksekusi4
from features.statistik import fitur_statistik
from features.operasisederhana import eksekusi1


pembuka()
while True:
    pilihan = menu()
    match pilihan:
        case 1:
            eksekusi1()
        case 2:
            fitur_statistik()
        case 3:
            space()
            print("Fitur ini belum tersedia.")
        case 4:
            eksekusi4()
        case 5:
            space()
            print("Fitur ini belum tersedia.")
        case 6:
            space()
            print("Fitur ini belum tersedia.")
        case 7:
            break
        case _ :
            space()
            error("Pilihan tidak tersedia.")