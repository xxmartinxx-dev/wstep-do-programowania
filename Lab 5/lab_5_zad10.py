#10. Napisz program, który po otrzymaniu od użytkownika roku, miesiąca i dnia zwróci:
#a. Dzień roku (pamiętaj o latach przestępnych)
#b. Numer tygodnia
#c. Datę na 2 tygodnie przed i po
#d. Datę najbliższej niedzieli
#e. Czas unixowy bieżącej godziny w podanym dniu
import datetime

def czy_przestepny(rok):
    return (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0)

def dzien_roku(data):
    pierwszy_dzien_roku = datetime.date(data.year, 1, 1)
    return (data - pierwszy_dzien_roku).days + 1

def numer_tygodnia(data):
    return data.isocalendar()[1]

def data_przed_po(data):
    dzien_przed = data - datetime.timedelta(days=14)
    dzien_po = data + datetime.timedelta(days=14)
    return dzien_przed, dzien_po

def najblizsza_niedziela(data):
    dni_do_niedzieli = (6 - data.weekday() + 7) % 7
    return data + datetime.timedelta(days=dni_do_niedzieli)

def czas_unixowy(data):
    return int((data - datetime.datetime(1970, 1, 1)).total_seconds())

if __name__ == "__main__":
    try:
        rok = int(input("Podaj rok: "))
        miesiac = int(input("Podaj miesiąc: "))
        dzien = int(input("Podaj dzień: "))

        data = datetime.date(rok, miesiac, dzien)

        print(f"Dzień roku: {dzien_roku(data)}")
        print(f"Numer tygodnia: {numer_tygodnia(data)}")

        dzien_przed, dzien_po = data_przed_po(data)
        print(f"Data 2 tygodnie przed: {dzien_przed}")
        print(f"Data 2 tygodnie po: {dzien_po}")

        najblizsza_niedz = najblizsza_niedziela(data)
        print(f"Najbliższa niedziela: {najblizsza_niedz}")

        czas_unix = czas_unixowy(datetime.datetime(rok, miesiac, dzien))
        print(f"Czas Unixowy bieżącej godziny: {czas_unix}")
    except ValueError:
        print("Podano nieprawidłowe dane.")