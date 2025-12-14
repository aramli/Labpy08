print("Program Kalkulator sederhana")
print("-----------------------------------")

try:
    bil_1 = int(input("Inputkan bilangan pertama : "))
    bil_2 = int(input("Inputkan bilangan kedua   : "))
except ValueError:
    print("Error: Input harus berupa angka!")
    exit()

pilihan = """
-----------------------------------
Pilih operasi bilangan
1. Tambah (+)
2. Kurang (-)
3. Kali   (x)
4. Bagi   (/)
-----------------------------------
"""
print(pilihan)

operator = input("Pilih operasi yang akan dilakukan : ")

try:
    if operator == "1":
        hasil = bil_1 + bil_2
    elif operator == "2":
        hasil = bil_1 - bil_2
    elif operator == "3":
        hasil = bil_1 * bil_2
    elif operator == "4":
        try:
            hasil = bil_1 / bil_2
        except ZeroDivisionError:
            print("Error: Tidak bisa membagi dengan nol!")
            exit()
    else:
        raise Exception("Operasi gagal: Operator tidak valid!")

    print("Hasil dari operasi adalah :", hasil)

except Exception as e:
    print("Error:", e)
