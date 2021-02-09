#"------------------------------Hands On #4 Part Two-----------------------------------------")
from user import User
from privileges import Privileges 

class Admin(User):
    """Admin Profile"""    
    def __init__(self,first_name,last_name,username,email,password):
        super().__init__(first_name,last_name,username,email,password)
        self.privileges= Privileges()