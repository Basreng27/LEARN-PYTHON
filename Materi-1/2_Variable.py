nama = "Ray" #String
umur = 23 #Int
berat_badan = 68 #Nama variable _
tinggi_badan = 1.7 #Decimal
var_list = [1, 2, 3, 4, 5] # List (bisa di ubah datanya)
var_tuple = (1, 2, 3, 4, 5) # Tuple (tidak bisa di ubah datanya)
var_colection = {1, 2, 3, 4, 5} # Colection
var_colection_dictionary = {'nama': 'Rayandra', 'umur': 23} # Colection Dictionary

bmi = berat_badan / (tinggi_badan * 2) #Perhitungan Math

#Jika Huruf Besar Berarti Const/Tidak Bisa Diubah
PI = 3.14
NAMA_APP = "TEST PYTHON"

print(bmi)
print(var_list)
print(var_tuple)
print(var_colection)
print(var_colection_dictionary)
print(var_colection_dictionary['nama'])
print(PI)

# type digunakan untuk melihat tipe data varibale
print(type(bmi))