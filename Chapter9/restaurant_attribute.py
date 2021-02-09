class Restaurant():
    """Class representing a restaurant."""

    def __init__(self, name, cuisine_type, number_served=0):
        """Initialize attributes of the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type   
        self.number_served = number_served  

    def describe_restaurant(self):       
        print(f"{self.name} serves {self.cuisine_type} cuisine.")        

    def open_restaurant(self):      
        print(f"{self.name} is open.")
        
    def set_number_served(self, served):        
        self.number_served = int(served)

    def increment_number_served(self, served):        
        self.number_served += int(served)

print("-------------------------------Chapter 9, Exercise 9-4-------------------------------")
restaurant = Restaurant('The Strudel Shoppe', 'German', 4)
restaurant.open_restaurant()
restaurant.describe_restaurant()
#printing number served 
print(f"Initial customers served is ", restaurant.number_served)
#changing number served 
restaurant.number_served = 20
print(f"The new number of customers served is ", restaurant.number_served)
#using set_number_served method to change customers served 
served = input("How many customers have been served?")
restaurant.set_number_served(served)
print(f"The new number of customers served is ", restaurant.number_served)
#adding customers served using increment
served = input("How many additional customers have been served?")
restaurant.increment_number_served(served)
print("The total number of customers served is ", restaurant.number_served)