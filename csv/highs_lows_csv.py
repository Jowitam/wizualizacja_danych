import csv

filname = 'sitka_weather_07_2014.csv'
with open(filname) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # wyswietlenie naglowkow i ich polozenia
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # wyodrebnienie i odczytanie danych
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
    print(highs)
