# Mengenal String
# String adalah kumpulan karakter

data = "ini adalah string"
print(data)
print(type(data))  # Menampilkan tipe data string

# 1. Cara Membuat String
"""
   String dapat dibuat dengan:
   1. Menggunakan single quote ('...')
   2. Menggunakan double quote ("...")
"""

# Contoh single quote
data = 'Menggunakan Single Quote'
print(data)

# Contoh double quote
data = "Menggunakan Double Quote"
print(data)

# String dengan tanda petik dalam teks
print("ini hari jum'at")
print('nama saya "ucup"')

# 2. Menggunakan Tanda Escape (\)
# Membuat tanda ' menjadi bagian dari string
print('mari sholat jum\'at')

# Menulis path file dengan tanda backslash
print('c:\\user\\ucup')

# Menggunakan tab (\t)
print("ronaldo\t\tmessi")  # Tab dua kali
print("MU\t\tJuara")

# Menggunakan backspace (\b)
print("MU\bJuara")  # Menghapus karakter sebelum \b

# Menggunakan newline (\n)
print("baris pertama.\nbaris kedua.")  # LF (Line Feed)
print("baris pertama.\r\nbaris kedua.")  # CRLF (Carriage Return + Line Feed)

# 3. Raw String
# Raw string digunakan agar karakter escape (\) tidak diproses
print(r'c:\user\ucup')