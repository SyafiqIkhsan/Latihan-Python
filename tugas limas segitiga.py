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
