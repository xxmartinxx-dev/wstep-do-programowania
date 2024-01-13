import random

# Poproś użytkownika o podanie pięciu cyfr rozdzielonych przecinkiem
user_input = input("Podaj pięć cyfr rozdzielonych przecinkiem: ")

# Sprawdź, czy użytkownik podał pięć cyfr
input_list = user_input.split(',')
if len(input_list) != 5:
    print("Podano niewłaściwą liczbę cyfr. Konieczne jest podanie dokładnie pięciu cyfr.")
else:
    # Przekształć podane cyfry na liczby całkowite
    numbers = [int(x) for x in input_list]

    # Zmień tablicę na inny typ kolekcji (użyj random.shuffle)
    random.shuffle(numbers)

    # Pobierz pierwszy element z przemieszanej kolekcji
    selected_number = numbers[0]

    # Sprawdź, czy wylosowany element jest najmniejszą lub największą z podanych liczb
    if selected_number == min(numbers):
        print(f"Wylosowana liczba {selected_number} jest najmniejszą z podanych liczb.")
    elif selected_number == max(numbers):
        print(f"Wylosowana liczba {selected_number} jest największą z podanych liczb.")
    else:
        print(f"Wylosowana liczba to {selected_number}.")
# Rozmiar pola gry
szerokosc = 6
wysokosc = 5

# Inicjalizacja planszy jako pustej trawy
plansza = [['.' for _ in range(szerokosc)] for _ in range(wysokosc)]

# Pozycje przeciwników
przeciwnicy = [(0, 1), (2, 3), (2, 4), (3, 4)]

# Pozycje monet
monety = [(1, 1), (2, 0), (3, 3), (5, 3)]

# Rzeka na wysokości y=2
rzeka_y = 2

# Wypełnienie planszy zgodnie z pozycjami przeciwników, monet i rzeki
for x, y in przeciwnicy:
    plansza[y][x] = 'x'

for x, y in monety:
    plansza[y][x] = '*'

for x in range(szerokosc):
    plansza[rzeka_y][x] = '='

# Wyświetlenie planszy w konsoli
for row in plansza:
    print(' '.join(row))

