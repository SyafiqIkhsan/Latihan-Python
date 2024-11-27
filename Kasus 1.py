jam_masuk = int(input('Jam masuk: '))

jam_keluar = int(input('Jam keluar: '))

if jam_masuk > 12:
    print('Tidak Valid')
elif jam_masuk < 1:
    print('Tidak Valid')

if jam_keluar > 12:
    print('Tidak Valid')
elif jam_keluar > 12:
    print('Tidak Valid')

if jam_masuk > jam_keluar:
    jam_kerja = (jam_keluar + 12) - jam_masuk
elif jam_masuk > jam_keluar:
    jam_kerja = jam_keluar - jam_masuk

print('Lama waktu bekerja: ', jam_kerja, 'jam')   