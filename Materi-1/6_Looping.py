# For
angka = [1, 2, 3, 4, 5]

for bilangan in angka:
    print(bilangan * 2)
print("=============== For ===============")

# While
x = 1

while x <= 10:
    print(x)
    x += 1
print("=============== While ===============")

# Nested Loop
huruf_awal = ["A", "B", "C"]
angka_akhir = [1, 2, 3]

for huruf in huruf_awal:
    for angka in angka_akhir:
        print(huruf + str(angka))
print("=============== Nested Loop ===============")

# Kontrol Perulangan
# Break (Menghentikan Jika Kondisi Terpenuhi)
for i in range(10):
    print(i)
    if i == 5:
        break
print("=============== Break ===============")

# Continue (Melanjutkan Kondisi)
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
print("=============== Continue ===============")

# Else Setelah For (Jika Tidak Ada Element/Data Yang Diloop)
for x in range(10):
    if x % 2 == 0:
        continue
    print(x, "adalah ganjil")
else:
    print("Selesai")
print("=============== Else Seleteah For ===============")

# Else Setelah While (Jika Tidak Ada Element/Data Yang Diloop)
i = 0
while i < 10:
    print(i)
    i += 1
else:
    print("Perulangan selesai")
print("=============== Else Seleteah While ===============")

# Pass (Placeholder Untuk Menunjukkan Bahwa Tidak Ada Operasi)
for i in range(10):
    if i % 2 == 0:
        pass
    else:
        print(i)
print("=============== Pass ===============")

# List Comprehension
# cara yang ringkas dan efisien untuk membuat list baru berdasarkan list yang sudah ada
bilangan_ganjil = [x for x in range(1, 11) if x % 2 != 0]

print(bilangan_ganjil)
print("=============== List Comprehesion ===============")

# Looping Through Dict
makanan = {"apel": 5000, "pisang": 3000, "jeruk": 4000, "anggur": 8000}

for buah in makanan:
    print(buah)
    print(makanan[buah])
print("=============== Looping Through Dict ===============")
