corta = True
while corta:
    ingrediente =input("Ingrese pizza toppings, sino ingrese quit para salir")


    if ingrediente == 'quit':
        corta = False
        break
    else:
        print(f'Se ingresará {ingrediente} a su pizza')



