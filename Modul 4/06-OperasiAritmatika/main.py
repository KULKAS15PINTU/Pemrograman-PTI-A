# operasi aritmatika

a = 10
b = 3

# Operasi penjumlahan (TAMBAH)
print("==== TAMBAH ====")
hasil = a + b
print(a, "+", b, "=", hasil)

# Operasi pengurangan (KURANG)
print("==== KURANG ====")
hasil = a - b
print(a, "-", b, "=", hasil)

# Operasi perkalian (KALI)
print("==== KALI ====")
hasil = a * b
print(a, "*", b, "=", hasil)

# Operasi pembagian (BAGI)
print("==== BAGI ====")
hasil = a / b
print(a, "/", b, "=", hasil)

# Operasi pemangkatan (EKSPONENSIAL)
print("==== EKSPONENSIAL ====")
hasil = a ** b
print(a, "", b, "=", hasil)

# Operasi sisa bagi (MODULUS)
print("==== MODULUS ====")
hasil = a % b
print(a, "%", b, "=", hasil)

# Operasi floor division
print("==== FLOOR DIVISION ====")
hasil = a // b
print(a, "//", b, "=", hasil)

# Prioritas perhitungan (operasi)
"""
   1. ()
   2. Perkalian, pembagian, eksponen, modulus, floor division (*, /, **, %, //)
   3. Penjumlahan dan pengurangan (+, -)
"""

x = 3
y = 4
z = 2

hasil = x**z * (y + x)  / z - z % y // x
print(x,"**",z, "*", y, "+", x, "/", z, "-", z, "%", y, "//", x, "=", hasil)

hasil = x + y * z
print(x, "+", y, "*", z, "=", hasil)
hasil = (x + y) * z
print("(",x, "+",y,")", "*", z, "=", hasil)