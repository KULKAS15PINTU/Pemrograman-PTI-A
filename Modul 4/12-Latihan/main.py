import datetime as dt

# Input tanggal lahir
tanggal = 11
bulan = 8
tahun = 2005

# Konversi ke tipe data date
tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir: {tanggal_lahir}")

# Tanggal hari ini
hari_ini = dt.date.today()
print(f"Hari ini: {hari_ini}")

# Hitung usia dalam hari
usia_hari = (hari_ini - tanggal_lahir).days
print(f"Usia dalam hari: {usia_hari} hari")

# Hitung usia dalam bulan (perkiraan)
usia_bulan = int(usia_hari / 30.44)  # Rata-rata hari dalam sebulan
print(f"Usia dalam bulan: {usia_bulan} bulan")