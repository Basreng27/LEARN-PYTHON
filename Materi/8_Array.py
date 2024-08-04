# Dalam python ada beberapa tipe data yang memiliki konsep penyimpanan nilai yang mirip dengan array dalam bahasa pemrograman lain. 
# Contohnya: list, tuple, set, string, dan dictionary
# Array
lst = ["Ray", 10, 100.5, False, "ini kalimat"]

print(lst[0])
print(lst[-1]) 
print(lst[2:4])
print(type(lst[3])) 
print("=============== Array ===============")

# Untuk mengakses elemen pada dictionary dapat dilakukan dengan:
# Menggunakan kurung siku [ ] dengan key didalamnya, atau menggunakan get() untuk mendapatkan valuenya
# Menggunakan keys() untuk mendapatkan semua list key
# Menggunakan values() untuk mendapatkan selua list value
# Menggunakan items() untuk mendapatkan pasangan key value dari sebuah dictionary dalam bentuk list berisikan sebuah tuple.

# Element Array
makanan = {"apel": 5000, "pisang": 3000, "jeruk": 4000, "anggur": 8000}

print(makanan["apel"])
print(makanan.get("pisang"))

key_list = makanan.keys()
print(key_list)

value_list = makanan.values()
print(value_list)

item_list = makanan.items()
for key, value in item_list:
    print(key + ": " + str(value))
print("=============== Element Array ===============")

# Check Item Array
buah = {"apel": 5000, "pisang": 3000, "jeruk": 4000, "anggur": 8000}

if "apel" in buah:
    print("Apel termasuk salah satu buah")
print("=============== Check Item Array ===============")

# Replace Array Value
warna = ["merah", "kuning", "biru", "abu"]
warna[-1] = "ungu" 
print(warna)

buah = {"apel": 5000, "pisang": 3000, "jeruk": 4000}

buah["jeruk"] = 4500 # mengganti value
print(buah)
buah["mangga"] = 6000 # menambahkan elemen baru
print(buah)
buah.update({"anggur": 7000, "pisang": 3500}) # menambahkan dan mengganti elemen
print(buah)

print("=============== Replace Array Value ===============")

# Untuk menambahkan elemen baru ke list dapat menggunakan:
# Append(): Metode ini digunakan untuk menambahkan elemen ke akhir dari suatu list.
# Insert(): Metode ini memungkinkan kita untuk menambahkan elemen baru ke dalam list pada posisi yang kita tentukan dengan menyediakan indeks tertentu.
# Extend(): Metode extend() digunakan untuk menambahkan elemen-elemen dari suatu iterable (seperti list, tuple, atau string) ke akhir list.

# Add Item Array
warna = ["merah", "kuning"]

warna.append("hijau")
print(warna)
warna.insert(1, "jingga") 
print(warna)
warna2 = ["biru", "nila", "ungu"]
print(warna)
warna.extend(warna2) 
print(warna)
print("=============== Add Item Array ===============")

# Untuk menghapus elemen pada list dapat menggunakan:
# remove(): Hapus elemen dengan nilai tertentu dari list menggunakan nilai sebagai argumen.
# pop(): Keluarkan dan hapus elemen berdasarkan indeks; tanpa argumen mengeluarkan elemen terakhir.
# del: Menghapus elemen berdasarkan indeks atau bahkan variabel
# clear(): Hapus semua elemen dalam list tanpa argumen

# Remote Item Array
warna = ["merah", "jingga", "kuning", "hijau", "biru"]

warna.remove("hijau") 
print(warna)
warna.pop(1) 
print(warna)
warna.pop() 
print(warna)
del warna[0] 
print(warna)
warna.clear()
print(warna)

buah = {"apel": 5000, "pisang": 3000, "jeruk": 4000}

buah.pop("pisang")
print(buah)
print("=============== Remove Item Array ===============")

# Oprasi Array
# Len (Menghitung Array)
contoh_list = [1, 3, 3, 5, 7, 7, 9]

print(len(contoh_list))
print("=============== Len ===============")

# Min() dan Max() (Menentukan Nilai terkecil dan terbesar)
angka = (13, 7, 96, 84, 71)

print(min(angka))
print(max(angka))
print("=============== Min() dan Max() ===============")

# Count() (Menghitung Berapakali Muncul)
word = "Hallo World!"

print(word.count('l'))
print("=============== Count() ===============")

# Short (Mengurutkan)
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()

print(kendaraan)
print("=============== Short() ===============")

# Copy() (Membuat Salinan Yang Tidak Terhubung Dengan Yang Aslinya)
list_asli = [1, 2, 3, 4, 5]
list_salinan = list_asli.copy()

list_salinan.append(6)
print(list_asli)
print(list_salinan)
print("=============== Copy() ===============")

# Index() (Melihat Index)
string_kalimat = "Belajar Python"

indeks_a = string_kalimat.index("a")  
print(indeks_a)
print("=============== Index() ===============")

# Reverse() (Membalik Element Array)
list_angka = [1, 2, 3, 4, 5]

list_angka.reverse()
print(list_angka)
print("=============== Reverse() ===============")

# Memberikan Nilai untuk Multiple Variable
data = ['shirt', 'white', 'L']
apparel, color, size = data

print(apparel)
print(color)
print(size)
print("=============== Memberikan Nilai untuk Multiple Variable ===============")
