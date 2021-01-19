print("------------------Chapter 5, Exercise 5-10--------------------------")
current_users = ["clargent", "aeldis", "mlehr", "nancy", "kree"]
new_users = ["Aeldis", "Mlehr", "frnk5", "norbert", "lisle"]

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} : That user name is taken. Please enter a different user name.")
    else:
        print(f"{new_user} : That user name is available.")