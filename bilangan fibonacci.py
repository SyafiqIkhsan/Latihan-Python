def fibonacci(n):
    f1, fb2 = 0, 1
    for _ in range(n):
        print(f1, end=" ")
        f1, f2 = f2, f1 + f2

def main():
    num = int(input("Jumlah bilangan Fibonacci: "))
    fibonacci(num)

if __name__ == "__main__":
    main()
