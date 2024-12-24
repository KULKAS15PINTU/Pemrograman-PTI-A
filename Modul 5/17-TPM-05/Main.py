# Program menghitung diskon berdasarkan membership dan total belanja

# Input data dari pengguna
member = input("Apakah Member? (ya/tidak): ").strip().lower()
total_belanja = float(input("Input total belanja (Rp): "))

# Inisialisasi variabel diskon
diskon_persen = 0

# Logika diskon
if member == "ya":
    if total_belanja > 500000:
        diskon_persen = 20
    else:
        diskon_persen = 10
else:  # Jika bukan member
    if total_belanja > 500000:
        diskon_persen = 5
    else:
        diskon_persen = 0

# Menghitung diskon dan total yang harus dibayar
diskon_rupiah = total_belanja * diskon_persen / 100
total_bayar = total_belanja - diskon_rupiah

# Output hasil perhitungan
print("\nHasil Perhitungan:")
print(f"Total Belanja: Rp. {total_belanja:,.0f}")
print(f"Diskon: {diskon_persen}%")
print(f"Diskon Rp: {diskon_rupiah:,.0f}")
print(f"Total Bayar: Rp. {total_bayar:,.0f}")