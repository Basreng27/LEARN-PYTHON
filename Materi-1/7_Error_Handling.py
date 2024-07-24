# try…except…finally…
def bagi(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Tidak boleh membagi dengan 0!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        print("Operasi bagi selesai")

bagi(10, 2)
bagi(10, 0)
print("=============== try…except…finally ===============")

# Raise Exception
def cek_umur(umur):
    if umur < 18:
        raise ValueError("Usia minimal 18 tahun")
    else:
        print(f"Usia Anda {umur} tahun")

cek_umur(17)  # Output: ValueError: Usia minimal 18 tahun
cek_umur(20)  # Output: Usia Anda 20 tahun
print("=============== Raise Exception ===============")