#soal 1 5, dan 6
bulan = ['Januari','februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']
bulan.append('Muharram')

for a,b in enumerate(bulan):
    print(f'bulan ke-{a+1} yaitu {b}')

#soal 2
print(bulan[2])
print(bulan[9])

#soal 3 dan 4
bulan[7] = 'August'
print(bulan[7])
bulan[0] = 'January'
print(bulan[0])







