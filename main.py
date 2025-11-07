from utills import pembuka, menu, error, space
<<<<<<< HEAD
from features.FPBdanKPK import eksekusi4
=======
from features.statistik import fitur_statistik

>>>>>>> b3cd6f3dbe6e52f8accee6db53fec2f606459585

pembuka()
while True:
    pilihan = menu()
    match pilihan:
        case 1:
            space()
            print("Fitur ini belum tersedia.")
        case 2:
            space()
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