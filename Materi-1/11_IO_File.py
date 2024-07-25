# Fungsi open() pada Python adalah cara untuk mengelola operasi input dan output file, dimana fungsi ini menerima dua parameter: nama file dan mode akses yang dibutuhkan.
# Mode Akses: Terdiri dari "r" untuk membaca, "w" untuk menulis, "a" untuk menambahkan, dan "r+" untuk membaca dan menulis.
# Tambahan Mode: "t" digunakan untuk pembacaan teks (default), sedangkan "b" digunakan untuk pembacaan data binary, seperti gambar.
# Objek File: Fungsi open() mengembalikan objek file yang memungkinkan operasi lebih lanjut pada file tersebut.

# Membaca Files
# Fungsi read():
# Menggunakan fungsi read() untuk membaca seluruh isi file.
# Mengembalikan isi file sebagai string.
# Argumen opsional dapat digunakan untuk membatasi jumlah karakter yang dibaca.
f = open("IO/file.txt")
print(f.read()) # mencetak isi dari contoh_file.txt
print(f.read(5)) # mencetak Hello
f.close()

f = open("IO/file.txt")
print("=============== Fungsi Read() ===============")

# Fungsi readline():
# Menggunakan fungsi readline() untuk membaca satu baris dari file setiap kali dipanggil.
# Mengembalikan baris berikutnya setiap pemanggilan berikutnya.
f = open("IO/file.txt")
print(f.readline()) # mencetak Hello World!
print(f.readline()) # mencetak Ini contoh file.

f = open("IO/file.txt")
for x in f:
    print(x) # mencetak setiap baris yang ada di dalam file.
print("=============== Fungsi Readline() ===============")

# Menulis dan Membuat File Baru
# Proses operasi pada file melibatkan pembacaan, penambahan, dan pembuatan file baru. Dalam konteks ini, ada dua mode penting yang berperan, yakni "a" dan "w". Metode yang umum digunakan adalah white(), dan writelines().
# Metode write() memungkinkan penulisan teks ke dalam file, dengan data yang ditulis harus berbentuk string. 
# Metode writelines(), pada sisi lain, digunakan untuk menulis daftar teks ke dalam file, dengan asumsi setiap elemen dalam daftar adalah string terpisah. Metode ini menyimpan setiap elemen sebagai baris terpisah dalam file.
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
file = open("IO/file_create.txt", "w")
file.writelines(lines)  # Menulis daftar teks ke dalam file
file.close()
print("=============== Menulis dan Membuat File Baru ===============")

# Mode "a" untuk Penambahan
# Dengan menggunakan mode "a", file dapat diakses untuk menambahkan teks atau data baru tanpa menghapus yang sudah ada. Jika file tidak ada, Python akan membuatnya terlebih dahulu.
f = open("IO/contoh_file_a.txt", "a")
f.write("Hi!, ini penambahan baru pada file.") # menambahkan text pada file
f.close()
print("=============== Mode a untuk Penambahan ===============")

# Mode "w" untuk Pembuatan Baru
# Dalam mode "w", kita dapat membuat file baru untuk menulis data. Jika file dengan nama yang sama sudah ada, file tersebut akan dihapus dan digantikan dengan yang baru, sehingga perlu berhati-hati agar data yang ada sebelumnya tidak hilang.
f = open("IO/contoh_file_w.txt", "w")
f.write("Ini data baru yang menimpa data sebelumnya") 
# data sebelumnya pada file akan terhapus pada mode "w"
f.close()
print("=============== Mode w untuk Penambahan ===============")

# Menghapus Files
# Untuk menghapus file atau folder dalam Python, Anda perlu mengimpor modul os.
# Penghapusan File: os.remove("nama_file.txt") akan menghapus file dengan nama yang diberikan.
# Penghapusan Folder: os.rmdir("nama_folder") akan menghapus folder dengan nama yang diberikan jika folder tersebut kosong.
import os

os.remove("nama_file.txt") # Menghapus file
os.rmdir("nama_folder")    # Menghapus folder
print("=============== Menghapus Files ===============")

# Pengecekan File
if os.path.exists("nama_file.txt"):
    os.remove("nama_file.txt")
print("=============== Pengecekan File ===============")

# Handling Errors
#   Mode Akses   Keterangan
#   r           Membaca file, error apabila file tidak ada
#   a           Menambahkan data pada file, error apabila file tidak ada
#   w           Menulis file baru, akan membuat file baru apabila file tidak ada
#   x           Membuat file baru, error apabila file sudah ada.
f = open("contoh_file.txt", "r")
f.write("Halo lagi, ini penambahan baru pada file.") # menambahkan text pada file
f.close()

f = open("contoh_file.txt", "a")
f.read() # membaca text pada file
f.close()
print("=============== Handling Errors ===============")
