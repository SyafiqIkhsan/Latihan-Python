statusLampu = input('Masukkan status lampu : ').lower()
warnaLampu = input('Masukkan warna lampu : ').lower()

if statusLampu == 'menyala':
    if warnaLampu == 'merah':
        print('Berhenti!')
    elif warnaLampu == 'kuning':
        print('Bersiap-siap!')
    elif warnaLampu == 'hijau':
        print('Silahkan Jalan!')
    else:
        print('Salah!')
else:
    print('Jalan!')


