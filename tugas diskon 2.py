hargaBelanja = float(input('Masukkan harga belanja : '))
diskon = 0

if hargaBelanja >= 1000000:
    print('Mendapatkan diskon 6%')
    diskon = 6/100 * hargaBelanja
elif hargaBelanja >= 500000:
    print('Mendapatkan diskon 4%')
    diskon = 4/100 * hargaBelanja
elif hargaBelanja >= 100000:
    print('Mendapatkan diskon 2%')
    diskon = 2/100 * hargaBelanja

totalBayar = hargaBelanja - diskon

print(f'''
Harga Beli  : {hargaBelanja}
Diskon      : {diskon}
Dibayar     : {totalBayar}
''')