print('============================')
print('HITUNG LUAS DAN VOLUME KUBUS')
print('----------------------------')

def luasDanVulomeKubus():
    sisi = int(input('Masukkan nilai sisi\t: '))

    luas = lambda sisi: 6 * (sisi * sisi)
    volume = lambda sisi: sisi * sisi * sisi

print('Luas kubus\t\t:',sisi(sisi),' cm2')
print('volume kubus\t\t:',luas(sisi),'cm3')

luasDanVulomeKubus()
luasDanVulomeKubus()
luasDanVulomeKubus()