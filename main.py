from utills import pembuka, menu, error, space
from InputValidation import validasi_pilihan_utama

pembuka()
while True:
    menu()
    pilihan_menu = input("Masukkan pilihan anda: ")
    if pilihan_menu == "":
        error("Inputan tidak valid. Silahkan coba lagi.")
        continue

    pilihan = validasi_pilihan_utama(pilihan_menu)
    match pilihan:
        case "1":
            space()
            print("Fitur ini belum tersedia.")
        case "2":
            space()
            print("Fitur ini belum tersedia.")
        case "3":
            space()
            print("Fitur ini belum tersedia.")
        case "4":
            space()
            print("Fitur ini belum tersedia.")
        case "5":
            space()
            print("Fitur ini belum tersedia.")
        case "6":
            space()
            print("Fitur ini belum tersedia.")
        case "7":
            break
        case _ :
            space()
            error("Pilihan tidak tersedia.")