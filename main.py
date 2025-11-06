from utills import pembuka, menu, error, space

pembuka()
while True:
    pilihan = menu()
    match pilihan:
        case 1:
            space()
            print("Fitur ini belum tersedia.")
        case 2:
            space()
            print("Fitur ini belum tersedia.")
        case 3:
            space()
            print("Fitur ini belum tersedia.")
        case 4:
            space()
            print("Fitur ini belum tersedia.")
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