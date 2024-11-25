# opersi assignment adalah operasi yang dapat dilakukan dengan meringkas 
# operasi ditambah dengan assignment

a= 5 # assignment # tidak memakan memory karena dia literal (gak ada variabelnya)
print("nilai a = ", a)

a += 1 # artinya a = a += 1
print("nilai a += 1, nilai a menjadi = ", a)

a -= 1 # artinya a = a -= 1
print("nilai a -= 1, nilai a menjadi = ", a)

a *= 5 # artinya a = a *= 5
print("nilai a *= 5, nilai a menjadi = ", a)

a /= 5 # artinya a = a /= 5
print("nilai a /= 5, nilai a menjadi = ", a)

# modulus dan floordivision
# %=, //=
a %= 3 # artinya a = a %= 5
print("nilai a %= 5, nilai a menjadi = ", a)

a //= 1 # artinya a = a //= 5
print("nilai a //= 5, nilai a menjadi = ", a)

# pangkat / eksponen
# **=
a **= 10 # artinya a = a //= 5
print("nilai a //= 5, nilai a menjadi = ", a)

# operasi logika

# or
c = True
print("nilai c = ", c)
c |= False # artinya c = or false 
print("nilai c |= False, menjadi c = ", c)
c = True # artinya c = or true
print("nilai c |= True, menjadi c = ", c)

# and
c = True
print("nilai c = ", c)
c &= False # artinya c = and false
print("nilai c &= False, menjadi c = ", c)