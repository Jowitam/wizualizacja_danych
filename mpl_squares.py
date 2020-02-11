import matplotlib.pyplot as plt

input_value = list(range(1, 21))
squares = [x**2 for x in input_value]

plt.plot(input_value, squares, linewidth=5, color='green')

# tytul wykresu i osi
plt.title("Kwadraty liczb", fontsize=20)
plt.xlabel("wartość", fontsize=12)
plt.ylabel("kwadrat wartości", fontsize=12)
# wielkosc etykiet
plt.tick_params(axis='both', labelsize=12)

plt.show()
