rios = {}
rios['amazonas'] = 'peru'
rios['nilo'] = 'egipto'
rios['sena'] = 'francia'
rios['misisipi'] = 'estados unidos'
rios['rin'] = 'alemania'

for key,value in rios.items():
    print(f'el rio {key.title()} corre a travez de {value.title()}')
    # The Nile runs through Egypt
# lista de todos los rios
for rio in rios:
    print(f'{rio}')
# lista de todos los paises de rios importantes
for paises in rios.values():
    print(paises)