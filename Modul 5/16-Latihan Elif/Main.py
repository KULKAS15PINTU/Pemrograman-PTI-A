# Program penilaian berdasarkan rentang nilai

# Input nilai dari pengguna
nilai = float(input("Masukkan nilai (bisa menggunakan koma, contoh: 82.5): "))

# Menentukan grade berdasarkan nilai
if nilai > 90:
    grade = "A"
elif 81 <= nilai <= 90:
    grade = "A-"
elif 75 <= nilai <= 80:
    grade = "B+"
elif 70 <= nilai <= 74:
    grade = "B"
elif 65 <= nilai <= 69:
    grade = "C+"
elif 60 <= nilai <= 64:
    grade = "C"
elif 55 <= nilai <= 59:
    grade = "D"
else:
    grade = "E"

# Menampilkan hasil
print(f"Nilai Anda: {nilai}")
print(f"Grade Anda: {grade}")