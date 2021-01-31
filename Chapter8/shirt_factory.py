print("------------------Chapter 8, Exercise 8-3 & 8-4---------------------------")
#def make_shirt(size, message):
#    """Sumarrize the shirt that is going to be made."""
#    print(f"\nI'm going to make a {size} t-shirt.")
#    print(f"It will say, {message}")

#make_shirt("large", "'I love Python!'")
#make_shirt("medium","Python is best snake!")
#make_shirt("small", "This is confusing LOL!")

def make_shirt(size="large", message="I love Python!"):
    """Sumarrize the shirt that is going to be made."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f"It will say, {message}")

make_shirt()
make_shirt(size="medium")
make_shirt("small", "This is still confusing LOL!")