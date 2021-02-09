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

print("-------------------------------Chapter 9, Exercise 9-6-------------------------------")
#Couldn't get the loop to exit when inputting the number of ice cream stands
#number = input("How many Ice Cream Stands are you entering?")
#number = int(number)
counter= 0
flavorList=[]
#while counter<number:
name = input("Enter the name of the Ice Cream stand: ")    
flavor = input("Enter the ice cream flavors or q to quit: ")
tempFlavors=[]
while flavor !="q":
    tempFlavors.append(flavor)
    flavor = input("Enter the ice cream flavors or q to quit: ")
served =IceCreamStand(       
    name = name,
    cuisine_type= "Ice Cream",
    flavors = tempFlavors
)
print("------------------------------------------------------------------------------------")
served.describe_restaurant()
served.display_flavors()
#flavorList.append(served)
#counter += 1   

print("------------------------------------------------------------------------------------")
for f in flavorList:
    f.describe_restaurant()
    f.display_flavors()