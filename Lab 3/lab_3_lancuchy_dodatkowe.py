# Wczytaj zdanie od użytkownika
zdanie = input("Wprowadź zdanie: ")

# Usuń spacje i zamień na małe litery
zdanie = zdanie.replace(" ", "").lower()

# Utwórz zbiór z literami występującymi w zdaniu
litery_w_zdaniu = set(zdanie)

# Utwórz zbiór z alfabetem
alfabet = set("abcdefghijklmnopqrstuvwxyz")

# Posortuj litery alfabetycznie i wypisz
posortowane_litery = sorted(litery_w_zdaniu)
print("Litery w kolejności alfabetycznej:", " ".join(posortowane_litery))

# Oblicz i wypisz brakujące litery
brakujace_litery = sorted(alfabet - litery_w_zdaniu)
if brakujace_litery:
    print("Brakujące litery alfabetu:", " ".join(brakujace_litery))
else:
    print("Zdanie zawiera wszystkie litery alfabetu.")
