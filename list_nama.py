nama1 = 'Cahya'
nama2 = 'Firdan'
nama3 = 'Ziya'

nama = ['Aden','Aditya','Azami']
nama[0] = 'Aden Fachri Athoriq'
nama[1] = 'Aditya Saputra'
nama[2] = 'Azami Syauqi'

print(nama[0])
print(nama[1])
print(nama[2])
nama.append('Alifka')

for i,x in enumerate(nama):
    print(i+1,'.',x)
