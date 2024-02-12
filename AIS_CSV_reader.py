# Statystyka z danych AIS
# Ile unikatowych statków
# Ile statków (jaki procent) danej bandery
# Typy statków (jaki procent)
# Przedziały długości (LOA - 0-100m 

# Sprawdzić i wypisać, które statki mineły się w jakiej (najbliższej odległości)

# imports
import csv
from typing import List

# variables
count = 1               # pomocnicza zmienna funkcji print_data
sustain = 1             # zmienna podtrzymująca petle while
mmsi_ships = []         # unikatowe numery MMSI należace do nadajnikow typu A i B
mmsi_all = []           # wszystkie unikatowe nr MMSI
mmsi_countries = []     # lista mmsi państw z unikatowych nr MMSI
countries = []          # lista kraji z unikatowych MMSI

unique_countries = []
counted_countries = []  # lista wystąpień nazw państwa



def print_data():
    global count
    # Otwiera plik w csv
    with open('ship_ais.csv', newline='') as csvfile:
        # Tworzy listę z pliku csv
        reader = csv.DictReader(csvfile)
        # petla pobierania danych dla otwartego pliku
        # Do kazdej kolumny mozna odwolac sie po jej nazwie
        for row in reader:
            # nadaje numer rzedowi
            print(f'number: {count}')
            # podaje czas pozyskania danych
            print(row['# Timestamp'])
            # podaje rodzaj AIS
            print(row['Type of mobile'])
            # podaje numer MMSI
            print(row['MMSI'])
            # Podaje szerokość
            print(row['Latitude'])
            # Podaje długość
            print(row['Longitude'])
            # Podaje status nawigacyjny oraz wprowadza przerwę między liniami
            print(f'{row["Navigational status"]} \n')
            count += 1


# Unikatowe statki
# Nalezy otworzyc plik i dodawac kolejne numery MMSI tak, aby nie powtarzaly sie
# Dodatkowe kryterium to rodzaj nadajnika
def c_vessels():
    # komunikat
    print('Program się nie zawiesił. To może potrwać pare minut.')
    # tworzy liste
    global mmsi_ships
    #  Otwiera plik csv
    with open('ship_ais.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Uwzgledninie wylacznie statkow
            if row['Type of mobile'] == 'Class A':
                # dla troubleshootingu odkomentowac nizej
                # print('A')
                # jezeli numeru mmsi nie ma w liscie dodaje go do listy
                if row['MMSI'] not in mmsi_ships:
                    mmsi_ships.append(row['MMSI'])
            elif row['Type of mobile'] == 'Class B':
                # dla troubleshootingu odkomentowac nizej
                # print('B')
                # jezeli numeru mmsi nie ma w liscie dodaje go do listy
                if row['MMSI'] not in mmsi_ships:
                    mmsi_ships.append(row['MMSI'])
            # else:
                # dla troubleshootingu odkometowac nizej oraz else
                # print('other')
    # wyswietla ilosc unikatowych numerow mmsi ktore sa w liscie
    print(f'Number of vessels: {len(mmsi_ships)}')


# Tu szukamy wszystkich unikatowych numerów MMSI
def c_MMSI():
    # komunikat
    print('Program się nie zawiesił. To może potrwać pare minut.')
    # potrzebna lista
    global mmsi_all
    #  Otwiera plik csv
    with open('ship_ais.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Uwzgledninie wylacznie statkow
            if row['MMSI'] not in mmsi_all:
                mmsi_all.append(row['MMSI'])
    # wyswietla ilosc unikatowych numerow mmsi ktore sa w liscie
    print(f'Number of vessels: {len(mmsi_all)}')


def c_countries():
    # komunikat
    print('Program się nie zawiesił. To może potrwać pare minut.')
    # potrzebna lista
    global mmsi_countries, unique_countries, counted_countries
    with open('ship_ais.csv', newline='') as csvfile:
        AIS = csv.DictReader(csvfile)
        for row in AIS:
            # Uwzgledninie wylacznie statkow
            if row['Type of mobile'] == 'Class A':
                # dla troubleshootingu odkomentowac nizej
                # print('A')
                # jezeli numeru mmsi nie ma w liscie dodaje go do listy
                if row['MMSI'] not in mmsi_ships:
                    mmsi_countries.append(row['MMSI'])
            elif row['Type of mobile'] == 'Class B':
                # dla troubleshootingu odkomentowac nizej
                # print('B')
                # jezeli numeru mmsi nie ma w liscie dodaje go do listy
                if row['MMSI'] not in mmsi_ships:
                    mmsi_countries.append(row['MMSI'])
    with open('MID_MMSI.csv', newline='') as csvMMSI:
        MID = csv.DictReader(csvMMSI)
        for i in range(len(mmsi_countries)):
            print(i)
            for row in MID:
                if mmsi_countries[i][:3] == row['Digit']:
                    countries.append(row['Allocated to'])
    unique_countries = set(countries)
    for j in unique_countries:
        country_j = countries.count(j)
        counted_countries.append(country_j)
    for t in unique_countries:
        print(f'Liczba kraj: {unique_countries[t]} ma {counted_countries[t]} statków')


# pozwala na selektywne uruchomienie funkcji
while sustain == 1:
    u_in = input()
    # dla podania wybranych danych
    if u_in == 'print_data':
        print_data()
    # Podanie wszystkich unikatowych
    if u_in == 'Count MMSI':
        c_MMSI()
    # Dla podania liczby statkow
    if u_in == 'Count Vessels':
        c_vessels()
    if u_in == 'Count Countries':
        c_countries()
    if u_in == 'quit':
        sustain -= 1

