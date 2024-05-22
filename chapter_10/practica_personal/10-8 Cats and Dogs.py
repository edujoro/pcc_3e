from pathlib import Path

try:
    path_perros = Path('dogs.txt')
    path_gatos = Path('cats.txt')

    contenido_perros = path_perros.read_text()
    contenido_gatos = path_gatos.read_text()

    print(contenido_perros)
    print(contenido_gatos)
except FileNotFoundError:
    print('No existe el archivo')