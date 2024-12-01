import random

def main():
    print("Selamat datang di permainan Tebak Angka!")
    angka_rahasia = random.randint(1, 100)
    tebakan = None
    percobaan = 0
    
    while tebakan != angka_rahasia:
        tebakan = int(input("Tebak angka antara 1 dan 100: "))
        percobaan += 1
        
        if tebakan < angka_rahasia:
            print("Terlalu rendah!")
        elif tebakan > angka_rahasia:
            print("Terlalu tinggi!")
        else:
            print(f"Selamat! Anda menebak angka {angka_rahasia} dengan {percobaan} percobaan.")

if __name__ == "__main__":
    main()
