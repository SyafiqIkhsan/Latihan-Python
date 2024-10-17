total_harga = int(input('Masukkan total harga barang : '))

if total_harga > 100000:
    diskon = (90 / 100) * total_harga
    totalHarga = total_harga - diskon

print('Total diskon\t\t\t:',diskon,'%')
print('Total harga barang\t\t: Rp.',totalHarga)