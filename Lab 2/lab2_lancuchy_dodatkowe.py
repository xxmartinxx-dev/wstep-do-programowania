#Zadania dodatkowe
#Napisz program, który:
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