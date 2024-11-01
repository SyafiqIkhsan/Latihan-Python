nilai = []
jumlah = int(input('Jumlah data yang akan diinput: '))

for a in range(jumlah):
    nilai.append(float(input(f'Nilai ke-{a+1} : ')))

#perhitungan 
total = max = 0
min = nilai[0]
for data in nilai:
    #total = total + data
    total += data
    if data > max:
        max = data
    
    if data < min:
        min = data

# Buat aplikasi sensus usia
# Jumlah penduduk yang diinput dtanyakan
# Input usia berdasarkan jumlah penduduk yang diinput
# Cari rata rata usia di penduduk tersebut
# Cari usia tertua pertama dan usia tertua kedua
# Cari usia ternuda pertama dan usia termuda kedua
# Hitung data usia untuk masing masing usia
