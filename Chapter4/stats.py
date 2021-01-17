
print("------------------Chapter 4, Hands On #2---------------------------")
import random 

number = random.randrange(10,100)
numList = list(range(number))
print(numList)

print("The largest number = ", max(numList))
print("The smallest number =", min(numList))
print("The total of all the numbers =", sum(numList))
print("The average number =", sum(numList)/len(numList))