nilai = [80, 90, 'A', 70, 100, 'B']

total = 0
jum_data = 0

for i in nilai:
    try:
        total += i
        jum_data += 1
    except TypeError:
        print(f"Data '{i}' bukan angka, dilewati.")

if jum_data > 0:
    avg = total / jum_data
    print("Rata-rata nilai:", avg)
else:
    print("Tidak ada data nilai yang valid.")

