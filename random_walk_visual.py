import matplotlib.pyplot as plt

from random_walk import RandomWalk

# tworzenie nowego bladzenia losowego dopoki program aktywny
while True:
    # przygotowanie danych bladzenia losowego i wyswietlenie punktow
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values, rw.y_values, s=15, c=point_numbers, cmap=plt.cm.Greens, edgecolors='none')

    # podkreslenie pierwszego i ostatniego punktu
    plt.scatter(0, 0, c='red', edgecolors='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', edgecolors='none', s=50)

    # ukrycie osi
    plt.xticks([])
    plt.yticks([])

    plt.show()

    keep_running = input("Utworzyć kolejne błądzenie losowe? (t/n): ")
    if keep_running == "n":
        break
