import user2
class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(user2.User):
    def __init__(self, first_name, last_name, age, email, privileges):
        super().__init__(first_name, last_name, age, email)
        self.privileges = Privileges(privileges)