nilai_siswa = int(input('Masukkan nilai siswa : '))

if nilai_siswa <100:
    if nilai_siswa > 75:
        print('LULUS')
    else:
        print('Tidak Lulus')
else:
    print('salah!')
