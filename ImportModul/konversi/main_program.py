import math.py
import convert.py
import ubah_bilangan.py

def tampilkan_menu_utama() #menampilkan menu utama program
    print("\n==MENU UTAMA==")
    print("1. Aritmatika")
    print("2. konversi")
    print("3. ubah_bilangan")
    print("4. keluar")
    print("-----------------")

def tampilkan_menu_aritmatika() #menampilkan menu aritmatika
    print("\n == Aritmatika ==")
    print("1. Penjumlahan")
    print("2. Perkalian")
    print("3. Perpangkatan")
    print("-----------------")

def tampilkan_menu_ubah_konversi()
    print("\n == konversi ==")
    print("1. metertocm")
    print("2. cmtometer")
    print("----------------")

def tampilkan_menu_ubah_bilangan()
    print("\n == ubah_bilangan")
    print("1. desimal to biner")
    print("1. desimal to biner")
    print("2. desimal to oktal")
    print("3. desimal to hexadesimal")
    print("----------------")

def main()  #fungsi utama untuk menjalankan program
    while True:
        Tampilkan_menu_utama()
        pilihan_utama = input("pilih 1 - 4") : ")


        if pilihan utama == '1':
            while True:
                tampilkan_menu_aritmatika()
                pilihan_aritmatika = input("Pilih operasi aritmatika (1-4 atau klik x untuk kembali) : ")

                if pilihan_aritmatika == 'x':
                    break:

                try:
                    num_1 = float(input("Masukkan bilangan pertama : ")
                    num_1 = float(input("Masukkan bilangan kedua : ")  
                except ValueError:
                    print("Input tidak valid! silakkan coba lagi...")
                    continue

                if pilihan_aritmatika ==  '1':
                    hasil = aritmatika.penjumlahan(num1, num2)
                    print(f"Hasil penjumlahan yaitu : {hasil}")
                elif pilihan_aritmatika ==  '2':
                    hasil = aritmatika.perkalian(num1 * num2)
                    print(f"hasil perkaliann yaitu : {hasil}")
                elif pilihan_aritmatika ==  '3':
                    hasil = aritmatika.perpangkatan(num1 ** num2)
                    print(f"hasil perpangkatan yaitu : {hasil}")
                else:
                    print("Pilihan tidak valid, silakkan coba lagi ya :) ")
                
        elif pilihan utama == '2':
             while True:
                 tampilkan_menu_ubah_konversi()
                 pilihan_ubah_konversi = input("Pilih ubah konversi (1-2 atau klik x untuk kembali) : ")

                 if pilihan_ubah_konversi == 'x':
                     break:
                     
                try:
                    nilai = float(input("Masukkan bilangan desimal : ")
                except ValueError:
                       print("Input tidak valid, coba masukkan bilangan desimal")
                       continue

                if pilihan_konversi ==  '1':
                    hasil = konversi.metertocm(nilai)
                    print(f" {nilai} M = {hasil} CM")
                elif pilihan_konversi == '2':
                    hasil = konversi. cmtometer(nilai)
                    print(f"{nilai} CM = {hasil} M")
                else:
                    print("pilihan tidak valid silakan coba lagi yah :( ")

         elif pili3han utama == '3':
             while True:
                 tampilkan_menu_ubah_bilangan()
                 pilihan_menu_ubah_bilangan = input("Pilih ubah konversi (1-2 atau klik x untuk kembali) : ")

                 if pilihan_ubah_konversi == 'x':
                     bresk:

                 try:
                     nilai_desimal = float(input("masukkan bilangan desimal yg ingin diubah : ")
                 except ValueError:
                        print("input tidak valid, coba masukkan angka desimal yang mau diubah")
                        continue

                 if pilihan_ubah_bilangan == '1':
                    hasil = ubah_bilangan.desimal_to_biner(nilai_desimal)
                    print (f"Desimal = {nilai_desimal} = Biner{hasil} ")
                elif pilihan_ubah_bilangan == '2':
                    hasil = ubah_bilangan.desimal_to_oktal(nilai_desimal)
                    print(f"Desimal = {nilai_desimal} = oktal{hasil}")
                elif pilihan_ubah_bilangan == '3':
                    hasil = ubah_bilangan.desimal_to_hexadesimal(nilai_desimal)
                    print(f"Desimal = {nilai_desimal} = hexadesimal{hasil}")
                else:
                    print("pilihan tidak valid, silakan coba lagi nanti!")

        elif pilihan utama == '4':
            print("Terima kasih")
        break:
    else:
        print("pilihan tidak valid, silakkan masukkan anga dari 1 - 4")

if __name__ == "__main__":
    main()
    


                                           
                            
                
                 
                 
                 

                    
                    
                                  
         

                    
            
                

                
        
            
    
    


    
    
    
    

