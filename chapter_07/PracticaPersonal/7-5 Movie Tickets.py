while True:
    edad =int(input("Ingrese su edad"))
    if edad < 3:
        precio = 0
    elif edad <=12:
        precio = 10
    elif edad > 12:
        precio = 15
    print(f"El precio del ticket es {precio:.2f}")
