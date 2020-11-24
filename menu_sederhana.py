class hitungAngka:
    def bagi(a,b):
        return float(a/b)
    def modulus(a,b):
        return a%b
        
    def menu():
        while True:
            print("=========================")
            print("1. Penjumlahan")
            print("2. Pengurangan")
            print("3. Perkalian")
            print("4. Pembagian")
            print("5. Modulus")
            print("6. Kembali ke menu awal")
            print("=========================")
            menuHitung = int(input("Pilih (1/2/3/4/5) : "))
            print("-------------------------")
            
            hasil = 0
            bilangan = []
            
            if menuHitung == 1:
                masukan = int(input("Ingin penjumlahan berapa bilangan ? : "))
                for i in range(masukan):
                    i += 1
                    bil = int(input("Masukkan bilangan ke-%d : "%i))
                    bilangan.append(bil)
                    hasil += bil
                print("Hasil penjumlahan ",bilangan," : ",hasil)
            elif menuHitung == 2:
                masukan = int(input("Ingin pengurangan berapa bilangan ? : "))
                for i in range(masukan):
                    i += 1
                    bil = int(input("Masukkan bilangan ke-%d : "%i))
                    bilangan.append(bil)
                    hasil = bilangan[0] - sum(bilangan[1:])
                print("Hasil pengurangan ",bilangan," : ",hasil)
            elif menuHitung == 3:
                masukan = int(input("Ingin perkalian berapa bilangan ? : "))
                for i in range(masukan):
                    i += 1
                    bil = int(input("Masukkan bilangan ke-%d : "%i))
                    bilangan.append(bil)
                
                hasil = 1
                for j in bilangan:
                    hasil *= j
                print("Hasil perkalian ",bilangan," : ",hasil)
            elif menuHitung == 4:
                bil1 = int(input("Masukkan bilangan ke-1 : "))
                bil2 = int(input("Masukkan bilangan ke-2 : "))
                hasil = hitungAngka.bagi(bil1,bil2)
                print("Hasil pembagian ",bil1," : ",bil2," adalah : ",hasil)
            elif menuHitung == 5:
                bil1 = int(input("Masukkan bilangan ke-1 : "))
                bil2 = int(input("Masukkan bilangan ke-2 : "))
                hasil = hitungAngka.modulus(bil1,bil2)
                print("Hasil modulus ",bil1," % ",bil2," adalah : ",hasil)
            elif menuHitung == 6:
                menuAwal.menu()
            else:
                print("Masukkan salah!")
            
            pilih = str(input("Pilih menu perhitungan lagi? (y/n) : "))
            if pilih == 'y':
                True
            elif pilih == 'n':
                break
            else:
                print("Masukkan Salah!")
                break
    
class celcius:
    def toReamur(a):
        return float((4/5)*a)
    def toFahrenheit(a):
        return float((9/5)*a+32)
    def toKelvin(a):
        return float(a+273)

class reamur:
    def toCelcius(a):
        return float((5/4)*a)
    def toFahrenheit(a):
        return float((9/4)*a+32)
    def toKelvin(a):
        return float((5/4)*a+273)
    
class fahrenheit:
    def toCelcius(a):
        return float((5/9)*(a-32))
    def toReamur(a):
        return float((4/9)*(a-32))
    def toKelvin(a):
        return float((5/9)*(a-32)+273)

class kelvin:
    def toCelcius(a):
        return float(a-273)
    def toReamur(a):
        return float((4/5)*(a-273))
    def toFahrenheit(a):
        return float((9/5)*(a-273)+32)
    
