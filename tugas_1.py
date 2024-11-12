print('================================')
print('HITUNG LUAS DAN KELILING PERSEGI')
print('--------------------------------')

sisi = int(input('Masukkan nilai sisi\t: '))

luas = sisi * sisi
keliling =  4 * sisi

print('Luas persegi\t\t:',luas,' cm2')
print('keliling persegi\t:',keliling, ' cm2')

print('============================')
print('HITUNG LUAS DAN VOLUME KUBUS')
print('----------------------------')

sisi = int(input('Masukkan nilai sisi\t: '))

luas = 6 * (sisi * sisi)
volume = sisi * sisi * sisi

print('Luas kubus\t\t:',sisi,' cm2')
print('volume kubus\t\t:',luas,'cm3')

print('============================') 
print("HITUNG VOLUME DAN LUAS BALOK")
print('----------------------------')

panjang = int(input('Masukan nilai panjang\t: '))
lebar   = int(input('Masukan nilai lebar\t: '))
tinggi  = int(input('Masukan nilai tinggi\t: '))
 
luas = 2 * (panjang * lebar) + (panjang * tinggi) + (lebar * tinggi)
volume  = panjang * lebar * tinggi

print('Luas balok\t\t:',luas, 'cm2')
print('Volume balok\t\t:',volume,'cm3')

print('========================================')
print('HITUNG LUAS DAN KELILING PERSEGI PANJANG')
print('----------------------------------------')

panjang = int(input('masukkan nilai panjang\t: '))
lebar = int(input('masukkan nilai lebar\t: '))

luas = panjang * lebar
keliling = 2 * panjang + lebar

print('Luas Persegi Panjang\t:',luas, 'cm2')
print('Keliling Persegi\t:',keliling, 'cm2')

print('======================================')
print('HITUNG LUAS DAN KELILING JAJAR GENJANG')
print('--------------------------------------')

a = int(input('Masukkan nilai a\t: '))
b = int(input('Masukkan nilai b\t: '))
c = int(input('Masukkan nilai c\t: '))
d = int(input('Masukkan nilai d\t: '))
tinggi = int(input('Masukkan nilai tinggi\t: '))

luas = a * tinggi
keliling = a + b + c + d

print('Luas jajar genjang\t:',luas, 'cm2')
print('Keliling jajar genjang\t:',keliling, 'cm2')

print('=================================')
print('HITUNG LUAS DAN KELILING SEGITIGA')
print('---------------------------------')

a = int(input('Masukkan nilai alas\t: '))
tinggi = int(input('Masukkan nilai tinggi\t: '))
b = int(input('Masukkan nilai b\t: '))
c = int(input('Masukkan nilai c\t: '))
    
luas = 1/2 * a * tinggi
keliling = a + b + c

print('Luas segitiga\t\t:', luas, 'cm2')
print('Keliling segitiga\t:', keliling, 'cm2')

print('======================================')
print('HITUNG LUAS DAN KELILING BELAH KETUPAT')
print('--------------------------------------')

sisi = int(input('Masukkan nilai sisi\t: '))
d1 = int(input('Masukkan nilai d1\t: '))
d2 = int(input('Masukkan nilai d2\t: '))

luas = 1/2 * d1 * d2
keliling = 4 * sisi

print('Luas belah ketupat\t:',luas, 'cm2')
print('Keliling belah ketupat\t:',keliling, 'cm2')

print('==================================')
print('HITUNG LUAS DAN KELILING TRAPESIUM')
print('----------------------------------')

a = int(input('Masukkan nilai a\t: '))
b = int(input('Masukkan nilai b\t: '))
c = int(input('Masukkan nilai c\t: '))
d = int(input('Masukkan nilai d\t: '))
t = int(input('Masukkan nilai t\t: '))

luas = (a + b / 2) * t
keliling = a + b + c + d

print('Luas trapesium\t\t:',luas, 'cm2')
print('Keliling trapesium\t:',keliling, 'cm2')

print('======================================')
print('HITUNG LUAS DAN KELILING LAYANG LAYAN)G')
print('--------------------------------------')

AB = int(input('Masukkan nilai A\t: '))
BC = int(input('Masukkan nilai B\t: '))
CD = int(input('Masukkan nilai C\t: '))
DA = int(input('Masukkan nilai D\t: '))
d1 = int(input('Masukkan nilai d1\t: '))
d2 = int(input('Masukkan nilai d2\t: '))

luas = 1/2 * d1 * d2

keliling = AB + BC + CD + DA

print('Luas layang-layang\t:',luas, 'cm2')
print('Kelilng layang-layang\t:',keliling, 'cm2')

print('=======================================')
print('HITUNG LUAS DAN VOLUME LIMAS SEGITIGA ')
print('---------------------------------------')

la = int(input('Masukkan nilai luas alas\t\t: '))
tinggi = int(input('Masukkan nilai tinggi\t\t\t: '))
luas_selubung_limas = int(input('Masukkan nilai luas selubung limas\t: '))

luas = la + luas_selubung_limas

volume = 1/3 * la * tinggi

print('Luas limas segititga\t\t\t:',luas, 'cm2')
print('Volume limas segitiga\t\t\t:',volume, 'cm3')








