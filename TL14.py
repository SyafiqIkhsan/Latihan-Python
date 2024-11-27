panjang = 10

for x in range(panjang):
    print("*" * (x+1))
    if panjang == x+1:
        print("*" * (x + 5))
for x in range(panjang, 0, -1):
    print("*" * x)