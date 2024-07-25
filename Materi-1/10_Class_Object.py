# Class
class Hewan:
    pass

# Object
class Hewan:
    pass

hewan_1 = Hewan()

# Atribut Class
class Hewan:
    nama = "Hewan"
    jenis = "Kucing"

hewan = Hewan()
print(hewan.nama)
print(hewan.jenis)
print("=============== Atribut Class ===============")

# Class Constructor (Fungsi Yang Paling Pertama Dijalankan __init__)
class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

kucing1 = Hewan("Kitty", "Mamalia")

print(kucing1.nama)
print(kucing1.jenis)
print("=============== Class Constructor ===============")

# Method - Object Method
class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def makan(self):
        print(f"{self.nama} sedang makan.")

kucing1 = Hewan("Kitty", "Mamalia")
print(kucing1.nama)
kucing1.makan()
print("=============== Method - Object Method ===============")

# Method - Static Method
class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    @staticmethod
    def kategorikan_hewan(jenis):
        if jenis in ["Mamalia", "Unggas", "Reptil", "Ikan"]:
            print(f"{jenis} adalah hewan.")
        else:
            print(f"{jenis} bukan hewan.")

Hewan.kategorikan_hewan("Mamalia")
print("=============== Method - Static Method ===============")

# Method - Class Method
class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    @classmethod
    def kategorikan_hewan(cls, nama_hewan):
        if nama_hewan in ["Kucing", "Anjing"]:
            kategori = "Hewan Peliharaan"
        else:
            kategori = "Hewan Liar"
        return kategori

burung1 = Hewan("Cici", "Burung")
kategori_burung = Hewan.kategorikan_hewan("Burung")

print(f"Kategori {burung1.nama}: {kategori_burung}")
print("=============== Method - Class Method ===============")

# Inheritance (Pewarisan)
class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def makan(self):
        print(f"{self.nama} sedang makan.")

class Kucing(Hewan):
    def bersuara(self):
        print(f"{self.nama} mengeong.")

kucing1 = Kucing("Kitty", "Mamalia")
kucing1.bersuara()
print("=============== Inheritance (Pewarisan) ===============")

# Super (Mengambil Function Didalam Function)
class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def makan(self):
        print(f"{self.nama} sedang makan.")

class Kucing(Hewan):
    def makan(self):
        super().makan()
        print("... dan minum susu.")

kucing1 = Kucing("Kitty", "Mamalia")
kucing1.makan()
print("=============== Super ===============")
