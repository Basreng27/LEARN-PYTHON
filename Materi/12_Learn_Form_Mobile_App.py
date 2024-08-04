# Menghitung Total Kata/Panjang
len("Data")

s = "www.Learn.com     "
# Mengecek Apakah Awalan Hurufnya www
s.startswith('www',) # Output Boolean
s.startswith('www', 0, 5) # Output Boolean Dengan Mengetahui Index ke 0 sampai 5
# Mengecek Apakah Awalan Hurufnya www
s.endswith('com') # Output Boolean
s.replace('.', ' ') # Replace . Menjadi "Spasi"
s.replace('.', ' ', 1) # Replace . Menjadi "Spasi" Tapi Hanya 1 Saja
s.swapcase() # Merubah Huruf Besar Ke Kecil Dan Sebalinya
s.capitalize() # Merubah Huruf Besar Awalan Kalimat
s.upper() # Merubah Huruf Besar Semua
s.lower() # Merubah Huruf kecil Semua
s.title() # Merubah Huruf Besar Setiap Kata
s.strip() # Menghilangkan Spasi Kiri Kanan
s.rstrip() # Menghilangkan Spasi Kanan
s.lstrip() # Menghilangkan Spasi Kiri
dir(s) # Melihat Method Yang Bisa Digunakan
s[3] # Index Ke 3 = .
s[3:10] # Slicing = Mengambil Nilai
# Slicing Dari Depan Di Mulai Dari 0 Dan Dari Belakang -1
s[-3]