def persegi():
    sisi = int(input('sisi\t\t:'))
    luas = lambda s: s * s
    keliling = lambda s: 4 * s 

    print('Luas\t\t:',luas(sisi), 'cm2')
    print('Keliling\t: ',keliling(sisi),'cm2')

    rata2 = lambda nilai1,nilai2,nilai3 : (nilai1+nilai2+nilai3)/3

    print(rata2(90,88,76))


