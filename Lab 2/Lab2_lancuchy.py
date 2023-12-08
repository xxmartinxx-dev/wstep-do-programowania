#zad 1.	Dla łańcucha tekst = "Rzeszów jest piękny" wyświetl:
#Pierwszą literę w tekście,
# Siódmą, dziesiątą, trzynastą oraz drugą.
tekst = "Rzeszów jest piękny"
print(tekst[1])
print(tekst[7],tekst[10],tekst[13], tekst[2])

#zad 2.	Wyświetl z łańcucha tekst ="Python jest super" znaki o indeksach:
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

