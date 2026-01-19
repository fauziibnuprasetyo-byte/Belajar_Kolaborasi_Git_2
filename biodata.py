# Program Biodata Sederhana

print("=== PROGRAM BIODATA DIRI ===")

# Mengambil input dari pengguna
nama          = input("Masukkan Nama Lengkap: ")
panggilan     = input("Masukkan Nama Panggilan: ")
umur          = input("Masukkan Umur: ")
kota_asal     = input("Masukkan Kota Asal: ")
hobi          = input("Masukkan Hobi: ")

# Menampilkan hasil biodata
print("\n" + "="*25)
print("      BIODATA DIRI      ")
print("="*25)
print(f"Nama Lengkap   : {nama}")
print(f"Nama Panggilan : {panggilan}")
print(f"Umur           : {umur} Tahun")
print(f"Kota Asal      : {kota_asal}")
print(f"Hobi           : {hobi}")
print("="*25)
print("Terima kasih sudah mengisi!")
