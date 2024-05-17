# import random
#
# lista = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e']
# lista_ganadora = random.choices(lista,k=4)
# print(f"Random number is {lista_ganadora} y gana el premio")


import random

# Crear una lista con 10 números y 5 letras
elementos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Seleccionar aleatoriamente 4 elementos de la lista
seleccionados = random.sample(elementos, 4)

# Crear el mensaje
mensaje = f"Cualquier boleto que coincida con estos 4 números o letras: {seleccionados} gana un premio."

# Imprimir el mensaje
print(mensaje)
