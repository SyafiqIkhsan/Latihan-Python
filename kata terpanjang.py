def main():
    kalimat = input("Masukkan kalimat: ")
    kata = kalimat.split()
    
    terpanjang = max(kata, key=len)
    print(f"Kata terpanjang: {terpanjang}")

if __name__ == "__main__":
    main()
