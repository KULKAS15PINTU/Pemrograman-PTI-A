# Meminta input dari user untuk suhu dalam Fahrenheit
fahrenheit = float(input("masukkan suhu dalam Fahrenheit: "))

# Mengonversi Fahrenheit ke Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Menampilkan hasil konversi
print("Suhu dalam Celsius adalah:", round(celsius, 2))