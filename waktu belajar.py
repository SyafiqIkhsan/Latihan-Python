import time

def main():
    task = input("Lagi ngapain bray? ")
    print(f"Mulai mengerjakan: {task}")
    start_time = time.time()
    
    input("Teken 'Enter' kalo dah selese...")
    
    end_time = time.time()
    time_spent = end_time - start_time
    print(f"Waktu yang dihabiskan: {time_spent} detik")

if __name__ == "__main__":
    main()
