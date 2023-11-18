import random
# zad 1 sprawdzanie typów wyników działań

print(type(1 + 2))
print(type(1 + 4.5))
print(type(3 / 2))
print(type(4 / 2))
print(type(3 // 2))
print(type(-3 // 2))
print(type(11 % 2))
print(type(2 ** 10))
print(type(8 ** (1/3)))

input("Press any key to continue...")


# zad 2 wyjasnienie działań poszczególnych instrukcji

# zmiana liczby w nawiasie na l. całkowitą
print(int(3.0))
# zmiania liczby w nawiasie na liczbę zmiennoprzecinkową
print(float(3))
# zmiana stringa w nawiasie na liczbę zmiennoprzecinkową
print(float("3"))
# zmiana liczby na tekst
print(str(12.4))
# Zmiana liczby na zmienną boolean - prawda/fałsz
print(bool(0))

input("Press any key to continue...")


# zad 3 skrypt pobiera długości boków i oblicza pole i obwód

print("Obliczamy pole prostokąta:")

a = int(input("Podaj 1 bok:"))
b = int(input("Podaj 2 bok:"))

pole = (a*b)
obwod = 2*a + 2*b

print("Pole prostokąta =", pole, "Obwód prostokąta =", obwod)

input("Press any key to continue...")


# zad 4 skrypt pobiera od użzytkownika drogę oraz średnie spalanie (na 100km) i przewiduje zużycie paliwa

print("Obliczamy zużycie paliwa - podaj dane")

droga = round(float(input("Podaj droge:")), 2)
spalanie = round(float(input("Podaj śr. spalanie:")), 2)
cena = 6.5

zuzycie = round(droga*spalanie/100, 2)
koszt = round(zuzycie*cena, 2)

print("Zużycie paliwa:", zuzycie, "Koszt:", koszt)

input("Press any key to continue...")


# zad 4.1 skrypt losuje drogę oraz średnie spalanie (na 100km) i przewiduje zużycie paliwa

print("Obliczamy zużycie paliwa - losowe dane")

droga = round(float(random.randint(1, 10000)), 2)
print("Droga = ", droga)
spalanie = round(float(random.randint(1, 30)), 2)
print("Spalanie = ", spalanie)
cena = 6.5

print("Cena = ", cena)
print("Droga:", droga, "Spalanie:", spalanie)
zuzycie = round(droga*spalanie/100, 2)
koszt = round(zuzycie*cena, 2)

print("Zużycie paliwa:", zuzycie, "Koszt:", koszt)

input("Press any key to continue...")


# zad 5 skrypt wyliczający zużycie paliwa z modyfikacją na wykorzystanie f-string

print("Obliczamy zużycie paliwa - losowe dane z użyciem f-string")

droga = round(float(random.randint(1, 10000)), 2)
print(f'Droga {droga}')
spalanie = round(float(random.randint(1, 30)), 2)
print(f'Spalanie {spalanie}')
cena = 6.5
print(f'Cena {cena}')

print(f'Droga: {droga} Spalanie: {spalanie}')
zuzycie = round(droga*spalanie/100, 2)
koszt = round(zuzycie*cena, 2)
print(f'Zużycie paliwa: {zuzycie} Koszt: {koszt}')

input("Press any key to continue...")


print("Obliczamy pole prostokąta - losowe dane z użyciem f-string")

a = int(random.randint(1, 100))
print(f'a = {a}')
b = int(random.randint(1, 100))
print(f'b = {b}')

pole = (a*b)
obwod = 2*a + 2*b

print(f'Pole prostokąta = {pole} Obwód prostokąta = {obwod}')
