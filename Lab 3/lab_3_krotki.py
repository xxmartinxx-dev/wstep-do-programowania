import random
import string

n = int(input("Podaj liczbę n: "))
x = int(input("Podaj maksymalną długość ciągów znakowych x: "))

# Tworzenie listy składającej się z n losowych ciągów znakowych o losowej długości od 1 do x
lista_ciagow = [''.join(random.choices(string.ascii_lowercase, k=random.randint(1, x))) for _ in range(n)]

# Konwersja listy na krotkę
krotka_ciagow = tuple(lista_ciagow)

# Wyświetlenie listy i krotki
print("Lista ciągów: ", lista_ciagow)

# a) Sprawdzenie i wypisanie ilości znaków w liście
ilosc_znakow = sum(len(ciag) for ciag in lista_ciagow)
print(f"Ilość znaków w liście: {ilosc_znakow}")

# b) Sprawdzenie i wypisanie ilości liter 'k' w liście
ilosc_liter_k = sum(ciag.count('k') for ciag in lista_ciagow)
print(f"Ilość liter 'k' w liście: {ilosc_liter_k}")

# c) Sprawdzenie i wypisanie ilości ciągów znaków 'kt' w liście
ilosc_ciagow_kt = sum(1 for ciag in lista_ciagow if 'kt' in ciag)
print(f"Ilość ciągów znaków 'kt' w liście: {ilosc_ciagow_kt}")

# d) Sprawdzenie i wypisanie ilości ciągów znaków dłuższych niż s
s = int(input("Podaj długość s: "))
ilosc_ciagow_dluzych_niz_s = sum(1 for ciag in lista_ciagow if len(ciag) > s)
print(f"Ilość ciągów znaków dłuższych niż {s}: {ilosc_ciagow_dluzych_niz_s}")
#2. Stwórz listę zakupów jako słownik (artykuł : kwota). Wyświetl go i podsumuj wydatki.
# Tworzenie słownika zakupów
lista_zakupow = {
    'jajka': 5.0,
    'chleb': 3.5,
    'mleko': 2.0,
    'masło': 4.0,
    'sok pomarańczowy': 3.0
}

# Wyświetlanie listy zakupów
print("Lista zakupów:")
for produkt, cena in lista_zakupow.items():
    print(f"{produkt}: {cena} PLN")

# Obliczanie sumy wydatków
suma_wydatkow = sum(lista_zakupow.values())

# Wyświetlanie sumy wydatków
print(f"\nSuma wydatków: {suma_wydatkow} PLN")
#Zdefiniuj słownik, którego wartości będą rachunki za prąd przez ostatnich kilka miesięcy.

rachunki_za_prad = {
    'styczeń': 200,
    'luty': 180,
    'marzec': 220,
    'kwiecień': 210,
    'maj': 250,
    'czerwiec': 260
}
#a Wyznacz maksymalną, minimalną, sumę oraz wartość średnią (polecam użyć listy wartości)

wartosci = list(rachunki_za_prad.values())
maksimum = max(wartosci)
minimum = min(wartosci)
suma = sum(wartosci)
srednia = suma / len(wartosci)

print(f"Maksymalna wartość rachunku: {maksimum} PLN")
print(f"Minimalna wartość rachunku: {minimum} PLN")
print(f"Suma rachunków: {suma} PLN")
print(f"Średnia wartość rachunku: {srednia} PLN")

# b Sprawdź czy w ostatnim miesiącu wartość przekroczyła średnią.
# Jeśli tak, to wyświetl „Zacznij oszczędzać”. W przeciwnym razie „Jesteś bezpieczny”.
ostatni_miesiac = list(rachunki_za_prad.keys())[-1]
wartosc_ostatniego_miesiaca = rachunki_za_prad[ostatni_miesiac]

if wartosc_ostatniego_miesiaca > srednia:
    print("Zacznij oszczędzać")
else:
    print("Jesteś bezpieczny")

import random

# Generowanie losowych wartości a i b z przedziału <3, 7>
a = random.randint(3, 7)
b = random.randint(3, 7)

# Generowanie zbiorów X i Y z losowymi elementami z przedziału <0, 10>
X = set(random.randint(0, 10) for _ in range(a))
Y = set(random.randint(0, 10) for _ in range(b))

# a Wypisz na ekran informację czy zbiór X zawiera liczbę 5.
contains_5_X = 5 in X
print("a) Zbiór X zawiera liczbę 5:", contains_5_X)

# b Wypisz na ekran informację czy zbiór X jest podzbiorem zbioru Y.
is_subset_X_Y = X.issubset(Y)
print("b) Zbiór X jest podzbiorem zbioru Y:", is_subset_X_Y)

# c Wypisz na ekran informację czy zbiór Y jest podzbiorem zbioru X.
is_subset_Y_X = Y.issubset(X)
print("c) Zbiór Y jest podzbiorem zbioru X:", is_subset_Y_X)

# d Wypisz na ekran informację czy zbiór X jest nadzbiorem zbioru Y.
is_superset_X_Y = X.issuperset(Y)
print("d) Zbiór X jest nadzbiorem zbioru Y:", is_superset_X_Y)

# e Wypisz na ekran informację czy zbiór Y jest nadzbiorem zbioru X.
is_superset_Y_X = Y.issuperset(X)
print("e) Zbiór Y jest nadzbiorem zbioru X:", is_superset_Y_X)

# f Wypisz na ekran sumę zbiorów X oraz Y.
union_X_Y = X.union(Y)
print("f) Suma zbiorów X i Y:", union_X_Y)

# g Wypisz na ekran różnicę zbiorów X oraz Y.
difference_X_Y = X.difference(Y)
print("g) Różnica zbiorów X i Y:", difference_X_Y)

# h Wypisz na ekran różnicę zbiorów Y oraz X.
difference_Y_X = Y.difference(X)
print("h) Różnica zbiorów Y i X:", difference_Y_X)

# i Wypisz na ekran iloczyn zbiorów X oraz Y.
intersection_X_Y = X.intersection(Y)
print("i) Iloczyn zbiorów X i Y:", intersection_X_Y)

# j Wypisz na ekran różnicę symetryczną zbiorów X oraz Y.
symmetric_difference_X_Y = X.symmetric_difference(Y)
print("j) Różnica symetryczna zbiorów X i Y:", symmetric_difference_X_Y)

# k Wypisz na ekran wartość najwyższego elementu w obu zbiorach.
max_X = max(X)
max_Y = max(Y)
print("k) Najwyższy element w zbiorze X:", max_X)
print("   Najwyższy element w zbiorze Y:", max_Y)

# l Usuń ze zbioru X pierwszy element i dołącz go do zbioru Y.
if X:
    first_element_X = X.pop()
    Y.add(first_element_X)
    print("l) Usunięto pierwszy element z X i dołączono go do Y:", first_element_X)

# m Przekopiuj wszystkie elementy zbioru X do zbioru Y.
Y.update(X)
print("m) Skopiowano wszystkie elementy z X do Y")

# n Wyczyść oba zbiory.
X.clear()
Y.clear()
print("n) Wyczyszczono oba zbiory X i Y")



