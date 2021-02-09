#"------------------------------Hands On #4 Part Two-----------------------------------------")

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