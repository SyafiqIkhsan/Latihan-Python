harga_belanja = int(input('Masukkan harga belanja : '))

diskon = 0

if harga_belanja > 1000000:
    print("Mendapatkan diskon 6%")
    harga_total = diskon + harga_belanja - 6/100
elif harga_belanja > 500000:
    print("Mendapatkan diskon 4%")
    harga_total = diskon + harga_belanja - 4/100
elif harga_belanja > 100000:
    print("Mendapatkan diskon 2%")
    harga_total = diskon + harga_belanja - 2/100

print("Total Harga : Rp.",harga_total)

