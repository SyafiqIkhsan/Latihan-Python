def sensus_usia():
    #Menyimpan data usia
    usia = []
    
    # Input jumlah penduduk
    jumlah_penduduk = int(input("Masukkan jumlah penduduk: "))
    
    # Mengumpulkan data usia
    for i in range(jumlah_penduduk):
        umur = int(input(f"Masukkan usia penduduk ke-{i + 1}: "))
        usia.append(umur)

    # Menghitung orang paling tua dan termuda
    if len(usia) < 2:
        print("Jumlah penduduk harus lebih dari satu untuk menemukan orang tua dan muda kedua.")
        return

    # Mengurutkan data usia
    usia.sort()
    
    # Mendapatkan orang paling tua dan paling muda
    orang_paling_tua = usia[-1]
    orang_tua_kedua = usia[-2]
    orang_pertama_termuda = usia[0]
    orang_termuda_kedua = usia[1]

    # Menampilkan hasil
    print(f"Jumlah penduduk: {jumlah_penduduk}")
    print(f"Orang paling tua: {orang_paling_tua} tahun")
    print(f"Orang kedua paling tua: {orang_tua_kedua} tahun")
    print(f"Orang pertama termuda: {orang_pertama_termuda} tahun")
    print(f"Orang kedua termuda: {orang_termuda_kedua} tahun")

# Menjalankan aplikasi sensus usia
sensus_usia()
