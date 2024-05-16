class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is a {self.cuisine_type} restaurant")

    def open_restaurant(self):
        print(f"The restaurant is open")


class IceCream(Restaurant):
    def __init__(self, restaurant_name,cuisine_type, flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)

lista_sabores = ['limon', 'apple', 'banana', 'fresa']
IceCream_restaurant = IceCream("Mama Julia", "heladería", lista_sabores)
IceCream_restaurant.describe_restaurant()
IceCream_restaurant.show_flavors()
