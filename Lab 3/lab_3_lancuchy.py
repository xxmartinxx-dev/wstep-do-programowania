#zad1 Stwórz listę z imionami 4 osób.
list = ["Martyna", "Nina", "Lena", "Laura"]
#a Posortuj ją alfabetycznie i wyświetl,
list = sorted(list)

#b Dodaj na końcu dwie osoby i pobierz ostatnią z nich poleceniem pop()
list.append("jola")
list.append("kasia")
print(list)
print(list.pop())
print(list)
#c Na pozycji 3 dodaj jeszcze jedną osobę,
list.insert(3,"Wiola")
print(list)
#d Odwróć kolejność na liście i zdubluj ją.
list.reverse()
print(list)
nowa_lista = list
print(list)
print(nowa_lista)

#zad 2Dla łańcucha tekst = "Rzeszów jest piękny" wyświetl:
tekst = "Rzeszów jest piękny"
#Pierwszą literę w tekście,
print(tekst[1])
# Siódmą, dziesiątą, trzynastą oraz drugą.
print(tekst[7],tekst[10],tekst[13], tekst[2])

#zad 3.	Wyświetl z łańcucha tekst ="Python jest super" znaki o indeksach:
tekst ="Python jest super"
#Zerowym
print(tekst[0])
#Ostatnim
print(tekst[-1])
#Co drugi, zaczynając od zerowego
print(tekst[0:-1:2])
#Co trzeci zaczynając od pierwszego
print(tekst[1:-1:3])
#Od dziesiątego do ostatniego
print(tekst[10:])
#Wyświetl od końca do początku
print(tekst[0:])

#zad 2.	Dla łańcucha tekst = "Rzeszów jest piękny" wyświetl:
#Pierwszą literę w tekście,
# Siódmą, dziesiątą, trzynastą oraz drugą.
tekst = "Rzeszów jest piękny"
print(tekst[1])
print(tekst[7],tekst[10],tekst[13], tekst[2])

#zad 3.	Wyświetl z łańcucha tekst ="Python jest super" znaki o indeksach:
#Zerowym
#Ostatnim
#Co drugi, zaczynając od zerowego
#Co trzeci zaczynając od pierwszego
#Od dziesiątego do ostatniego
#Wyświetl od końca do początku
tekst ="Python jest super"
print(tekst[0])
print(tekst[-1])
print(tekst[0:-1:2])
print(tekst[1:-1:3])
print(tekst[10:])
print(tekst[0:])

#zad 4. Napisz program, który:
#Wczyta (zmienną) imię oraz wyświetli tekst „Witaj” oraz wczytane imię.
imie = input("Jak masz na imię?")
print("Witaj",imie)
#Wczyta (zmienną) wiek oraz wyświetli tekst „Twój wiek to:” oraz wczytany wiek.
wiek = input("Ile masz lat?")
print("Twój wiek to",wiek)
#Wczyta (zmienne) imię i nazwisko i wyświetli inicjały.
imie = input("Jak masz na imię?")
nazwisko = input("Jak masz na nazwisko?")
print("Twoje inicjały to",imie[0],nazwisko[0])

#Wczyta łańcuch i wyświetli go pięć razy.
tekst = input("Napisz coś dla mnie: ")
tekst = tekst + " "
print(tekst*5)
#Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta połączone te dwa łańcuchy.
tekst1 = input("Napisz coś dla mnie: ")
tekst2 = input("Może napisz coś jeszcze: ")
tekst3 = tekst1 + tekst2
print(tekst3)

#Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta pierwszą połowę pierwszego i drugą połowę drugiego.
text1 = input("Napisz coś dla mnie: ")
x1 = len(text1)
x1 = int(x1/2)
text2 = input("Może napisz coś jeszcze: ")
x2 = len(text2)
x2 = int(x2/2)
text3 = text1[:x2] + text2[x2:]
print(text3)