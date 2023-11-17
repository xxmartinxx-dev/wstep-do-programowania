"""import string
alfabet_d = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
alfabet_m = alfabet_d.lower()
litera = input("Podaj literę: ")
for litera in alfabet_d:
    print("Duża litera")
else:
    print("Mała litera")"""
import string
print(string.ascii_lowercase)
alfabet_m = list(string.ascii_lowercase)
alfabet_d = list(string.ascii_uppercase)
litera = input("Podaj literę: ")
for litera in alfabet_d:
    print("Duża litera")
else:
    print("Mała litera")
