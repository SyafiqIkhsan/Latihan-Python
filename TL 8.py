jumlah = 0 
count = 10

for c in range(2, count + 1, 2):
    print(c, end=" ")
    if c != count - 1:
        print("+", end=" ")
    jumlah = jumlah + 1

print("=", jumlah)