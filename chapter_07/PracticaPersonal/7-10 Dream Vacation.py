# Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results of the poll.

vacaciones = {}

while True:
    nombre = input("Ingrese su nombre: ")
    if nombre == 'quit':
        break
    lugar = input("If you could visit one place in the world,where would you go?: ")

    vacaciones[nombre] = lugar



print(vacaciones)

print