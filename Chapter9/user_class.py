print("-------------------------------Chapter 9, Exercise 9-3-------------------------------")
class User():
    """Simple User Profile"""

    def __init__(self, first_name, last_name, username, email, password):
        """Initialize user attributes"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.password = password
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """Increment login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset attempts back to zero"""
        self.login_attempts = 0  

print("---------------------------------------------------------------------")
christine = User('Christine', 'Largent', 'CL5', 'Me@me.com', 'kites%9')
christine.describe_user()
christine.welcome_user()
print("---------------------------------------------------------------------")
larry = User('Larry', 'Porter', 'Lp2000', 'larry@email.com', 'password')
larry.describe_user()
larry.welcome_user()
print("---------------------------------------------------------------------")
karla = User('Karla', 'Glacier', 'FuzzyKat', 'kkat@aol.com', 'admin')
karla.describe_user()
karla.welcome_user()

print("-------------------------------Chapter 9, Exercise 9-5-------------------------------")
max = User('Max', 'Lehr', 'MLX', 'Max@me.com', 'kites55%9')
max.describe_user()
max.welcome_user()
max.increment_login_attempts()
print(f"Max has tried to login {max.login_attempts} times!")
max.increment_login_attempts()
print(f"Max has tried to login {max.login_attempts} times!")
max.increment_login_attempts()
print(f"Max has tried to login {max.login_attempts} times!")
max.increment_login_attempts()
print(f"Max has tried to login {max.login_attempts} times!")
max.increment_login_attempts()
print(f"Max has tried to login {max.login_attempts} times!")
max.increment_login_attempts()
print(f"Max has tried to login {max.login_attempts} times!")

if max.login_attempts >=6 :
    print("You have exceeded the number of login attempts!")
    max.reset_login_attempts()
    print(f"The number of attempts has been reset to: {max.login_attempts}")
    print("Your account has been locked for 30 minutes, please try back later!")



