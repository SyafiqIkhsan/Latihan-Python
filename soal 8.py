print('='*34)
print('PROGRAM MENGHITUNG GEOMETRI TABUNG')
print('='*34)

phi = float(input('phi: '))
jari = int(input('jari: '))
tinggi = int(input('tinggi: '))

volume = 2 * phi * jari * tinggi 

luas = (phi * jari * jari) + (2 * phi * jari * tinggi)

print('Volume tabung: ',volume,)
print('Luas tabung: ',luas,)
