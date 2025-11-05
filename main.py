from utills import pembuka, menu, error
from InputValidation import validasi_pilihan_utama

pembuka()
while True:
    menu()
    pilihan = validasi_pilihan_utama(input("Masukkan pilihan anda: "))
    match pilihan:
        case "1":
            
        case "2":
            
        case "3":
            
        case "4":

        case "5":

        case "6":
            
        case "7":
            break
        case _ :
           error("Pilihan tidak ada di menu") 
        