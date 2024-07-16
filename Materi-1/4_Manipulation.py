# Merubah Tipe Data
a = '5'
int(a) #floast(), str(), bool()
print(a)

# Merubah Huruf Besar Kecil
text = "hallo ges"

lower = text.lower()
upper = text.upper()
capitalize = text.capitalize()

print(lower)
print(upper)
print(capitalize)

# Menghapus whitespace pada sebelah kanan atau akhir string
print("Hallo          ".rstrip())

# Menghapus whitespace pada sebelah kiri atau awal string
print("          Hallo".lstrip())

# Menghapus whitespace pada awal dan akhir string
print("          Hallo          ".strip())

# Menghapus karakter pada awal dan akhir string
kata = 'aaaaaHalloaaaaa'
print(kata.strip("a"))

# Menemukan suatu kata pada awal string
print('Hallo World'.startswith('Hallo'))

# Menemukan suatu kata pada akhir string
print('Hallo World'.endswith('Hallo'))

# Memisahkan kata
a = "Hello World !"
print(a.split())
print(a.split()[1])

# Contoh pemisahan string berdasarkan koma
data = "apel, jeruk, nanas, mangga, anggur"
buah = data.split(", ")
print(buah)
print(buah[2])

# Penggabungan/Concatenation
# +
a = "Hello"
b = "World"
c = a + " " + b
print(c) 

# join()
a = ["Selamat", "Pagi", "Semua"]
b = ", ".join(a)
print(b)

# Mengganti bagian text/Replace
a = "Hello World"
b = a.replace("World", "Everyone")
print(b) 

# Pengecekan Huruf Kapital
print('RAY'.isupper())

# Pengecekan Huruf Kecil
print('ray'.islower())

# Pengecekan Huruf Alfabet
print('Ray'.isalpha())

# Pengecekan Alfanumerik
print('Ray12'.isalnum())

# Pengecekan Angka
print('123'.isdecimal())

# Pengecekan whitespace
print('      '.isspace())

# Pengecekan Huruf Kapital pada Awal Kata
print('Ray Wan'.istitle())

nama = "Ray"
umur = 23
# Menambahkan variabel ke dalam string (format())
print("Nama saya {}, dan umur saya {} tahun".format(nama, umur))

# Menggunakan f-string
print(f"Nama saya {nama}, dan umur saya {umur} tahun")

# Menambahkan argumen pada fungsi print()
print("Nama saya", nama, "dan umur saya", umur, "tahun", sep=", ", end=".\n")

# Menggunakan operator %
print("Nama saya %s, dan umur saya %d tahun" % (nama, umur))

# Menggunakan metode str.format_map()
# print("Nama saya {nama}, dan umur saya {umur} tahun".format_map(data))