class hitungSuhu:
    def menu():
        while True:
            print("=========================")
            print("1. Celcius ke Reamur")
            print("2. Celcius ke Fahrenheit")
            print("3. Celcius ke Kelvin")
            print("4. Reamur ke Celcius")
            print("5. Reamur ke Fahrenheit")
            print("6. Reamur ke Kelvin")
            print("7. Fahrenheit ke Celcius")
            print("8. Fahrenheit ke Reamur")
            print("9. Fahrenheit ke Kelvin")
            print("10. Kelvin ke Celcius")
            print("11. Kelvin ke Reamur")
            print("12. Kelvin ke Fharenheit")
            print("13. Kembali ke menu awal")
            print("=========================")
            menuHitung = int(input("Pilih (1/2/../12/13) : "))
            print("-------------------------")
            
            if menuHitung == 1:
                suhu = float(input("Masukkan suhu Celcius : "))
                hasil = celcius.toReamur(suhu)
                print(suhu," Celcius adalah : ",hasil," Reamur")
            elif menuHitung == 2:
                suhu = float(input("Masukkan suhu Celcius : "))
                hasil = celcius.toFahrenheit(suhu)
                print(suhu," Celcius adalah : ",hasil," Fahrenheit")
            elif menuHitung == 3:
                suhu = float(input("Masukkan suhu Celcius : "))
                hasil = celcius.toKelvin(suhu)
                print(suhu," Celcius adalah : ",hasil," Kelvin")
            elif menuHitung == 4:
                suhu = float(input("Masukkan suhu Reamur : "))
                hasil = reamur.toCelcius(suhu)
                print(suhu," Reamur adalah : ",hasil," Celcius")
            elif menuHitung == 5:
                suhu = float(input("Masukkan suhu Reamur : "))
                hasil = reamur.toFahrenheit(suhu)
                print(suhu," Reamur adalah : ",hasil," Fahrenheit")
            elif menuHitung == 6:
                suhu = float(input("Masukkan suhu Reamur : "))
                hasil = reamur.toKelvin(suhu)
                print(suhu," Reamur adalah : ",hasil," Kelvin")
            elif menuHitung == 7:
                suhu = float(input("Masukkan suhu Fahrenheit : "))
                hasil = fahrenheit.toCelcius(suhu)
                print(suhu," Fahrenheit adalah : ",hasil," Celcius")
            elif menuHitung == 8:
                suhu = float(input("Masukkan suhu Fahrenheit : "))
                hasil = fahrenheit.toReamur(suhu)
                print(suhu," Fahrenheit adalah : ",hasil," Reamur")
            elif menuHitung == 9:
                suhu = float(input("Masukkan suhu Fahrenheit : "))
                hasil = fahrenheit.toKelvin(suhu)
                print(suhu," Fahrenheit adalah : ",hasil," Kelvin")
            elif menuHitung == 10:
                suhu = float(input("Masukkan suhu Kelvin : "))
                hasil = kelvin.toCelcius(suhu)
                print(suhu," Kelvin adalah : ",hasil," Celcius")
            elif menuHitung == 11:
                suhu = float(input("Masukkan suhu Kelvin : "))
                hasil = kelvin.toReamur(suhu)
                print(suhu," Kelvin adalah : ",hasil," Reamur")
            elif menuHitung == 12:
                suhu = float(input("Masukkan suhu Kelvin : "))
                hasil = kelvin.toFahrenheit(suhu)
                print(suhu," Kelvin adalah : ",hasil," Fahrenheit")
            elif menuHitung == 13:
                menuAwal.menu()
            else:
                print("Masukkan salah!")
                menuAwal.menu()
            
            pilih = str(input("Pilih menu perhitungan lagi? (y/n) : "))
            if pilih == 'y':
                True
            elif pilih == 'n':
                break
            else:
                print("Masukkan Salah!")
                break

class desimal:
    def toBiner(b):
        return bin(b)
    def toOktal(b):
        return oct(b)
    def toHeksa(b):
        return hex(b)

class hitungBiner:
    def menu():
         while True:
            print("=========================")
            print("1. Desimal ke Biner")
            print("2. Desimal ke Oktal")
            print("3. Desimal ke Heksadesimal")
# =============================================================================
#             print("4. Biner ke Desimal")
#             print("5. Biner ke Oktal")
#             print("6. Biner ke Heksadesimal")
#             print("7. Heksadesimal ke Desimal")
#             print("8. Heksadesimal ke Biner")
#             print("9. Heksadesimal ke Oktal")
# =============================================================================
            print("10. Kembali ke menu awal")
            print("=========================")
            menuHitung = int(input("Pilih (1/2/3/4/5) : "))
            print("-------------------------")
            
            if menuHitung == 1:
                bil = int(input("Masukkan bilangan Desimal : "))
                hasil = desimal.toBiner(bil)
                print("Bilangan Biner dari Desimal ",bil, " adalah : ",hasil[2:])
            elif menuHitung == 2:
                bil = int(input("Masukkan bilangan Desimal : "))
                hasil = desimal.toOktal(bil)
                print("Bilangan Oktal dari Desimal ",bil, " adalah : ",hasil[2:])
            elif menuHitung == 3:
                bil = int(input("Masukkan bilangan Desimal : "))
                hasil = desimal.toHeksa(bil)
                print("Bilangan Heksadesimal dari Desimal ",bil, " adalah : ",hasil[2:])
            elif menuHitung == 10:
                menuAwal.menu()
            else:
                print("Masukkan salah!")
                menuAwal.menu()
            
            pilih = str(input("Pilih menu perhitungan lagi? (y/n) : "))
            if pilih == 'y':
                True
            elif pilih == 'n':
                break
            else:
                print("Masukkan Salah!")
                break
            
class menuAwal:
    def menu():
        print("########### PANDHU BRIAN ALDHIANSYAH ###########")
        print("------------------------------------------------")
        print("----- 1. Perhitungan Angka         -----")
        print("----- 2. Konversi Suhu             -----")
        print("----- 3. Konversi Bilangan Desimal -----")
        print("----- 4. Keluar                    -----")
        print("------------------------------------------------")
        print("------------------------------------------------")
        menu = int(input("Pilih menu (1/2/3/4) : "))
        
        if menu == 1:
            hitungAngka.menu()
        elif menu == 2:
            hitungSuhu.menu()
        elif menu == 3:
            hitungBiner.menu()
        elif menu == 4:
            exit()
        else:
            print("Masukkan Salah!")
            exit()
            
menuAwal.menu()
