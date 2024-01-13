#Zadania dodatkowe
#. Napisz funkcję, która jako argument przyjmuje imię, a następnie zwraca wynik „kobieta” lub „mężczyzna”.
imie = input("Wpisz imię, by określić płeć")
def okresl_plec(imie):
    """
    Funkcja, która na podstawie imienia określa płeć.
    Zakłada się, że imiona żeńskie w języku polskim zazwyczaj kończą się na 'a'.
    """
    if imie.endswith('a'):
        return 'kobieta'
    else:
        return 'mężczyzna'
print(okresl_plec(imie))
# Następnie zdefiniuj tablicę z 5 różnymi imionami i wykorzystując stworzoną funkcję stwórz słownik zawierający pary imię: płeć.
# Definiowanie tablicy z pięcioma różnymi imionami
imiona = ['Anna', 'Krzysztof', 'Maria', 'Piotr', 'Ewa']

# Utworzenie słownika zawierającego pary imię: płeć
slownik_plec = {imie: okresl_plec(imie) for imie in imiona}
print(slownik_plec)

#2. Napisz funkcję o zmiennej liczbie parametrów, która wyświetla wartości parametrów na ekranie.
# Następnie zmodyfikuj funkcję tak, aby znajdowała i zwracała wartość maksymalną.
#Wskazówka: użyj parametru *args, który łączy wszystkie dodatkowe (nadmiarowe) argumenty pozycyjne, niebędące słowami kluczowymi
# podczas wywoływania funkcji, w krotkę.

def wyswietl_i_znajdz_max(*args):
    """
    Funkcja o zmiennej liczbie parametrów, która wyświetla wartości parametrów
    i znajduje wartość maksymalną spośród nich.
    """
    # Wyświetlanie wartości parametrów
    print("Wartości parametrów:", args)

    # Znalezienie i zwrócenie wartości maksymalnej
    return max(args) if args else None

# Przykładowe wywołanie funkcji
max_wartosc = wyswietl_i_znajdz_max(8, 5, 11, 36, 23)
print("Wartość maksymalna:", max_wartosc)

#3. Napisz funkcję, która oblicza pierwiastki równania kwadratowego. Wynik powinien być zwracany w postaci krotki lub listy.
# Przetestuj przekazując różne wartości a, b, c do funkcji i wyświetlając wyniki. Ustaw domyślne wartości b i c na 0.
#Uwaga: pusta krotka – ()
#krotka z jednym elementem, np. liczbą 1.2 - (1.2,)
#Pamiętaj o zabezpieczeniu funkcji przed błędnymi danymi i wyjątkami.
import math

def oblicz_pierwiastki(a, b=0, c=0):
    """
    Funkcja obliczająca pierwiastki równania kwadratowego ax^2 + bx + c = 0.
    Zwraca wynik w postaci krotki.
    """
    if a == 0:
        return ()  # a nie może być 0 w równaniu kwadratowym

    delta = b**2 - 4*a*c

    # Brak rozwiązań rzeczywistych
    if delta < 0:
        return ()

    # Jedno rozwiązanie (delta = 0)
    elif delta == 0:
        x = -b / (2*a)
        return (x,)

    # Dwa rozwiązania (delta > 0)
    else:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b - sqrt_delta) / (2*a)
        x2 = (-b + sqrt_delta) / (2*a)
        return (x1, x2)

# Przetestowanie funkcji z różnymi wartościami a, b, c
test1 = oblicz_pierwiastki(1, -3, 2)    # a=1, b=-3, c=2
test2 = oblicz_pierwiastki(1, 2, 1)    # a=1, b=2, c=1
test3 = oblicz_pierwiastki(1, 0, -4)   # a=1, b=0, c=-4
test4 = oblicz_pierwiastki(1, 4, 5)    # a=1, b=4, c=5 (brak rozwiązań rzeczywistych)
test5 = oblicz_pierwiastki(0, 2, 1)    # a=0 (błędne dane)

print(test1, test2, test3, test4, test5)


