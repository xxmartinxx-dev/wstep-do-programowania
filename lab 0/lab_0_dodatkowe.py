import math
#ZADANIA DODATKOWE
#zad 1 obliczamy równanie liniowe, współczynniki a i b podaje użytkownik
print("Skrypt oblicza równanie liniowe, gdzie a i b podaje użytkownik")
a = float(input('a = '))
b = float(input('b = '))
if a == 0:
    if b == 0:
        print('Równanie tożsamościowe')
    else:
        print('Równanie sprzeczne')
else:
    x = -b/a
    print('x =', x)

input("Press any key to continue...")

#zad 2 Obliczamy pole trójkąta
print("Skrypt oblicza pole trójkąta różnobocznego ze wzoru na 3 boki, podaj ich wartość")
c = float(input('c = '))
d = float(input('d = '))
e = float(input('e = '))
p=(a+b+c)/2

Pole = round(math.sqrt(p*(p-c)*(p-d)*(p-e)),2)
print("Pole trójkąta:", Pole)

import math

#zad 3 Kalkulator
print("Skrypt oblicza podstawowe działania na 2 podanych przez użytkownika liczbach:")
f = float(input('f = '))
g = float(input('g = '))
dodawanie= f+g
odejmowanie = f-g
mnożenie = f*g
dzielenie = f/g
print(f"{f}+{g}={dodawanie}")
print(f"{f}-{g}={odejmowanie}")
print(f"{f}*{g}={mnożenie}")
print(f"{f}:{g}={dzielenie}")
