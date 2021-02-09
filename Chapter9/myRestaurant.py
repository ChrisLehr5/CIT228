from restaurant import Restaurant
from icecream import IceCreamStand

print("-------------------------------Hands On #4, Part One-------------------------------")
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