#zad 1	Napisz skrypt, który pobierze od użytkownika dwie liczby całkowite.
# Następnie zaczynając od mniejszej liczby, wypisze kolejne liczby aż do osiągnięcia wartości drugiej (większej) liczby.

liczba1 = int(input("Wprowadź liczbę: "))
liczba2 = int(input("Wprowadź liczbę: "))

while liczba1<liczba2:
    print(liczba1)
    liczba1 = liczba1 + 1
else:
    print(liczba1)

#zad2 2.	Napisz program, który wyświetli wartości funkcji 𝑦=2𝑥^2−5𝑥−8, dla 𝑥∈[−4,4], z krokiem 0.5.
x = float(-4)
while x >= (-4) and x <= 4:
    print("dla x=",x," Wartość wyrażenia: 𝑦=2𝑥^2−5𝑥−8, dla 𝑥∈[−4,4] wynosi")
    wartosc=2*(x**2)-(5*x)-8
    print(wartosc)
    x = x+0.5
else:
    print(wartosc)
    print("end")

# zad 3 3.	Napisz pętlę nieskończoną, w której użytkownik podaje liczby całkowite. W przypadku liczby ujemnej, następuję wyjście z pętli.

x = int(input("Wprowadź liczbę parzystą: "))
while x>=0:
    x = int(input("Wprowadź liczbę parzystą: "))
    if x<=0: break


# zad 4 Zmodyfikuj program z zad. 1 tak, aby przechodząc po kolejnych liczbach przedziału, wypisywać tylko liczby parzyste, a nieparzyste – pomijać.
# Użyj instrukcji continue.
liczba1 = int(input("Wprowadź liczbę: "))
liczba2 = int(input("Wprowadź liczbę: "))
if liczba1 < liczba2:
    for i in range(liczba1, liczba2):
        if liczba1 % 2 == 1:
            continue
        print(liczba1)
else:
    print("end")

liczba1 = int(input("Podaj pierwszą liczbę "))
liczba2 = int(input("Podaj drugą liczbę "))

if liczba1 < liczba2:
    for i in range(liczba1, liczba2+1):
        if i % 2 == 1:
            continue
        print(i)
elif liczba1 > liczba2:
    for i in range(liczba2, liczba1+1):
        if i % 2 == 1:
            continue
        print(i)