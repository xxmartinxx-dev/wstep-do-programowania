#8. Napisz funkcję do obliczania pola trójkąta ostrokątnego, gdzie dane są długości dwóch
#boków i szerokość kąta ostrego pomiędzy nimi (w stopniach). Nie zapomnij o
#weryfikacji danych użytkownika:
#a. Czy trójkąt jest ostrokątny?
#b. Czy trójkąt istnieje?

print("Będziemy liczyć pole kąta ostrego z użyciem dwóch boków i sinusa kąta zawartego pomiędzy nimi!")
import math
a = int(input("Podaj bok a:"))
b = int(input("Podaj bok b:"))
kat = int(input("Podaj kąt pomiędzy bokami:"))

def pole_trojkata_ostrokątnego(a, b, kat):

    # Sprawdzenie czy kąt jest ostrym
    if kat <= 0 or kat >= 90:
        return "Błąd: Kąt musi być ostrym (większym niż 0 i mniejszym niż 90 stopni)."

    # Sprawdzenie czy trójkąt istnieje
    if a <= 0 or b <= 0:
        return "Błąd: Długości boków muszą być większe od zera."

    # Obliczenie pola trójkąta
    kat_radiany = math.radians(kat)
    pole = 0.5 * a * b * math.sin(kat_radiany)
    return pole

print(pole_trojkata_ostrokątnego(a, b, kat))


