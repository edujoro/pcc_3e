def show_messages(mensajes):
    for mensaje in mensajes:
        print(mensaje)


def send_messages(mensajes, mensajes_enviados):
    while mensajes:
        mensaje = mensajes.pop()
        print(mensaje)
        mensajes_enviados.append(mensaje)


lista_mensajes = ['Hola mundo', 'Como esto', 'Hola', 'Que hay de nuevo']
show_messages(lista_mensajes)
sent_messages = []
send_messages(lista_mensajes, sent_messages)

print('Lista_mensajes')
print(lista_mensajes)
print('sent_messages')
print(sent_messages)