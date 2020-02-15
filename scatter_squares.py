import matplotlib.pyplot as plt

"""wykres punktowy"""

x_values = list(range(1, 51))
y_values = [x ** 2 for x in x_values]

# wlasny kolor
# plt.scatter(x_values, y_values, edgecolors='none', color=(0, 0, 0.5), s=40)
# mapa kolorow
plt.scatter(x_values, y_values, edgecolors='none', c=y_values, cmap=plt.cm.Greens, s=40)

# tytul wykresu i osi
plt.title("Kwadraty liczb", fontsize=20)
plt.xlabel("wartość", fontsize=12)
plt.ylabel("kwadrat wartości", fontsize=12)
# wielkosc etykiet
plt.tick_params(axis='both', which='major', labelsize=12)

# zakres dla kazdej osi
plt.axis([0, 55, 0, 3000])

# pokazanie wykresu
# plt.show()

# zapis wykresu do pliku
plt.savefig('squares.png')
