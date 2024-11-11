import math

# nilai jari-jari
r = float(input("masukkan nilai jari-jari lingkaran: "))

# nilai pi dari modul math
luas_lingkaran = math.pi * (r ** 2)

# hasil
print("Luas lingkaran dengan jari-jari", r, "adalah:", round(luas_lingkaran, 2))