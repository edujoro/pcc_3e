from pathlib import Path
import json

path = Path('numero_favorito.txt')
contenido = path.read_text()
numero_favorito = json.loads(contenido)
print(f"El numero del favorito es {numero_favorito}")