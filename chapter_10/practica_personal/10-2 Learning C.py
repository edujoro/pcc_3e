from pathlib import Path

ruta_archivo = 'learning_python.txt'
path = Path(ruta_archivo)
archivo = path.read_text()
lineas = archivo.splitlines()

for linea in lineas:
    print(linea.replace('Python', 'C'))