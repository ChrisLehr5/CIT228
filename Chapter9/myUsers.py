print("-------------------------------Hands On #4, Part Two-------------------------------")
from user import User
from privileges import Privileges 
from admin import Admin


christine = Admin('christine', 'largent', 'CML','me@email.com', 'KittyKat5')
christine.describe_user()

christine_privileges = [
    'Reset passwords',
    'Can suspend accounts',
    'Can add posts'
]

christine.privileges.privileges = christine_privileges
christine.privileges.show_privileges()