current_users = ['marcela','diego','armando','betty','patricia','bertha']
current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

new_users = ['Patricia','BEtty','greta']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("Por favor escoger otro nombre de usuario")
    else:
        print("el nombre de usuario está disponible")
