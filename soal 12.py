print('A = 90-100')
print('B = 80-90')
print('C = 70-80')
print('D = 60-70')
print('E = <60')

nilai_siswa = int(input('Masukkan nilai siswa: '))

if nilai_siswa > 90:
    print('Mendapatkan nilai: A')
elif nilai_siswa > 80:
    print('Mendapatkan nilai: B')
elif nilai_siswa > 70:
    print('Mendapatkan nilai: C')
elif nilai_siswa > 60:
    print('Mendapatkan nilai: D')
else:
    print('Mendapatkan nilai: E')



