import random

# Crear una lista con 10 números y 5 letras
elementos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Seleccionar aleatoriamente 4 elementos de la lista
seleccionados = random.sample(elementos, 4)

# Crear el mensaje
mensaje = f"Cualquier boleto que coincida con estos 4 números o letras: {seleccionados} gana un premio."

# Imprimir el mensaje
print(mensaje)

mi_seleccion = [5, 2, 'A', 'B']
contador = 0
while True:
    seleccionados = random.sample(elementos, 4)
    if set(mi_seleccion) == set(seleccionados):
        break
    contador += 1

print(f"Se encontró luego de {contador} iteraciones")
# Crear el mensaje
mensaje = f"Cualquier boleto que coincida con estos 4 números o letras: {seleccionados} gana un premio."

# Imprimir el mensaje
print(mensaje)