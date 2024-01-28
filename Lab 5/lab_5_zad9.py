#9. Napisz grę w zgadywanie liczby:
#a. Użytkownik podaje zakres losowania.
#b. Użytkownik ma tylko 3 próby zgadnięcia.
#c. Gra zwraca wskazówki „za mało” lub „za dużo” w zależności od odpowiedzi
#użytkownika.
#Ponad to gra ma weryfikować czy użytkownik nie chce jej oszukać (podając za mały
#zakres, i czy podaje na pewno liczby).

import random
print("Zagrajmy w grę! Podaj zakres liczb (różnica pomięczy liczbami musi wynosić conajmniej 10.")
print("Po podaniu zakresu program wylosuje dowolną liczbę. Musisz zgadnąć jaka to liczba")
print("Masz tylko trzy podejścia!")
print("POWODZENIA!")

def gra(a, b):
    szukana_liczba = random.randint(a, b)
    print(f"Zakres liczb to {a} - {b}")
    for proba in range(1, 4):
        while True:
            try:
                liczba_uzytkownika = int(input(f"Podejście nr {proba}. Podaj swoja losową liczbę: "))
                break
            except ValueError:
                print("Nie udało się. Podaj poprawną liczbę.")
        if szukana_liczba == liczba_uzytkownika:
            print("Gratulacje! Udało się!")
            break
        elif szukana_liczba > liczba_uzytkownika:
            print("Podałeś za małą liczbę.")
        elif szukana_liczba < liczba_uzytkownika:
            print("Podałeś za dużą liczbę.")
    else:
        print("To koniec! Wyczerpałeś limit prób!")
        print("GAME OVER! :(")

# Zakres liczb


while True:
    try:
        a = int(input("Podaj liczbę będącą początkiem zakresu: "))
        b = int(input("Podaj koniec zakresu, PAMIĘTAJ! liczba musi być min. o 10 większa od poczatkowej:"))
        if a >= b or b - a < 10:
            print("Zakres nie spełnia wymienionych warunków.")
        else:
            break
    except ValueError:
        print("Podaj poprawne liczby")

# początek gry
gra(a, b)
