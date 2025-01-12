# Nilai potongan tetap untuk member
potongan_tetap = 5  # Ganti dengan nilai potongan tetap yang diinginkan

# Input data pelanggan
nama = input("Masukkan nama pelanggan: ")
member = input("Apakah pelanggan memiliki kartu member? (ya/tidak): ").lower() == "ya"
total_belanja = float(input("Masukkan total belanja: "))

# Inisialisasi variabel diskon
diskon_persen = 0

# Perhitungan diskon berdasarkan status member dan total belanja
if member:
    if total_belanja >= 500000:
        diskon_persen = 10
    elif total_belanja >= 100000:
        diskon_persen = potongan_tetap
    else:
        diskon_persen = 3
else:
    if total_belanja >= 100000:
        diskon_persen = 3

# Hitung diskon dalam rupiah dan total yang harus dibayar
diskon_rupiah = total_belanja * diskon_persen / 100
total_bayar = total_belanja - diskon_rupiah

# Cetak hasil
print(f"Nama Pelanggan: {nama}")
print(f"Status Member: {'Member' if member else 'Non-Member'}")
print(f"Total Belanja Sebelum Potongan: Rp {total_belanja:,}")
print(f"Diskon: {diskon_persen}%")
print(f"Diskon (Rupiah): Rp {diskon_rupiah:,}")
print(f"Total Belanja Setelah Potongan: Rp {total_bayar:,}")
print("-" * 30)