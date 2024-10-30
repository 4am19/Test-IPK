# Deklarasi variabel
ipk = float(input("Masukkan IPK: "))
sks_maks = 0

# Hitung SKS maksimum berdasarkan IPK
if ipk < 2.75: (tombol A)
    sks_maks = 16 (kondisi)
elif 2.75 <= ipk < 4.0: (tombol B)
    sks_maks = 22 (kondisi)
else: (tombol C)
    sks_maks = lebih dari 22 (kondisi) # Anda bisa mengubah nilai ini sesuai kebijakan

# Tampilkan hasil
print("SKS maksimum yang dapat diambil:", sks_maks)

#Pengujian Path Coverage:
Jalur 1: input ipk < 2.75 (tombol A), sks_maks = 16
Jalur 2: input 2.75 <= ipk < 4.0 (tombol B), sks_maks = 22
Jalur 3: input ipk < 4.0 (tombol c), sks_maks = lebih dari 22