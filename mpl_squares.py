import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_value, squares, linewidth=5, color='green')

# tytul wykresu i osi
plt.title("Kwadraty liczb", fontsize=20)
plt.xlabel("wartość", fontsize=12)
plt.ylabel("kwadrat wartości", fontsize=12)
# wielkosc etykiet
plt.tick_params(axis='both', labelsize=12)

plt.show()
