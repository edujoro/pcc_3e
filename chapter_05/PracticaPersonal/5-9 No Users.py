usernames = [] #['admin', 'edu', 'jorge','luis','petra']
if usernames:
    for username in usernames:
        if username == 'admin':
            print('buenos días username, te gustaría ver un resporte del estado del sistema')
        else:
            print(f'buenos dias {username}, gracias por loguearte al sistema')
else:
    print('Necesitamos encontrar algunos usuarios')
