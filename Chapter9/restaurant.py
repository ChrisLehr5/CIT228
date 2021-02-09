#Hands On #4 Part 1
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
