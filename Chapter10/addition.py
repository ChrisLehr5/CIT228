print("------------------------------Hands On #1, Exercise 10-6 & 10-7-----------------------------------------")
def addition(n,d):   
    return n + d

quit=""
while quit != "q": 
    
    try:
        n = input("Please enter the first number: ")
        n = int(n)
        d = input("Please enter the second number: ")
        d = int(d)
        print(n, "+", d, "=", addition(n,d))
    except ValueError:
        print("You need to use a number, not text. Try again!")        
       
        while quit != "q": 
    
            try:
                n = input("Please enter the first number: ")
                n = int(n)
                d = input("Please enter the second number: ")
                d = int(d)
                print(n, "+", d, "=", addition(n,d)) 
                break   
              
            except ValueError:
                print("You need to use a number, not text. Try again!") 
    
    finally:
        print("Thanks for playing!")      
 
    quit=input("Would you like to continue, q to quit? ")  
    
    


