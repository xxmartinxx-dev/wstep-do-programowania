#zad 1.	Napisz dwa programy – wykorzystujące i niewykorzystujące polecenie continue, które wczytują zmienną dana
# oraz jeżeli dana jest nieujemną liczbą całkowitą, to
#wyświetl informację, 'to jest liczba' i wczytaj kolejny raz zmienną dana, jeżeli nie wówczas zakończy się program
#wyświetli jej pierwiastek kwadratowy, jeżeli nie wówczas zakończy się program i wyświetli się informacja 'dziękujemy za skorzystanie z naszej aplikacji'.
while True:
    try:
        dana = int(input("Podaj liczbę: "))
        if dana >= 0:
            print("to jest liczba")
            print("Pierwiastek kwadratowy: ", dana ** 0.5)
        else:
            print("dziękujemy za skorzystanie z naszej aplikacji")
            break
    except ValueError:
        print("dziękujemy za skorzystanie z naszej aplikacji")
        break
###
while True:
    try:
        dana = int(input("Podaj liczbę: "))
        if dana < 0:
            print("dziękujemy za skorzystanie z naszej aplikacji")
            break
    except ValueError:
        print("dziękujemy za skorzystanie z naszej aplikacji")
        break

    print("to jest liczba")
    print("Pierwiastek kwadratowy: ", dana ** 0.5)
    continue