#4. Napisz funkcję, która otrzymuje string i zwraca liczbę wielkich i małych liter oraz liczbę pozostałych znaków
# w postaci słownika.
def policz_znaki(tekst):
    """
    Funkcja, która otrzymuje string i zwraca liczbę wielkich i małych liter
    oraz liczbę pozostałych znaków w postaci słownika.
    """
    wynik = {"wielkie_litery": 0, "male_litery": 0, "pozostale_znaki": 0}

    for znak in tekst:
        if znak.isupper():
            wynik["wielkie_litery"] += 1
        elif znak.islower():
            wynik["male_litery"] += 1
        else:
            wynik["pozostale_znaki"] += 1

    return wynik

# Przykładowe wywołanie funkcji
tekst_testowy = "Witaj Świecie! 123"
wynik = policz_znaki(tekst_testowy)
print(wynik)

#5. Napisz funkcję, która otrzymuje dwa obiekty iterowalne (sekwencje) i zwraca listę wspólnych dla obu obiektów wartości.
def znajdz_wspolne_wartosci(seq1, seq2):
    """
    Funkcja do znajdowania wspólnych wartości między dwoma obiektami iterowalnymi (sekwencjami).

    :param seq1: Pierwsza sekwencja iterowalna.
    :param seq2: Druga sekwencja iterowalna.
    :return: Lista wspólnych wartości między seq1 i seq2.
    """
    # Konwersja sekwencji na zbiory w celu usunięcia duplikatów i wykonania przecięcia
    set1 = set(seq1)
    set2 = set(seq2)

    # Znalezienie przecięcia (wspólnych elementów) i konwersja z powrotem na listę
    wspolne_elementy = list(set1.intersection(set2))

    return wspolne_elementy

# Przykładowe użycie
seq1 = [1, 2, 3, 6, 7]
seq2 = [4, 5, 6, 7, 8]
znajdz_wspolne_wartosci(seq1, seq2)
print(znajdz_wspolne_wartosci(seq1, seq2))
#6. Napisz funkcję pozwalającą na odnalezienie największego wspólnego dzielnika dwóch liczb.
def nwd(a, b):
    """
    Funkcja do znajdowania największego wspólnego dzielnika (NWD) dwóch liczb.

    :param a: Pierwsza liczba.
    :param b: Druga liczba.
    :return: Największy wspólny dzielnik liczb a i b.
    """
    while b:
        a, b = b, a % b
    return a

# Przykładowe użycie funkcji
nwd(12, 24)  # NWD dla liczb 48 i 18
print(nwd(12, 24))

#7. Napisz funkcję badającą czy dane słowo to palindrom.
def czy_palindrom(slowo):
    """
    Funkcja do sprawdzania, czy dane słowo jest palindromem.

    :param slowo: Słowo do sprawdzenia.
    :return: True jeśli słowo jest palindromem, w przeciwnym razie False.
    """
    # Usunięcie spacji i konwersja na małe litery dla unifikacji
    slowo = slowo.replace(" ", "").lower()

    # Sprawdzenie, czy słowo jest takie samo czytane od przodu i od tyłu
    return slowo == slowo[::-1]

# Przykładowe użycie funkcji
czy_palindrom("kajak")  # Sprawdzenie dla słowa "kajak"
czy_palindrom("python")  # Sprawdzenie dla słowa "python"

print(czy_palindrom("kajak"))
print(czy_palindrom("python"))


#8. Napisz funkcję informującą czy dwa podane słowa są anagramami.
def czy_anagram(slowo1, slowo2):
    """
    Funkcja do sprawdzania, czy dwa słowa są anagramami.

    :param slowo1: Pierwsze słowo.
    :param slowo2: Drugie słowo.
    :return: True jeśli słowa są anagramami, w przeciwnym razie False.
    """
    # Usunięcie spacji i konwersja na małe litery dla unifikacji
    slowo1 = slowo1.replace(" ", "").lower()
    slowo2 = slowo2.replace(" ", "").lower()

    # Sprawdzenie, czy posortowane litery obu słów są takie same
    return sorted(slowo1) == sorted(slowo2)

# Przykładowe użycie funkcji
czy_anagram("listen", "silent")  # Sprawdzenie dla słów "listen" i "silent"
czy_anagram("hello", "world")    # Sprawdzenie dla słów "hello" i "world"

print(czy_anagram("listen", "silent"))
print(czy_anagram("hello", "world"))