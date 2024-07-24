# If
bilangan = 22

if bilangan > 0:
    print("Bilangan Positif")
elif bilangan < 0:
    print("Bilangan Negatif")
else :
    print("Nol")
print("=============== If ===============")

# Tenary Atau If Sebaris
is_adult = (bilangan >= 18)

message = "Dewasa" if is_adult else "Anak-anak"
print(message)
print("=============== Tenary Atau If Sebaris ===============")

# Tenary Tuple
age = ("Dewasa", "Anak-anak") [bilangan <= 33]
print(age)
print("=============== Tenary Tuple ===============")