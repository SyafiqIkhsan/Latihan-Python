# bisa berapa banyak orang yang d input
# berapa usianya
# cari rata rata 
# cari usia tertua pertama dan kedua
# cari usia termuda pertama dan kedua
# cari data masing masing untuk usia




def aplication():
    print ("~Selamat datang di Cianjur~")
    jumlah = int(input("Berapa banyak orang?"))
    data = []
    for x in range (jumlah):
        usia = int(input("Berapa umurnya? :"))
        data.append(usia)
    jumlah2 = sum(data) / jumlah
    data.sort()
    umur_tertua = data[0]
    umur_tertua2 = data[1] if jumlah > 1 else None
    umur_termuda = data[-1]
    umur_termuda2 = data[-2] if jumlah > 1 else None
    print (f'rata rata umur di desa ini adalah {int(jumlah2)} tahun')
    print (f'yang paling muda adalah umur {umur_tertua} tahun')
    print (f'yang paling muda kedua adalah umur{umur_tertua2} tahun')
    print (f'yang paling tua adalah umur {umur_termuda} tahun')
    print (f'yang paling tua kedua adalah umur {umur_termuda2} tahun')
  

aplication()