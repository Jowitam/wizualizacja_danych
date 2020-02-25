import pygal

from dice import Dice

# utworzenie kosci typu D6
dice = Dice()

# wykonanie pewnej liczby rzutow i wyniki na liscie
results = []
for roll_num in range(1000):
    result = dice.roll()
    results.append(result)

# analiza wynikow
frequencies = []
for value in range(1, dice.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# wizualizacja wynikow wystapien danej liczby oczek - wykres histogram
hist = pygal.Bar(title="Wynik rzucania pojedynczą kością D6 tysiąc razy.", x_title="Wynik",
                 y_title="Częstotliwość występowania wartości")
hist.force_uri_protocol = 'http'
hist.x_labels = ['1', '2', '3', '4', '5', '6']

hist.add('D6', frequencies)
hist.render_to_file('dice_visual.svg')
