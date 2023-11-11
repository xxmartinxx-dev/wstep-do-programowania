x = 5
print("Obliczamy pole prostokąta:")

y = int(input("Podaj 1 bok:"))
x = int(input("Podaj 2 bok:"))
pole = (y*x)
print("Pole prostokąta =", pole)

print("Obliczamy zużycie paliwa - podaj dane")
droga = float(input("Podaj droge:"))
spalanie = float(input("Podaj śr. spalanie:"))
cena = 6.5

zuzycie = droga*spalanie/100
koszt = zuzycie*cena
print("Zużycie paliwa:",zuzycie, "Koszt:", koszt)

print("Obliczamy zużycie paliwa - losowe dane")
import random

droga = float(random.randint(1, 10000))
spalanie = float(random.randint(1, 30))
cena = 6.5
print("Droga:", droga, "Spalanie:", spalanie)
zuzycie = droga*spalanie/100
koszt = zuzycie*cena
print("Zużycie paliwa:", zuzycie, "Koszt:", koszt)
