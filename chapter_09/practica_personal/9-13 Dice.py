import random


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)


die = Die(6)
for i in range(1, 11):
    resultado = die.roll_die()
    print(f"Iteracion {i} resultado: {resultado}")

print()
die10 = Die(10)
die20 = Die(20)
for i in range(1, 11):
    resultado1 = die10.roll_die()
    resultado2 = die20.roll_die()
    print(f"Iteracion {i} resultado1: {resultado1}, resultado2: {resultado2}")
