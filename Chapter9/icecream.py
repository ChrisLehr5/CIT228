#Hands On #4 Part 1
from restaurant import Restaurant

class IceCreamStand(Restaurant):   
    """Class representing an ice cream stand."""
    def __init__(self, name, cuisine_type, flavors):        
        super().__init__(name, cuisine_type, flavors)
        self.flavors = flavors

    def display_flavors(self):
        """Display the flavors available."""
        print("\nThe following flavors are available:")
        for f in self.flavors:
            print(f.title())