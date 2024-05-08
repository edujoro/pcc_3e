lugares_favoritos = {}
lugares_favoritos['mario'] = ['cuba', 'alemania', 'argentina']
lugares_favoritos['marcela'] = ['chile', 'peru', 'mexico', 'india']
lugares_favoritos['patricia'] = ['estados unidos', 'canada', 'dinamarca']

for persona, lugares in lugares_favoritos.items():
    print(f'\n {persona} ')
    for lugar in lugares:
        print(f'\t{lugar}')