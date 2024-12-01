from datetime import datetime

now = datetime.now()
tanggalSekarang = now.strftime(f"%A, %d {'of'} %B {'on'} %Y, %I-%M-%S %p")
print(tanggalSekarang)