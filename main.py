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

#zad 2 wyjasnienie działań poszczególnych instrukcji
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

#zad 3 skrypt pobiera długości boków i oblicza pole i obwód
x = 5
print("Obliczamy pole prostokąta:")

y = int(input("Podaj 1 bok:"))
x = int(input("Podaj 2 bok:"))
pole = (y*x)
obwod = 2*x +2*y
print("Pole prostokąta =", pole, "Obwód prostokąta =", obwod)

#zad 4 skrypt pobiera od uzytkownika drogę oraz średnie spalanie (na 100km) i przewiduje zużycie paliwa
print("Obliczamy zużycie paliwa - podaj dane")
droga = float(input("Podaj droge:"))
spalanie = float(input("Podaj śr. spalanie:"))
cena = 6.5

zuzycie = droga*spalanie/100
koszt = zuzycie*cena
print("Zużycie paliwa:",zuzycie, "Koszt:", koszt)


#zad 4.1 skrypt losuje drogę oraz średnie spalanie (na 100km) i przewiduje zużycie paliwa
print("Obliczamy zużycie paliwa - losowe dane")
import random

droga = float(random.randint(1, 10000))
spalanie = float(random.randint(1, 30))
cena = 6.5
print("Droga:", droga, "Spalanie:", spalanie)
zuzycie = droga*spalanie/100
koszt = zuzycie*cena
print("Zużycie paliwa:", zuzycie, "Koszt:", koszt)

#zad 5 skrypt wyliczający zużycie paliwa z modyfikacją na wykorzystanie f-string

#ZADANIA DODATKOWE
#zad 1 obliczamy równanie liniowe, współczynniki a i b podaje użytkownik
#zad 2 Obliczamy pole trójkąta
#zad 3 Kalkulator