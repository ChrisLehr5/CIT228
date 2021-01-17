# Hands on 1- creating and accessing lists 
foods =["pizza", "ice cream", "cheese", "chocolate", "apples", "hardboiled eggs"]
numbers =[7, 25, 15, 5 , 7777, 17]
movies =["Lord of The Rings", "Wizards", "Ordinal Scale"]
combo =["cheese", "pizza", 17, 7777, "Ordinal Scale", "Lord of The Rings"]

print("------------------Hands On #1---------------------------")
print(f"Favorite Foods: {foods}")
print(f"Lucky Numbers: {numbers}")
print(f"Favorite Movies: {movies}")
# The easy way to do a combo list 
# print(f"Combo List: {combo}")
print(f"Combo List: {foods[-1]}, {foods[0]}, {numbers[-1]} {numbers[-4]}, {movies[0]}, {movies[-1]}")
print(f"Last Food Item = {foods[-1]}")
print(f"2nd, 4th, and 6th numbers: {numbers[-5]}, {numbers[-3]}, {numbers[-1]}")
print(f"All Three Movies = {movies[0]}, {movies[-2]}, {movies[-1]}")
print(f"First Food, First Number, and First Movie: {foods[0]}, {numbers[0]}, {movies[0]}")

print("------------------Hands On #2---------------------------")
movies.append("The Rock")
print("Movie added to the end: ", movies)

numbers.insert(3,99)
print("Number added to position 3: ", numbers)

foods.insert(5, "cheesecake")
print("Food added to position 5: ", foods)

del foods[0]
print("Removed an item from the food list: ", foods)

numbers.pop()
print("Deleted a number from the end: ", numbers)

numbers.pop(2)
print("Deleted subscript 2: ", numbers)

print("------------------Hands On #3---------------------------")
movies.sort()
print("Sorted List: ", movies)

foods.sort()
print("Sorted List: ", foods)

print("Temp Sorted List: ", sorted(numbers))
print("Original List: ",numbers)

movies.reverse()
print("Sorted List Reverse Order: ", movies)