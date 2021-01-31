print("------------------Chapter 7, Exercise 7-8 & 7-9---------------------------")
sandwich_orders = ["Chicken", "pastrami","Egg", "Tuna", "Pulled Pork","pastrami", "Peanut Butter", "Ham", "Steak", "Vegan", "pastrami"]
finished_sandwiches = []

print("I am sorry, we are out of pastrami!")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich.title()} sandwich")
    finished_sandwiches.append(current_sandwich)

print("\nSandwiches made today include:")
for s in finished_sandwiches:
    print(s.title())














