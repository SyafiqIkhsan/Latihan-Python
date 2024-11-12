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

print('============================')
print('HITUNG LUAS DAN VOLUME KUBUS')
print('----------------------------')

def luasDanVulomeKubus():
    sisi = int(input('Masukkan nilai sisi\t: '))

    luas = lambda sisi: 6 * (sisi * sisi)
    volume = lambda sisi: sisi * sisi * sisi

print('Luas kubus\t\t:',sisi(sisi),' cm2')
print('volume kubus\t\t:',luas(sisi),'cm3')

luasDanVulomeKubus()
luasDanVulomeKubus()
luasDanVulomeKubus()

print('============================') 
print("HITUNG VOLUME DAN LUAS BALOK")
print('----------------------------')

def volumeDanLuasBalok():
    panjang = int(input('Masukan nilai panjang\t: '))
    lebar   = int(input('Masukan nilai lebar\t: '))
    tinggi  = int(input('Masukan nilai tinggi\t: '))
 
    luas = lambda panjang, lebar, tinggi: 2 * (panjang * lebar) + (panjang * tinggi) + (lebar * tinggi)
    volume  = lambda panjang, lebar, tinggi: panjang * lebar * tinggi

print('Luas balok\t\t:',luas(panjang, lebar, tinggi), 'cm2')
print('Volume balok\t\t:',volume(panjang, lebar, tinggi),'cm3')

volumeDanLuasBalok()
volumeDanLuasBalok()
volumeDanLuasBalok()

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

print('==================================')
print('HITUNG LUAS DAN KELILING TRAPESIUM')
print('----------------------------------')

def kelilingTrapesium():
    a = int(input('Masukkan nilai a\t: '))
    b = int(input('Masukkan nilai b\t: '))
    c = int(input('Masukkan nilai c\t: '))
    d = int(input('Masukkan nilai d\t: '))
    t = int(input('Masukkan nilai t\t: '))

    luas = lambda a,b,c,d,t: (a + b / 2) * t
    keliling = lambda a,b,c,d,t: a + b + c + d

print('Luas trapesium\t\t:',luas(a,b,c,d,t), 'cm2')
print('Keliling trapesium\t:',keliling(a,b,c,d,t), 'cm2')

kelilingTrapesium()
kelilingTrapesium()
kelilingTrapesium()

print('======================================')
print('HITUNG LUAS DAN KELILING LAYANG LAYANG')
print('--------------------------------------')

def luasDanKelilingLayang():
    AB = int(input('Masukkan nilai A\t: '))
    BC = int(input('Masukkan nilai B\t: '))
    CD = int(input('Masukkan nilai C\t: '))
    DA = int(input('Masukkan nilai D\t: '))
    d1 = int(input('Masukkan nilai d1\t: '))
    d2 = int(input('Masukkan nilai d2\t: '))

luas = lambda AB,BC,CD,DA,d1,d2: 1/2 * d1 * d2

keliling = lambda AB,BC,CD,DA,d1,d2: AB + BC + CD + DA

print('Luas layang-layang\t:',luas(AB,BC,CD,DA,d1,d2), 'cm2')
print('Kelilng layang-layang\t:',keliling(AB,BC,CD,DA,d1,d2), 'cm2')

luasDanKelilingLayang()
luasDanKelilingLayang()
luasDanKelilingLayang()

print('=======================================')
print('HITUNG LUAS DAN VOLUME LIMAS SEGITIGA ')
print('---------------------------------------')

def luasDanVolumeLimas():
    la = int(input('Masukkan nilai luas alas\t\t: '))
    tinggi = int(input('Masukkan nilai tinggi\t\t\t: '))
    luas_selubung_limas = int(input('Masukkan nilai luas selubung limas\t: '))

    luas = lambda la, tinggi,luas_selubung_limas: la + luas_selubung_limas

    volume = lambda la, tinggi,luas_selubung_limas: 1/3 * la * tinggi

print('Luas limas segititga\t\t\t:',luas(la, tinggi,luas_selubung_limas), 'cm2')
print('Volume limas segitiga\t\t\t:',volume(la, tinggi,luas_selubung_limas), 'cm3')

luasDanVolumeLimas()
luasDanVolumeLimas()
luasDanVolumeLimas()







