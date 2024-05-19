from pathlib import Path

lineas = Path('learning_python.txt').read_text().splitlines()

for linea in lineas:
    print(linea.replace('Python', 'C'))
