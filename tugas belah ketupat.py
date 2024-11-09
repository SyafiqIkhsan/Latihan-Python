print('======================================')
print('HITUNG LUAS DAN KELILING BELAH KETUPAT')
print('--------------------------------------')

def belahKetupat():
    sisi = int(input('Masukkan nilai sisi\t: '))
    d1 = int(input('Masukkan nilai d1\t: '))
    d2 = int(input('Masukkan nilai d2\t: '))

    luas = lambda sisi,d1,d2: 1/2 * d1 * d2
    keliling = lambda sisi,d1,d2: 4 * sisi

print('Luas belah ketupat\t:',luas(sisi,d1,d2), 'cm2')
print('Keliling belah ketupat\t:',keliling(sisi,d1,d2), 'cm2')

belahKetupat()
belahKetupat()
belahKetupat()