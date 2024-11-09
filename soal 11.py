harga_barang = int(input("Harga Barang: "))

diskon = 0.05

if harga_barang > 100000:
    print('Mendapatkan diskon sebesar 5%')
    total = harga_barang - (diskon * harga_barang)
    print('Total harga yang harus dibayar:',total,)
else:
    print('Tidak mendapatkan diskon')
    total = harga_barang
    print('Total harga yang harus dibayar:',total,)








