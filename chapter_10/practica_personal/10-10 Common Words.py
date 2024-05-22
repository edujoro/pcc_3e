from pathlib import Path

path_libro = Path('el_quijote.txt')
libro = path_libro.read_text()
cantidad_repeticiones = libro.lower().count('la ')
print(cantidad_repeticiones)


path_libro = Path('crimen_y_castigo.txt')
libro = path_libro.read_text()
cantidad_repeticiones = libro.lower().count('la ')
print(cantidad_repeticiones)