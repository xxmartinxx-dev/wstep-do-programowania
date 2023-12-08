
#Zad1 Za pomocą pętli for wypisz na ekranie ciągi liczb: ciąg liczb całkowitych 1-100
print("Ciąg 1-100")
for i in range(1, 101):
    print(i)

print("Ciąg 100-0")
for i in range(100,-1, -1):
    print(i)

print("Ciąg 7-77")
for i in range(7, 78, 7):
    print(i)

print("Ciąg 20-0")
for i in range(20, -1, -2):
    print(i)

#zad2.	Napisz skrypt, który wyświetli gwiazdki jak poniżej. Liczba wierszy (lub gwiazdek w linii) powinna być podawana przez użytkownika.
#Przykład: 	3
#* * *
#* * *
#* * *
x = int(input("Podaj długość boku gwiazdkowego kwadratu "))

for i in range(0, x):
    linia = "* " * x
    print(linia)

#3.	Napisz program, który wyświetli „choinkę” jak poniżej. Wysokość „choinki” powinna być podawana z klawiatury.
#	4
#   *
#  * *
# * * *
#* * * *
podstawa = int(input("Podaj szerokość podstawy gwiazdkowej choinki "))

for i in range(1, podstawa + 1):
    liczba_znakow = podstawa - i
    odstep = " " * liczba_znakow
    wiersz1 = odstep + "* "*i
    print(wiersz1)


#zad 4 Napisz program, który wczyta liczbę naturalną n oraz dwie dowolne liczby rzeczywiste a i r. Wypisz n elementów ciągu arytmetycznego.
n = int(input("Podaj liczbę wyrazów w ciągu "))
a1 = int(input("Podaj pierwszy wyraz ciągu "))
r = int(input("Podaj różnicę ciągu "))

an = a1+(n-1)*r
if n <= 0:
    print("Numer wyrazu musi być liczbą naturalną")

elif n > 0:
    for i in range(a1, an+1, r):
        print(i)

#zad 5 Napisz program, który wczyta liczbę naturalną n oraz policzy jej silnię.
n = int(input("Podaj liczbę naturalną"))
import random
def silnia(n):
    if n == 1:
        return 1
    else:
        return n * silnia(n-1)

nx = random.randint(1, 100)
print(f"Wygenerowana liczba naturalna to {nx}")

wynik = silnia(nx)
print(f"n!={wynik}")
'''
    
  Zadania dodatkowe
1.	Napisz dwa programy – wykorzystujące i niewykorzystujące polecenie continue, które wczytują zmienną dana oraz jeżeli dana jest nieujemną liczbą całkowitą, to
•	wyświetl informację, 'to jest liczba' i wczytaj kolejny raz zmienną dana, jeżeli nie wówczas zakończy się program
•	wyświetli jej pierwiastek kwadratowy, jeżeli nie wówczas zakończy się program i wyświetli się informacja 'dziękujemy za skorzystanie z naszej aplikacji'.
'''