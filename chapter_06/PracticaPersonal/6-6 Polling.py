favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
personas_examinadas = ['jen','phil']
for k, v in favorite_languages.items():
    if k in personas_examinadas:
        print(f"{k.title()} Gracias por tomar el examen a tiempo")
    else:
        print(f"{k.title()} Por favor tomar el examen")