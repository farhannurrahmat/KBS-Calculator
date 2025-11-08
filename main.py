from utills import pembuka, menu, error, space, penutup
from features.FPBdanKPK import eksekusi4
from features.statistik import fitur_statistik
from features.operasisederhana import eksekusi1
from features.bangunruang import eksekusi5



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
            eksekusi5()
        case 6:
            space()
            print("Fitur ini belum tersedia.")
        case 7:
            penutup()
            break
        case _ :
            space()
            error("Pilihan tidak tersedia.")