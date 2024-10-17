nilai_mahasiswa = int(input('Masukkan nilai mahasiswa: '))


if nilai_mahasiswa > 80:
    print('Nilai : A')
elif nilai_mahasiswa > 70:
    print('Nilai : B')
elif nilai_mahasiswa > 55:
    print('Nilai : C')
elif nilai_mahasiswa > 40:
    print('Nilai : D')
elif nilai_mahasiswa < 40:
    print('Nilai : E')
