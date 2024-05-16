class user:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.phone_number = ''
        self.birthday = ''
        self.gender = ''

    def describe_user(self):
        print('First Name: ' + self.first_name)
        print('Last_Name: ' + self.last_name)
        print('Age: ' + str(self.age))
        print('Email: ' + self.email)
        print('Phone_Number: ' + self.phone_number)

    def greet_user(self):
        print('Hello ' + self.first_name + self.last_name)


class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(user):
    def __init__(self, first_name, last_name, age, email, privileges):
        super().__init__(first_name, last_name, age, email)
        self.privileges = Privileges(privileges)


lista_privilegios = ["can add post", "can delete post", "can ban user"]
administrator1 = Admin('John', 'Doe',30,'aaa@bbb.com',lista_privilegios)

administrator1.describe_user()
administrator1.privileges.show_privileges()