
print("------------------Chapter 4, Hands On #3---------------------------")
animals = ["cow", "horse", "chicken", "goat", "cat", "donkey"]
print("---------------------Original List---------------------------------")
for animal in animals:
    print(animal)

print("-----------------------New List------------------------------------")
newAnimals= animals[:]
newAnimals.append("llama")
newAnimals.append("mink")
newAnimals.append("alpaca")
newAnimals.append("yak")
for animal in newAnimals:
    print(animal)

print()
print("------------------Chapter 4, Exercise 4-10--------------------------")
newAnimals= animals[:]
newAnimals.append("llama")
newAnimals.append("mink")
newAnimals.append("alpaca")
newAnimals.append("yak")
for animal in newAnimals:
    print(animal)
print("The first three items in the new list are: ", newAnimals[:3])
print("The middle three items in the new list are: ", newAnimals[3:6])
print("The last three items in the new list are: ", newAnimals[7:])
