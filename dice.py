from random import randint

class Dice:
    """Klasa przedstawiajaca pojedyncza kosc"""
    def __init__(self, num_sides=6):
        """kosc do gry jest szescianem"""
        self.num_sides = num_sides

    def roll(self):
        """zwrot wartosci z zakresu od 1 do liczby scianek, ktore ma kosc"""
        return randint(1, self.num_sides)
