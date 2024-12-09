def hadiah_belanja(total_belanja):
  """Fungsi untuk menentukan hadiah berdasarkan total belanja.

  Args:
    total_belanja: Total belanja dalam rupiah.

  Returns:
    Hadiah yang didapatkan.
  """

  if total_belanja >= 500000:
    return "Selamat! Anda mendapatkan hadiah mouse dan keyboard."
  else:
    return "Terima kasih sudah berbelanja. Anda mendapatkan gantungan kunci."

# Input total belanja dari pengguna
total_belanja = int(input("Masukkan total belanja Anda: "))

# Panggil fungsi dan tampilkan hasil
hadiah = hadiah_belanja(total_belanja)
print(hadiah)