jumlah = 0
count = 6

for a in range(1, count):
    print(a,end=" ")
    if a != count - 1:
        print("+", end=" ")
    jumlah = jumlah + a

print("=",jumlah)