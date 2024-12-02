# string
nama = "ucup"
format_str = f"Hallo {nama}"
print(format_str)
print("Hallo", nama)
      
# boolean
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)
# Baris ini dihapus karena duplikat
# format_str = f"boolean = {boolean}"
# print(format_str)
      
# angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000000 # 2,000,000
format_str = f"jutaan = {angka:,}" # Menambahkan koma sebagai pemisah ribuan
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.3f}" # Membatasi 3 angka di belakang koma
print(format_str)

# menampilkan tanda + dan -
angka_minus = -10
angka_plus = +10.1234
format_minus = f"minus = {angka_minus:+d}" 
format_plus = f"plus = {angka_plus:+.2f}" # Menambahkan tanda + 
print(format_minus)
print(format_plus)

# format persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}" # Menampilkan dalam format persen
print(format_persen)