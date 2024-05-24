from pathlib import Path
import json

path = Path('numero_favorito_2.txt')
if path.exists():
    #extrae valor del path
    contenido = path.read_text()
    numero_favorito = json.loads(contenido)
    print(f"El numero del favorito es {numero_favorito}")
else:
    numero_favorito = int(input("Ingrese su número favorito: "))
    contenido = json.dumps(numero_favorito)
    path.write_text(contenido)
