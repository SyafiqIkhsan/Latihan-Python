def hitung_kata(kalimat):
    return len(kalimat.split())

def main():
    kalimat = input("Masukkan kalimat: ")
    jumlah_kata = hitung_kata(kalimat)
    print(f"Jumlah kata dalam kalimat: {jumlah_kata}")

if __name__ == "__main__":
    main()
