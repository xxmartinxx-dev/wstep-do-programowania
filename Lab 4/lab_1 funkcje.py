#Zadania
#1. Napisz funkcję, która policzy i wypisze pole koła o promieniu r.
r = int(input("Wpisz promień koła:" ))
def pole_kola(r):
    pi = 3.14159
    pole = pi * r * r
    print(f"Pole koła o promieniu {r} wynosi: {pole}")

print(pole_kola(r))


#2. Napisz funkcję obliczającą pole trapezu o wymiarach: a, b, h.
a = int(input("Wpisz długość podstawy:" ))
b = int(input("Wpisz długość 2 podstawy:" ))
h = int(input("Wpisz wyokość traoezu:" ))
def pole_trapezu(a, b, h):
    pole = (a + b) * h / 2
    return pole
print(pole_trapezu(a,b,h))


#3. Napisz funkcję o dwóch parametrach, imię oraz wiek, która wypisze ich wartości na ekranie.
imie = input("Wpisz imie:" )
wiek = input("Wpisz wiek:")
def wypisz_imie_i_wiek(imie, wiek):
    print(f"Imię: {imie}, Wiek: {wiek}")
print(wypisz_imie_i_wiek(imie,wiek))


#a. Dodaj w następnej linii po nagłówku funkcji komentarz opisujący działanie funkcji.
#Wyświetl ten opis za pomocą instrukcji print(nazwa_funkcji.__doc__)
def wypisz_imie_i_wiek(imie, wiek):
    """
    Wyświetla na ekranie imię i wiek podane jako argumenty.

    Parametry:
    imie (str): Imię osoby
    wiek (int): Wiek osoby
    """
    print(f"Imię: {imie}, Wiek: {wiek}")

# Wyświetlanie opisu funkcji
print(wypisz_imie_i_wiek.__doc__)
print(wypisz_imie_i_wiek(imie,wiek))


#b. Jeśli w wywołaniu funkcji nie podano wieku, przypisz do parametru wiek wartość domyślną 20.
#Uwaga: Parametry z wartościami domyślnymi powinny być definiowane jako ostatnie na liście parametrów,
# ponieważ Python dopasowuje argumenty do parametrów na podstawie ich pozycji: def fun(param1, param2=default2, param3=default3)
def wypisz_imie_i_wiek(imie, wiek=20):
    """
    Wyświetla na ekranie imię i wiek podane jako argumenty. Jeśli wiek nie jest podany, domyślnie przyjmuje wartość 20.

    Parametry:
    imie (str): Imię osoby
    wiek (int): Wiek osoby, domyślnie 20
    """
    print(f"Imię: {imie}, Wiek: {wiek}")


# Wyświetlanie opisu funkcji
print(wypisz_imie_i_wiek.__doc__)
print(wypisz_imie_i_wiek(imie,wiek))


#4. Napisz funkcję, która sprawdzi, czy podana liczba x jest dodatnia i wyświetli odpowiednią informację.
x = int(input("Wpisz liczbę, którą chcesz sprawdzić:" ))
def czy_dodatnia(x):
    """
    Sprawdza, czy podana liczba x jest dodatnia i wypisuje odpowiednią informację.

    Parametry:
    x (int/float): Liczba do sprawdzenia
    """
    if x > 0:
        print(f"Liczba {x} jest dodatnia.")
    else:
        print(f"Liczba {x} nie jest dodatnia.")

# Wyświetlanie opisu funkcji
print(czy_dodatnia.__doc__)
print(czy_dodatnia(x))


#5. Napisz funkcję, która na podstawie podanej wagi i wzrostu oblicza i zwraca wskaźnik BMI, a następnie informuje użytkownika w jakim jest zakresie.
waga = int(input("Wpisz wagę:" ))
wzrost = int(input("Wpisz wzrost:"))
def oblicz_bmi(waga, wzrost):
    """
    Oblicza wskaźnik BMI na podstawie podanej wagi i wzrostu, a następnie informuje, w jakim jest zakresie.

    Parametry:
    waga (float): Waga w kilogramach
    wzrost (float): Wzrost w metrach
    """
    bmi = waga / (wzrost ** 2)

    if bmi < 18.5:
        zakres = "niedowaga"
    elif 18.5 <= bmi < 25:
        zakres = "prawidłowa masa ciała"
    elif 25 <= bmi < 30:
        zakres = "nadwaga"
    else:
        zakres = "otyłość"

    return bmi, zakres

# Wyświetlanie opisu funkcji
print(oblicz_bmi.__doc__)
print(oblicz_bmi(waga,wzrost))


#6. Napisz funkcję, która oblicza pole trójkąta o boku a, b ,c. Pamiętaj o zabezpieczeniu funkcji przed błędnymi danymi i wyjątkami.
a = int(input("Wpisz bok a:" ))
b = int(input("Wpisz bok b:"))
c = int(input("Wpisz bok c:" ))

def pole_trojkata(a, b, c):
    """
    Oblicza pole trójkąta na podstawie długości jego boków, korzystając z wzoru Herona.
    Sprawdza, czy podane długości mogą tworzyć trójkąt.

    Parametry:
    a, b, c (float): Długości boków trójkąta
    """
    if a <= 0 or b <= 0 or c <= 0:
        return "Błędne dane: długości boków muszą być większe od zera."

    if a + b <= c or a + c <= b or b + c <= a:
        return "Błędne dane: suma długości dwóch boków musi być większa niż długość trzeciego boku."

    s = (a + b + c) / 2
    pole = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return pole

# Wyświetlanie opisu funkcji
print(pole_trojkata.__doc__)
print(pole_trojkata(a,b,c))


#7. Napisz funkcję odwracającą string.
s = input("Wpis słowa, które chcesz odwrócić:")
def odwroc_string(s):
    """
    Odwraca podany ciąg znaków (string).

    Parametry:
    s (str): Ciąg znaków do odwrócenia
    """
    return s[::-1]

# Wyświetlanie opisu funkcji
print(odwroc_string.__doc__)
print(odwroc_string(s))


#8. Napisz funkcję rekurencyjną obliczania n’tego stopnia potęgi liczby a.
a = int(input("Wpisz podstawe:" ))
n = int(input("Wpisz potege:"))
def potega(a, n):
    """
    Oblicza n-tą potęgę liczby a za pomocą rekurencji.

    Parametry:
    a (int/float): Podstawa potęgi
    n (int): Wykładnik potęgi, powinien być liczbą całkowitą
    """
    if n == 0:
        return 1
    if n < 0:
        return 1 / potega(a, -n)
    return a * potega(a, n - 1)

# Wyświetlanie opisu funkcji
print(potega.__doc__)
print(potega(a,n))


#9. Napisz funkcję rekurencyjną, która poda n-ty wyraz ciągu Fibonacciego
n = int(input("Wpisz ile znaków ma mieć ciąg:"))
def fibonacci(n):
    """
    Oblicza n-ty wyraz ciągu Fibonacciego za pomocą rekurencji.

    Parametry:
    n (int): Indeks wyrazu ciągu Fibonacciego, który ma być obliczony
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Wyświetlanie opisu funkcji
print(fibonacci.__doc__)
print(fibonacci(n))