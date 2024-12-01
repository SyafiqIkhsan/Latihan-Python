import random

def main():
    angka1 = random.randint(1, 10)
    angka2 = random.randint(1, 10)
    print(f"Berapa hasil dari {angka1} + {angka2}?")
    answer = int(input())
    
    if answer == angka1 + angka2:
        print("Jawaban Anda benar!")
    else:
        print("Jawaban Anda salah.")

if __name__ == "__main__":
    main()
