#Wyświetl wszystkie nazwy funkcji zawartych w modułach: math, tuple, keyword.
import math
import keyword
print("Najpierw wyświetlimy wszystkie funkcje z bibliotek math:")
funkcje_w_math = [nazwa for nazwa in dir(math) if callable(getattr(math, nazwa))]

funkcje_w_tuple = tuple(nazwa for nazwa in dir(tuple) if callable(getattr(tuple, nazwa)))

print(f"Funkcje w module math: {funkcje_w_math}")
print(f"Funkcje w module tuple: {funkcje_w_tuple}")


slowa_kluczowe = keyword.kwlist
print(f"Słowa kluczowe w Pythonie: {slowa_kluczowe}")

print("")
print("")
#7. Zdefiniuj 10cio elementową krotkę(tuple), której elementy są losowane z przedziału
#podanego przez użytkownika. Oblicz średnią geometryczną krotki.

print("Stworzymy teraz krotkę, z 10 elementów. Liczby losujemy z przedziału podanych przez Ciebie liczb!")
import random

def sr_ciag_geo(krotka):
    iloczyn = 1
    for element in krotka:
        iloczyn *= element
    return iloczyn ** (1/len(krotka))


while True:
    try:
        zakres_poczatek = int(input("Podaj początek zakresu: "))
        zakres_koniec = int(input("Podaj koniec zakresu: "))
        if zakres_poczatek >= zakres_koniec:
            print("Początek zakresu musi być mniejszy niż koniec. Spróbuj ponownie.")
        else:
            break
    except ValueError:
        print("Podaj poprawne liczby")

krotka_elementow = tuple(random.randint(zakres_poczatek, zakres_koniec) for _ in range(10))


print(f"Krotka wygenerowanych elementów: {krotka_elementow}")


srednia_geo = sr_ciag_geo(krotka_elementow)
print(f"Średnia geometryczna: {srednia_geo:.2f}")
