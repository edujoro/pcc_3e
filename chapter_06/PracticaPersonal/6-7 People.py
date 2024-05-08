persona = {}
persona['first_name'] = 'Raul'
persona['last_name'] = 'Navarro'
persona['age'] = '34'
persona['city'] = 'Lima'

persona_01 = {}
persona_01['first_name'] = 'jhonny'
persona_01['last_name'] = 'zuniga'
persona_01['age'] = '32'
persona_01['city'] = 'pucalpa'

persona_02 = {}
persona_02['first_name'] = 'mario'
persona_02['last_name'] = 'obregon'
persona_02['age'] = '29'
persona_02['city'] = 'puno'

people = [persona,persona_01, persona_02]

for person in people:
    print(person)