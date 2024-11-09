c:\smakzie\Ngoding\Python\tugas konversi suhu.pykarakter = input('Masukkan karakter : ').upper()
nilaiMatematika = int(input('Masukkan nilai matematika : '))
nilaiBindonesia = int(input('Masukkan nilai B. Indo : '))
nilaiBinggris = int(input('Masukkan nilai B. Inggris : '))

if karakter == 'A' or karakter == 'B' and nilaiMatematika >= 60 and nilaiBindonesia >= 70 and nilaiBinggris >= 55:
    print('\nDinyatakan Lulus')
else:
    print('\nTidak lulus')