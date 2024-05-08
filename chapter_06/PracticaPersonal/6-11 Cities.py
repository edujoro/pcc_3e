cities = {'lima': {'country': 'peru', 'population': '1 millon', 'fact': 'capital del perú'},
          'arequipa': {'country': 'peru', 'population': '500 mil', 'fact': 'ciudad blanca'},
          'cuzco': {'country': 'peru', 'population': '200 mil', 'fact': 'capital de los incas'}}

print(cities)
for k, valores_ciudad in cities.items():
    print(k)
    print(valores_ciudad)
    for key, valor in valores_ciudad.items():
        print(f'{key} : {valor} ')
