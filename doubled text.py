text = input("masukkan kalimat: ")

doubled_text = ''.join(char * 2 for char in text)

print(f"Teks pertama: {text}")
print(f"Teks setelah huruf digandakan: {doubled_text}")