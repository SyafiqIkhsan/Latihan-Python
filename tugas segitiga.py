print('=================================')
print('HITUNG LUAS DAN KELILING SEGITIGA')
print('---------------------------------')

def keliling_segitiga():
    a = int(input('Masukkan nilai alas\t: '))
    tinggi = int(input('Masukkan nilai tinggi\t: '))
    b = int(input('Masukkan nilai b\t: '))
    c = int(input('Masukkan nilai c\t: '))
    
    luas = lambda a,tinggi,b,c:  1/2 * a * tinggi
    keliling = lambda a,tinggi,b,c: a + b + c

print('Luas segitiga\t\t:', luas(a,tinggi,b,c), 'cm2')
print('Keliling segitiga\t:', keliling(a,tinggi,b,c), 'cm2')

keliling_segitiga()
keliling_segitiga()
keliling_segitiga()
