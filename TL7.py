jumlah = 0 
count = 6

for b in range(1, count + 1,2):
    print(b, end=" ")
    if b != count - 1:
        print("+", end=" ")
    jumlah = jumlah + 1

print("=", jumlah)