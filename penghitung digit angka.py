def hitung_digit(angka):
    return len(str(abs(angka)))

def main():
    angka = int(input("Masukkan angka: "))
    jumlah_digit = hitung_digit(angka)
    print(f"Jumlah digit dalam angka {angka} adalah {jumlah_digit}")

if __name__ == "__main__":
    main()
