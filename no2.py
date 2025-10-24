s1 = int(input("Masukkan setoran pertama: "))
s2 = int(input("Masukkan setoran kedua: "))
s3 = int(input("Masukkan setoran ketiga: "))

if s1 <= 0 or s2 <= 0 or s3 <= 0:
    print("Input tidak valid.")
else:
    total = s1 + s2 + s3
    print("Total setoran:", total)
    
    if total < 300000:
        print("Kategori: Rendah")
    elif total < 600000:
        print("Kategori: Sedang")
    else:
        print("Kategori: Tinggi")
