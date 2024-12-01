def main():
    angka = int(input("Masukkan angka untuk tabel perkalian: "))
    
    print(f"Tabel perkalian {angka}:")
    for i in range(1, 11):
        print(f"{angka} x {i} = {angka * i}")

if __name__ == "__main__":
    main()
