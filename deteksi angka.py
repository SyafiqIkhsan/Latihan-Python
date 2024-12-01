#mendeteksi apakah angka tsb ratusan, ribuan, atau jutaan.
angka = int(input('Masukkan nilai angka: '))

if angka >= 99 and angka <= 1000:
    print('Angka Ratusan')
elif angka >= 1000 and angka <= 999999:
    print('Angka Ribuan')
elif angka >= 999999:
    print('Angka Jutaan')
else:
    print('Angka tidak valid')