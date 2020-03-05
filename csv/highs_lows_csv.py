import csv
from datetime import datetime

from matplotlib import pyplot as plt

filname = 'sitka_weather_2014.csv'
with open(filname) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # wyswietlenie naglowkow i ich polozenia
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # wyodrebnienie i odczytanie danych
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'Brak danych.')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# dane wykresu
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

# formatowanie wykresu
plt.title("Najwyzsza i najnizsza temperatura dnia w 2014", fontsize=20)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()

plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.ylabel("temperatura", fontsize=16)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
