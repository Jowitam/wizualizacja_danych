import pygal

from basic.dice import Dice

# utworzenie 2 kosci typu D6
dice_1 = Dice()
dice_2 = Dice()

# wykonanie pewnej liczby rzutow i wyniki na liscie
results = []
for roll_num in range(1000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

# analiza wynikow
frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# wizualizacja wynikow wystapien danej liczby oczek - wykres histogram
hist = pygal.Bar(title="Wynik rzucania dwiema kośćmi D6 tysiąc razy.", x_title="Wynik",
                 y_title="Częstotliwość występowania wartości")
hist.force_uri_protocol = 'http'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

hist.add('D6 +D6', frequencies)
hist.render_to_file('dice_visual_twice.svg')
