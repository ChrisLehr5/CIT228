print("------------------Chapter 7, Hands On #2---------------------------")
import random 
problems = int(input("How many math problems would you like to practice?"))

keepGoing = 0

while keepGoing != -1:
    randNumber1 = random.randrange(1, 1000)
    randNumber2 = random.randrange(1, 1000)
    correctAnswer = int(randNumber1 / randNumber2)
    yourAnswer = int(input(f"What is the integer value of {randNumber1} / {randNumber2} "))
    if correctAnswer == yourAnswer:
        print("Great job, you answered correctly!")       
    else:
        print("Oops, the correct answer is ", correctAnswer)    
    
    keepGoing = int(input("If you would like to continue enter 1 or -1 to quit: "))
    
    if (keepGoing < 0 ) :
        print("Thanks for playing!")