# print("-------------------------------Chapter 9, Exercise 9-7-------------------------------")
# class User():
#     """Simple User Profile"""

#     def __init__(self, first_name, last_name, username, email, password):
#         """Initialize user attributes"""
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.username = username
#         self.email = email
#         self.password = password

#     def describe_user(self):
#         """Describe the user"""
#         print(f"\n{self.first_name} {self.last_name}")
#         print(f"Username: {self.username}")  
#         print(f"Email: {self.email}")
#         print(f"Password:{self.password}")

#     def welcome_user(self):
#         """Personalized welcome"""
#         print(f"\nWelcome back, {self.first_name}")
#         print(f"{self.first_name} {self.last_name} has a username of {self.username},")
#         print(f"a password of {self.password} and an email address of {self.email}")

# class Admin(User):
#     """Admin Profile"""    
#     def __init__(self,first_name,last_name,username,email,password):
#         super().__init__(first_name,last_name,username,email,password)
#         self.privileges= []  

#     def show_privileges(self):
#         print("\nPrivileges: ")
#         for privilege in self.privileges:
#             print(f"{privilege}")   

# christine = Admin('christine', 'largent', 'CML','me@email.com', 'KittyKat5')
# christine.describe_user()

# christine.privileges = [
#     'Reset passwords',
#     'Can suspend accounts',
#     'Can add posts'
# ]

# christine.show_privileges()

print("-------------------------------Chapter 9, Exercise 9-8-------------------------------")
class User():
    """Simple User Profile"""

    def __init__(self, first_name, last_name, username, email, password):
        """Initialize user attributes"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.password = password

    def describe_user(self):
        """Describe the user"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Username: {self.username}")  
        print(f"Email: {self.email}")
        print(f"Password:{self.password}")

    def welcome_user(self):
        """Personalized welcome"""
        print(f"\nWelcome back, {self.first_name}")
        print(f"{self.first_name} {self.last_name} has a username of {self.username},")
        print(f"a password of {self.password} and an email address of {self.email}")

class Admin(User):
    """Admin Profile"""    
    def __init__(self,first_name,last_name,username,email,password):
        super().__init__(first_name,last_name,username,email,password)
        self.privileges= Privileges()

class Privileges():  

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")        

christine = Admin('christine', 'largent', 'CML','me@email.com', 'KittyKat5')
christine.describe_user()

christine_privileges = [
    'Reset passwords',
    'Can suspend accounts',
    'Can add posts'
]

christine.privileges.privileges = christine_privileges
christine.privileges.show_privileges()