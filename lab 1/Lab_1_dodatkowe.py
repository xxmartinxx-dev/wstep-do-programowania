#zad 1 Dla 3 wzorów funkcji na podstawie argumentów podanych przez użytkownika wylicza się wartoś funkcji
input("Funkcja a(x) - kliknij dowolny przycisk, by podać argument")
x = int(input("Podaj argument: "))
print(x)
if x > 0:
    print("a(x) =", 2*x)
elif x == 0:
    print("a(x) =", x)
else:
    print("a(x) =", -3 * x)
input("Funkcja b(x) - kliknij dowolny przycisk, by podać argument")
x = int(input("Podaj argument: "))
print(x)
if x >= 1:
    print("b(x) =", x**2)
else:
    print("b(x) =", x)
input("Funkcja c(x) - kliknij dowolny przycisk, by podać argument")
x = int(input("Podaj argument: "))
print(x)
if x > 2:
    print("c(x) =", 2+x)
elif x == 2:
    print("c(x) =", 8)
else:
    print("c(x) =", x-4)

input("Press any key to continue...")


#zad 2 funkcja wykorzystuje operatory logiczne not i and ver. 1

print("Wpisz tak lub nie")
deszcz = input("Czy pada deszcz?")
autobus = input("Czy jest autobus?")
if (autobus == "Tak" or autobus == "tak" or autobus == "TAK") and (deszcz == "Nie" or deszcz == "NIE" or deszcz == "nie"):
    print("Dostaniesz się na uczelnie")
    print("Miłego dnia i pięknej pogody")
elif (autobus == "Tak" or autobus == "tak" or autobus == "TAK") and (deszcz == "Tak" or deszcz == "TAK" or deszcz == "tak"):
    print("Weź parasol")
    print("Dostaniesz się na uczelnie")
else:
    print("Nie dostaniesz się na uczelnię")

input("Press any key to continue...")

#zad 2 ver 2

print("Wpisz tak lub nie")
deszcz = input("Czy pada deszcz?")
autobus = input("Czy jest autobus?")
if (deszcz == "Tak") or (deszcz == "TAK") or (deszcz == "tak"):
    deszcz = 1
elif (deszcz == "Nie") or (deszcz == "NIE") or (deszcz == "nie"):
    deszcz = 0
if (autobus == "Tak") or (autobus == "tak") or (autobus == "TAK"):
    autobus = 1
elif (autobus == "Nie") or (autobus == "nie") or (autobus == "NIE"):
    autobus = 0

if autobus == 1 and deszcz == 0:
    print("Dostaniesz się na uczelnie")
    print("Miłego dnia i pięknej pogody")
elif autobus == 1 and deszcz == 1:
    print("Weź parasol")
    print("Dostaniesz się na uczelnie")
else:
    print("Nie dostaniesz się na uczelnię")

input("Press any key to continue...")

#zad 2 ver 3
print("Wpisz tak lub nie")
deszcz = input("Czy pada deszcz?")
autobus = input("Czy jest autobus?")
if deszcz == "Tak" or deszcz == "TAK" or deszcz == "tak":
    deszcz = True
elif deszcz == "Nie" or deszcz == "NIE" or deszcz == "nie":
    deszcz = False
if autobus == "Tak" or autobus == "tak" or autobus == "TAK":
    autobus = True
elif autobus == "Nie" or autobus == "nie" or autobus == "NIE":
    autobus = False

if autobus is True and not deszcz:
    print("Dostaniesz się na uczelnie")
    print("Miłego dnia i pięknej pogody")
elif autobus is True and deszcz is True:
    print("Weź parasol")
    print("Dostaniesz się na uczelnie")
else:
    print("Nie dostaniesz się na uczelnię")

input("Press any key to continue...")

# zad 3 funkcja zamienia małą literę na dużą, a dużą na małą

import string
alfabet_m = list(string.ascii_lowercase)
alfabet_d = list(string.ascii_uppercase)
litera = input("Wpisz literę: ")

def zamiana_wilkosci_liter(litera):
    if litera in alfabet_d:
        print(litera.lower())

    elif litera in alfabet_m:
        print(litera.upper())
    else:
        print("Musisz wpisa litery:")

zamiana_wilkosci_liter(litera)