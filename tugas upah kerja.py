print('='*25)
print('\tUPAH KERJA')
print('='*25)

JamKerjaNormal = 48
UpahLembur = 3000

nama_karyawan = (input("Masukkan nama karyawan: "))
golongan = str(input('Masukkan golongan(A-D): '))
jam_kerja = int(input('Masukkan jam kerja: '))
jam_lembur = int(input('Masukkan jam lembur: '))


if golongan == "A":
    upah_per_jam = 4000
elif golongan == "B":
    upah_per_jam = 5000
elif golongan == "C":
    upah_per_jam = 6000
elif golongan == "D":
    upah_per_jam = 7500

if jam_kerja < JamKerjaNormal:
    UpahTotal = jam_kerja * upah_per_jam
else:
    jam_lembur = jam_kerja - JamKerjaNormal
    UpahTotal = (JamKerjaNormal * upah_per_jam) + (jam_lembur * UpahLembur)

print('Upah total karyawan: Rp.',UpahTotal)



            
    
        





