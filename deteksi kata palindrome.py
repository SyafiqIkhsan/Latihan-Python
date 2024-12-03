# Program Palindrom

def cek_palindrom(s):
    return s == s[::-1]

def main():
    kata = input("Masukkan kata atau kalimat: ").replace(" ", "").lower()
    
    if cek_palindrom(kata):
        print(f"'{kata}' adalah palindrom.")
    else:
        print(f"'{kata}' bukan palindrom.")

if __name__ == "__main__":
    main()
