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
