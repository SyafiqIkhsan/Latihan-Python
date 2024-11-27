panjang = 10

for a in range(panjang):
    print(" " * (panjang - a) + "*" * (2 * a -1))
for a in range(panjang, 0, -1):
    print(" " * (panjang - a) + "*" * (2* a -1))
    