class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is a {self.cuisine_type} restaurant")


    def open_restaurant(self):
        print(f"The restaurant is open")


restaurant = Restaurant("Mama Julia2","cevichería")
print(restaurant.number_served)
restaurant.number_served = 100
print(restaurant.number_served)