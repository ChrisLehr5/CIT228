print("------------------Chapter 7, Exercise 7-3---------------------------")
number = input("Give me a number: ")
number = int(number) 

if number % 10 == 0:
    print(f"{number} is a multiple of ten.")
else:
    print(f"The number {number} is not a multiple of ten.")