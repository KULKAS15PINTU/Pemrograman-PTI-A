# Operasi Komparasi

# Hasil operasi selalu bertipe boolean (TRUE/FALSE)

# Operator: >, <, ==, !=, >=, <=, is, is not

a = 4
b = 2

# Lebih besar dari >
print("==== Lebih Besar Dari (>) ====")
hasil = a > 3  # TRUE
print(a, ">", 3, "=", hasil)
hasil = b > 3  # FALSE
print(b, ">", 3, "=", hasil)
hasil = b > 2  # FALSE
print(b, ">", 2, "=", hasil)

# Kurang dari <
print("==== Kurang Dari (<) ====")
hasil = a < 3  # FALSE
print(a, "<", 3, "=", hasil)
hasil = b < 3  # TRUE
print(b, "<", 3, "=", hasil)
hasil = b < 2  # FALSE
print(b, "<", 2, "=", hasil)

# Lebih dari sama dengan >=
print("==== Lebih Dari Sama Dengan (>=) ====")
hasil = a >= 3  # TRUE
print(a, ">=", 3, "=", hasil)
hasil = b >= 3  # FALSE
print(b, ">=", 3, "=", hasil)
hasil = b >= 2  # TRUE
print(b, ">=", 2, "=", hasil)

# Kurang dari sama dengan <=
print("==== Kurang Dari Sama Dengan (<=) ====")
hasil = a <= 3  # FALSE
print(a, "<=", 3, "=", hasil)
hasil = b <= 3  # TRUE
print(b, "<=", 3, "=", hasil)
hasil = b <= 2  # TRUE
print(b, "<=", 2, "=", hasil)

# Sama dengan ==
print("==== Sama Dengan (==) ====")
hasil = a == 3  # FALSE
print(a, "==", 3, "=", hasil)
hasil = b == 3  # FALSE
print(b, "==", 3, "=", hasil)
hasil = b == 2  # TRUE
print(b, "==", 2, "=", hasil)

# Tidak sama dengan !=
print("==== Tidak Sama Dengan (!=) ====")
hasil = a != 3  # TRUE
print(a, "!=", 3, "=", hasil)
hasil = b != 3  # TRUE
print(b, "!=", 3, "=", hasil)
hasil = b != 2  # FALSE
print(b, "!=", 2, "=", hasil)

# is sebagai komparasi
print("====objek indentitiy")
x = 5
y = 5
hasil = x is y  # TRUE, karena x dan y merujuk ke objek yang sama
print(x, "is", y, "=", hasil)
print("nilai x = ", x, "id = ", hex(id(x)))
print("nilai x = ", y, "id = ", hex(id(y)))

# is not sebagai komparasi
print("====objek identity")
x = 5
y = 6
hasil = x is y  # FALSE
print(x, "is not", y, "=", hasil)
print("nilai x = ", x, "id = ", hex(id(x)))
print("nilai x = ", y, "id = ", hex(id(y)))