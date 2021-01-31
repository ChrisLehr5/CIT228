print("------------------Chapter 7, Exercise 7-2---------------------------")
seatCount = input("How many people are in your dinner party? ")
seatCount = int(seatCount)
if seatCount >= 8:
    print("Please wait in the lounge until a table is available.")
else:
    print("Your table is ready, please follow me.")
