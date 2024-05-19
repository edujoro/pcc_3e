from pathlib import Path

ruta = 'learning_python.txt'
path = Path(ruta)

# tomamos el contenido del archivo en una variable contenido
contenido = path.read_text().rstrip()
# imprimimos todo el archivo
print(contenido)

# tomamos el contenido de la variable y la dividimos en una lista de líneas
lineas = path.read_text().splitlines()

# imprimimos el archivo línea por línea
for linea in lineas:
    print(linea)

print(type(lineas))
