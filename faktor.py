def main():
    angka = int(input("Masukkan sebuah angka: "))
    
    print(f"Faktor-faktor dari {angka} adalah:")
    for i in range(1, angka + 1):
        if angka % i == 0:
            print(i)

if __name__ == "__main__":
    main()
