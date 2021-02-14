print("------------------------------Hands On #2, Exercise 10-3-----------------------------------------")
"""# name = input("What is your name? ")

filename = 'C:/Users/Khyr/Desktop/CIT228/Chapter10/guests.txt'

# with open(filename, 'w') as file_object:
#     file_object.write(name)

print("------------------------------Hands On #2, Exercise 10-4-----------------------------------------")
# Non book example of while loop 
# print("Please enter 'quit' when finished.")
# while True:
#     name = input("\nWhat is your name? ")
#     if name == "quit":
#         break
#     else:
#         with open(filename, 'a') as file_object:
#             file_object.write(f"{name}\n")
#             print(f"Hello {name}, you've been added to the guest book.") 

# Book example 
name = input("What is your name (q to quit) ?")
while name!='q':
    with open(filename, 'a') as file_object:        
        file_object.write(f"{name}\n")        
        print(f"Hello {name}, you've been added to the guest book.")
        print("---------------------------------------------------")
        name = input("What is your name (q to quit) ?")
        """
import random
import os

filename = 'C:/Users/Khyr/Desktop/CIT228/Chapter10/guests.txt'
#delete existing file if exists 
if os.path.exists(filename):
    os.remove(filename)
#create new file 
rooms = []
with open(filename, "w") as guestFile:
   guest = input("What is your name (q to quit) ?")
   while guest !='q':
       number= random.randint(1,50)       
       while number in rooms:
           number = random.randint(1,50)
#Need to add oprator about the already existing number           
       print(f"Hello {guest}, you've been added to the guest book.")
       print(f"Your room will be {number}. Enjoy your stay!")
       rooms.append(number)
       guest+=", Room# " + str(number) + "\n"
       guestFile.write(guest)
       guest = input("What is your name (q to quit) ?")
#Read new file 
with open(filename) as guestFile:
    print("---------------------------------------------------")
    print("--------------Rooms and Guests---------------------")
    for line in guestFile:
        print(line)


    