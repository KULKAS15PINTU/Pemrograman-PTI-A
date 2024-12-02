# Operasi Logika atau Boolean

# Operator: NOT, OR, AND

# NOT
print("==== NOT ====")
a = False
c = not a
print("Data a =", a)
print("------------------ NOT")
print("Data c =", c)

# OR (jika salah satu True, hasilnya akan True)
print("\n==== OR ====")
a = False
b = False
c = a or b
print(a, "OR", b, "=", c)
a = True
b = False
c = a or b
print(a, "OR", b, "=", c)
a = False
b = True
c = a or b
print(a, "OR", b, "=", c)
a = True
b = True
c = a or b
print(a, "OR", b, "=", c)

# AND (keduanya harus True agar hasilnya True)
print("\n==== AND ====")
a = False
b = False
c = a and b
print(a, "AND", b, "=", c)
a = True
b = False
c = a and b
print(a, "AND", b, "=", c)
a = False
b = True
c = a and b
print(a, "AND", b, "=", c)
a = True
b = True
c = a and b
print(a, "AND", b, "=", c)