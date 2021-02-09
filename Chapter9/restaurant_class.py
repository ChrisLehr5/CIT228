print("-------------------------------Chapter 9, Exercise 9-1-------------------------------")
class Restaurant():
    """Class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize attributes of the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe the restaurant."""
        msg = f"{self.name} serves {self.cuisine_type} cuisine."
        print(f"{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open."
        print(f"{msg}")

print("---------Here are your selections---------")
restaurant = Restaurant('The Strudel Shoppe', 'German')
print(f"Restaurant= ", restaurant.name)
print(f"Cuisine= " ,restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


print("-------------------------------Chapter 9, Exercise 9-2-------------------------------")

german_restaurant = Restaurant('The Strudel Shoppe', 'German')
chinese_restaurant = Restaurant('China Fair', 'Chinese')
greek_restaurant = Restaurant('Opa! Grill & Taproom', 'Greek')

german_restaurant.describe_restaurant()
chinese_restaurant.describe_restaurant()
greek_restaurant.describe_restaurant()
