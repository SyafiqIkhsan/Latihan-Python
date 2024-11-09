print('========================================')
print('HITUNG LUAS DAN KELILING PERSEGI PANJANG')
print('----------------------------------------')

def persegi_panjang():
    panjang = int(input('masukkan nilai panjang\t: '))
    lebar = int(input('masukkan nilai lebar\t: '))

    luas = lambda panjang,lebar: panjang * lebar
    keliling = lambda panjang,lebar,: 2 * panjang + lebar

    print('Luas Persegi Panjang\t:',luas(panjang,lebar), 'cm2')
    print('Keliling Persegi\t:',keliling(panjang,lebar), 'cm2')

persegi_panjang()
persegi_panjang()
persegi_panjang()
