#zad 1 1.	Grupa laboratoryjna składa się z n studentów (wartość n podaje użytkownik).
# Wprowadzamy liczbę punktów dla każdego studenta.
# Napisz program, który obliczy średnią liczbę punktów w grupie z wykorzystaniem pętli while.
# Użytkownik podaje liczbę studentów
n = int(input("Podaj liczbę studentów w grupie laboratoryjnej: "))

# Zmienna do przechowywania sumy punktów
suma_punktow = 0

# Licznik do sterowania pętlą while
i = 0

while i < n:
    # Użytkownik wprowadza liczbę punktów dla każdego studenta
    punkty = float(input(f"Podaj liczbę punktów dla studenta {i + 1}: "))
    suma_punktow += punkty
    i += 1

# Obliczenie średniej
srednia = suma_punktow / n

# Wyświetlenie wyniku
print(f"Średnia liczba punktów w grupie wynosi: {srednia}")

#zad 2 2.	Zastosuj instrukcje continue w programie z zad. 5 tak, aby po podaniu liczby punktów spoza przedziału 0 – 100
# pomijać dalsze wykonywanie pętli. Sprawdź działanie programu. Następnie zmień pętlę na nieskończoną,
# czyli taką której warunek zawsze jest prawdziwy.
#Zakończ działanie pętli przy użyciu instrukcji break.
# Użytkownik podaje liczbę studentów
n = int(input("Podaj liczbę studentów w grupie laboratoryjnej: "))

# Zmienna do przechowywania sumy punktów
suma_punktow = 0

# Licznik do sterowania pętlą while
i = 0

# Zmiana pętli na nieskończoną
while True:
    # Użytkownik wprowadza liczbę punktów dla każdego studenta
    punkty = float(input(f"Podaj liczbę punktów dla studenta {i + 1}: "))

    # Sprawdzenie, czy punkty są w przedziale 0-100
    if punkty < 0 or punkty > 100:
        print("Liczba punktów poza dozwolonym przedziałem. Spróbuj ponownie.")
        continue

    suma_punktow += punkty
    i += 1

    # Jeśli liczba przetworzonych studentów osiągnie n, zakończ pętlę
    if i == n:
        break

# Obliczenie średniej
srednia = suma_punktow / n

# Wyświetlenie wyniku
print(f"Średnia liczba punktów w grupie wynosi: {srednia}")