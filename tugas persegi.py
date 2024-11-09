print('================================')
print('HITUNG LUAS DAN KELILING PERSEGI')
print('--------------------------------')

def persegi():
    sisi = int(input('Masukkan nilai sisi\t: '))

    luas = lambda sisi: sisi * sisi
    keliling = lambda sisi: 4 * sisi

    print('Luas persegi\t\t:',luas(sisi),' cm2')
    print('keliling persegi\t:',keliling(sisi), ' cm2')

persegi()