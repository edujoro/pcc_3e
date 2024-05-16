class user:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.phone_number = ''
        self.birthday = ''
        self.gender = ''
        self.login_attempts = 0

    def describe_user(self):
        print('First Name: ' + self.first_name)
        print('Last_Name: ' + self.last_name)
        print('Age: ' + str(self.age))
        print('Email: ' + self.email)
        print('Phone_Number: ' + self.phone_number)

    def greet_user(self):
        print('Hello ' + self.first_name + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


usuario1 = user('John', 'Doe', 30, '<EMAIL1>')
usuario1.describe_user()
usuario1.increment_login_attempts()
usuario1.increment_login_attempts()
usuario1.increment_login_attempts()
usuario1.increment_login_attempts()
usuario1.increment_login_attempts()
usuario1.increment_login_attempts()
print(usuario1.login_attempts)
usuario1.reset_login_attempts()
print(usuario1.login_attempts)

