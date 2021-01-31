print("------------------Chapter 8, Exercise 8-12---------------------------")

def make_sandwich(*toppings):
    """Making a sandwich with different topping amounts"""
    print("\nMaking you a sandwich!")
    for topping in toppings:
        print(f"Adding {topping} to your sandwich.")
    print("Here you go!")

make_sandwich("ham","swiss","mustard","mayo")
make_sandwich("peanut butter","bananna","brown sugar")
make_sandwich("peanut butter", "jelly")
    