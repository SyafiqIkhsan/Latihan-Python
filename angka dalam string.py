def main():
    nomor = input("Masukkan angka: ")
    digit_sum = sum(int(digit) for digit in nomor)
    print(f"Jumlah digit dalam {nomor} adalah {digit_sum}")

if __name__ == "__main__":
    main()
