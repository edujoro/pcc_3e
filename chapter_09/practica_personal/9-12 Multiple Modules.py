import admin

lista_privilegios = ["can add post", "can delete post", "can ban user"]
administrator1 = admin.Admin('John', 'Doe', 30, 'aaa@bbb.com', lista_privilegios)

administrator1.describe_user()
administrator1.privileges.show_privileges()
