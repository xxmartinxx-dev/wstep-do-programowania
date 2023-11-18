import string
import math

#zad 1
wiek = int(input("Wprowadź wiek klienta: "))
if wiek > 18:
    cena = 20
    print(f'Cena biletu: {cena}')
elif wiek < 4:
    cena = 0
    print(f'Cena biletu: {cena}')
else:
    cena = 10
    print(f'Cena biletu: {cena}')

input("Press any key to continue...")

#zad 2
print(string.ascii_lowercase)
alfabet_m = list(string.ascii_lowercase)
alfabet_d = list(string.ascii_uppercase)
litera = input("Podaj literę: ")
if litera in alfabet_d:
    print("Duża litera")
else:
    print("Mała litera")

input("Press any key to continue...")

#zad 3
print("Prosty Kalkulator")
#pobieram dane od użytkownika
x = int(input("Podaj 1 liczbę: "))
y = int(input("Podaj 2 liczbę: "))
#informuje o możliwościach wyboru
print("Dodawanie: +")
print("Odejmowanie: -")
print("Mnożenie: *")
print("Dzielenie: /")
#proszę o wybór działania
operator = input("Wybierz działanie które chcesz wykonać(+,-,*,/,)")

if operator == "+":
    print(x+y)
elif operator == "-":
    print(x-y)
elif operator == "*":
    print(x*y)
elif operator == "/":
    print(x/y)
else:
    print("Error: Operator nie został znaleziony")

input("Press any key to continue...")

#zad 4

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
delta = b**2 - 4*a*c
if delta > 0:
    pierwiastek = math.sqrt(delta)
    x1 = (-(b) - pierwiastek) / (2*a)
    x2 = (-(b) + pierwiastek) / (2*a)
    print(f'x1 = {x1} i x2 = {x2}')
elif delta == 0:
    x0 =-(b)/(2*a)
    print(f'x0 = {x0}')
else:
    print(f'brak rozwiązań')

input("Press any key to continue...")


#zad 5
x = float(input('a = '))
y = float(input('b = '))
z = float(input('c = '))

if x < y and y < z:
    print(f'Kolejność rosnąca {x},{y},{z}')
elif x < z and z < y:
    print(f'Kolejność rosnąca {x},{z},{y}')
elif y < x and x < z:
    print(f'Kolejność rosnąca {y},{x},{z}')
elif y < z and z < x:
    print(f'Kolejność rosnąca {y},{z},{x}')
elif z < x and x < y:
    print(f'Kolejność rosnąca {z},{x},{y}')
elif z < y and y < x:
    print(f'Kolejność rosnąca {z},{y},{x}')


input("Press any key to continue...")
