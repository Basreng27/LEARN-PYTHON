# // Membuat Hasil Bagi Di Bulatkan
a = 9 // 5
print(a)

# Fungsi
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# Memanggil fungsi
luas = luas_persegi_panjang(5, 7)
print(f"Luas persegi panjang: {luas}")
print("=============== Fungsi ===============")

# Prosedur
def greeting(nama):
    print(f"Halo, {nama}!")

# Memanggil prosedur
greeting("Ray")
print("=============== Prosedur ===============")

# Fungsi memiliki nilai kembalian, sedangkan prosedur tidak.

# Positional Argument
def greeting (nama, usia):
    print(f"Halo, {nama}! Kamu berusia {usia} tahun.")

# Memanggil fungsi dengan argumen posisional
greeting("Ray", 24)
# Memanggil fungsi dengan argumen posisional yang terbalik 
greeting(24, "Ray")
print("=============== Positional Argument ===============")

# Keyword Argument
def greeting(nama, usia):
    print(f"Halo, {nama}! Kamu berusia {usia} tahun.")

# Memanggil fungsi dengan argumen keyword
greeting(usia=24, nama="Ray")
# Memanggil fungsi dengan argumen keyword yang terbalik
greeting(nama="Ray", usia=24)
print("=============== Keyword Argument ===============")

# Default Argument
def greeting(nama="Teman", usia=None):
    if usia is None:
        print(f"Halo, {nama}!")
    else:
        print(f"Halo, {nama}! Kamu berusia {usia} tahun.")

# Memanggil fungsi tanpa argumen
greeting()
# Memanggil fungsi dengan argumen nama
greeting("Ray")
# Memanggil fungsi dengan argumen nama dan usia
greeting("Ray", 24)

print("=============== Default Argument ===============")

# Var-Positioning Argument
def hitung_total(*args):
    total = sum(args)
    print(f"Total: {total}")

# Memanggil fungsi dengan beberapa argumen posisional
hitung_total(1, 2, 3, 4, 5)
# Memanggil fungsi dengan satu argumen posisional
hitung_total(10)
print("=============== Var-Positioning Argument ===============")

# Var-Keyword Argument
def data_diri(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Memanggil fungsi dengan beberapa argumen keyword
data_diri(nama="Ray", usia=24, pekerjaan="Programmer")
print("=============== Var-Keyword Argument ===============")

# Recursive Functions (Fungsi Yang Memangil Dirinya Sendiri)
def faktorial(n):
    if n <= 1:
        return 1
    else:
        return n * faktorial(n-1)

print(faktorial(5))
print("=============== Recursive Functions ===============")

# Lambda Expressions (Anonymus Function)
kali2 = lambda a : a * 2
print(kali2(2))

tambah = lambda a, b : a + b
print(tambah(1, 2))

faktorial = lambda n : n * faktorial(n - 1) if n > 1 else 1
print(faktorial(5))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
print("=============== Lambda Expressions ===============")
