#zad1
#Wylosuj „szczęśliwy numerek” dla swojej grupy.

import random
happy_number = random.randint(1,19)
print("Szczęśliwy numer dzisiaj to:",happy_number)
#Zdefiniuj tablicę której elementami będą roczniki urodzenia wszystkich osób w grupie. Wylosuj szczęśliwy rocznik.
roczniki = [1994,1998,2002,2002,2003,2004]
happy_year = random.choice(roczniki)
print("Szczęśliwy rocznik dzisiaj to:",happy_year)
#W losowaniu dużego lotka losuje się 6 kul spośród liczb 1 do 49. Wygeneruj listę 1 do 49 (range).
# oszukaj informacji na temat random.sample() i zasymiluj losowanie totolotka.

#oblicz
import math
x=math.sqrt(81)
print("pierwsze działanie, pierwiastek z 81",x )

print("drugie działanie, 8 do potęgi 10:",math.pow(8,10))
b = math.sqrt(2)
c = math.sqrt(3)
d = math.sqrt(6)
wynik = b + c + d
print("drugie działanie, pierwistek z 2 + pierwiastek z 3 + pierwiastek z 6:",wynik)
a = -5
if a>0:
    x = math.sqrt(a)
    print("3 działanie: ", x)
else:
    print("3 działanie: Nie można wykonać")


print("4 działanie: ", 125**(1/3))

#Napisz program „sekundnik”, który prze określony przez użytkownika czas
# będzie wyświetlał liczbę sekund pozostałą do końca.
import time

czas = int(input("Podaj czas w sekundach:"))
def sekundnik(czas):
    while czas > 0:
        print ("Pozostało",{czas},"sekund")
        time.sleep(1)
        czas -= 1
    print("Czas minął!")

print(sekundnik(czas))

#Wykonaj operację, która obliczy ile dni upłynęło od ostatnich laboratoriów oraz ile czasu zostało do kolokwium.
# Niech wynik wyświetli się w przystępny sposób z nazwą miesiąca.


import datetime
import time

#Zad 4

data_dzisiejsza = datetime.date.today()
print(f"Data dzisiejsza to {data_dzisiejsza}")
from datetime import date
data_ost_zaj = date(2023, 12, 10)
print(f"Data ostatnich zajęć to {data_ost_zaj}")
data_kolosa = date(2024, 2, 11)
print(f"Data kolokwium to {data_kolosa}")
czas_od_zajec = data_dzisiejsza - data_ost_zaj

print(f"Od ostatnich zajęć minęło: {czas_od_zajec}")
czas_do_kol = data_kolosa - data_dzisiejsza
print(f"Czas do kolokwium to {czas_do_kol}")


# Zad 5
import keyword
c = "for"
d = "print"
e = "break"
f = "done"
g = "bad"
print(keyword.iskeyword(c))