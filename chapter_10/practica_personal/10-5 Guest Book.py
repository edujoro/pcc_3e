from pathlib import Path

lista_nombres = ""
while True:
    nombre = input("ingrese Nombre, para salir ingrese exit: ")
    if nombre == "exit":
        break
    lista_nombres += nombre + "\n"


path = Path('guest_book.txt')
path.write_text(lista_nombres)