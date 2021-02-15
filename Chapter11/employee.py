print("-----------------------------------Hands On #2, Exercise 11-3------------------------------------------")
class Employee():
    """A class to represent employee"""

    def __init__(self, firstName, lastName, salary):
        """Initialize the employee"""
        self.firstName = firstName.title()
        self.lastName = lastName.title()
        self.salary = salary
    
    def give_raise(self, amount = 5000):
        """Give employee raise"""
        self.salary += amount 