def buat_persegi(n):
    for i in range(n):
        print("* " * n)

def main():
    ukuran = int(input("Masukkan ukuran persegi (n): "))
    print("Pola Persegi:")
    buat_persegi(ukuran)

if __name__ == "__main__":
    main()
