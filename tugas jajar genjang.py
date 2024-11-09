print('======================================')
print('HITUNG LUAS DAN KELILING JAJAR GENJANG')
print('--------------------------------------')

def jajarGenjang():
    a = int(input('Masukkan nilai a\t: '))
    b = int(input('Masukkan nilai b\t: '))
    c = int(input('Masukkan nilai c\t: '))
    d = int(input('Masukkan nilai d\t: '))
    tinggi = int(input('Masukkan nilai tinggi\t: '))

    luas = lambda a,b, c, d: a * tinggi
    keliling = lambda a,b,c,d: a + b + c + d

print('Luas jajar genjang\t:',luas(a,b,c,d), 'cm2')
print('Keliling jajar genjang\t:',keliling(a,b,c,d), 'cm2')

jajarGenjang()
jajarGenjang()
jajarGenjang()