class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is a {self.cuisine_type} restaurant")


    def open_restaurant(self):
        print(f"The restaurant is open")

restaurant1 = Restaurant("Isla escondida","Cevichería")
restaurant2 = Restaurant("Mis costillitas","Costillas")
restaurant3 = Restaurant("Rokys","pollería")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()