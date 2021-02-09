print("-------------------------------Chapter 9, Exercise 9-13-------------------------------")
from random import randint

class Die():
    """Represent a die"""

    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        """Return a random number between 1 and number of sides"""
        return randint(1, self.sides)

#Make a 6 sided die & roll 10 times
d6 = Die()

results = []
for roll_number in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a d6: ")
print(results)

#Make 10 sided die & roll 10 times

d10 = Die(sides = 10)

results = []
for roll_number in range(10):
    result = d10.roll_die()
    results.append(result)
print("10 rolls of a d10: ")
print(results)

#Make a 20 sided die & roll 10 times 

d20 = Die(sides = 20)

results = []
for roll_number in range(10):
    result = d20.roll_die()
    results.append(result)
print("10 rolls of a d20: ")
print(results)