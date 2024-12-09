# percabangan  
# percabangan 1 kondisi

# struktur percabangan 
"""
    1. if -yna
    2. kondisinya, statement yang harus
    terpenuhi agar aksinya dijalankan 
    3. aksinya
"""

nama = input ("masukkan nama anda! ")

# percabangan inline 
# if <kondisi> : <aksi>
# if nama == "ucup": print("Selamat Datang")
# print("Terima Kasih") # bukan aksi

# percabangan dengan indensitas
if nama == "ucup":
    print("Selamat Datang") # aksi
    print("Selamat Belajar") # aksi
print("Terima Kasih") # bukan aksi

# percabangan dengan else statement
if nama == "ucup":
    print("Selamat Datang")
else:
    print("Anda Bukan ucup")

print("Program Berakhir")