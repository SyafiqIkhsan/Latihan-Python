jam_masuk = int(input('Masukkan jam masuk: '))
jam_keluar = int(input('Masukkan jam keluar: '))

if jam_masuk > 12:
    print('Tidak Valid')
elif jam_masuk < 1:
    print('Tidak Valid')

if jam_keluar > 12:
    print('Tidak Valid')
elif jam_keluar < 1:
    print('Tidak Valid')

if jam_masuk > jam_keluar:
    jam_kerja = (jam_keluar + 12) - jam_masuk
elif jam_masuk <= jam_keluar:
    jam_kerja = jam_keluar - jam_masuk

if jam_kerja > 2:
    bayarParkir = 2000 + (500 * jam_kerja) - 1000
elif jam_kerja <= 2:
    bayarParkir = 2000

print('Lamar Bekerja: ', jam_kerja, 'Jam')
print('Bayar Parkir: ', bayarParkir)