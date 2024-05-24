from pathlib import Path
import json

path = Path('numero_favorito.txt')
numero_favorito = int(input("Ingrese su número favorito: "))
contenido = json.dumps(numero_favorito)
path.write_text(contenido)