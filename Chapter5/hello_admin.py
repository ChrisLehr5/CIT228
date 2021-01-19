print("------------------Chapter 5, Exercise 5-8---------------------------")
users = ["Admin", "Christine", "Max", "Tim", "Bill"]

for user in users:
    if user == "Admin":
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")

print("------------------Chapter 5, Exercise 5-9--------------------------")
users = []

for user in users:
    if user == "Admin":
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")

