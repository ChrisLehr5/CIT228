print("------------------Exercise 3-4---------------------------")
guests = ["Artemisia Gentileschi", "Cohhcarnage", "Elizabeth Tudor"]
dinnermsg = "can you make it to dinner this Saturday?"
print(f"{guests[0]}, {dinnermsg}")
print(f"{guests[-1]}, {dinnermsg}")
print(f"{guests[-2]}, {dinnermsg}")

print("------------------Exercise 3-5---------------------------")
declinemsg = "cannot make it on Saturday"
print(f"{guests[0]} {declinemsg}.")
guests[0] = "Mom"
print(f"{guests[0]}, {dinnermsg}")
print(f"{guests[-1]}, {dinnermsg}")
print(f"{guests[-2]}, {dinnermsg}")

print("------------------Exercise 3-6---------------------------")
print("I found a larger dinner table!")
guests.insert(0, "Sir Sean Connery")
guests.insert(-2, "Lucy Ball")
guests.append ("Dad")
print("I am inviting", len(guests), "guests to dinner.")
print(f"{guests[0]}, {dinnermsg}")
print(f"{guests[-4]}, {dinnermsg}")
print(f"{guests[-3]}, {dinnermsg}")
print(f"{guests[-1]}, {dinnermsg}")
print(f"{guests[-2]}, {dinnermsg}")
print(f"{guests[-1]}, {dinnermsg}")


print("------------------Exercise 3-7---------------------------")
apology = "I am sorry, I cannot have you over for dinner. Maybe next week?"
print("I'm so sorry, my dinner table won't be available in time and I will only be able to invite 2 people for dinner!")
print(f"{guests[0]}, {apology}")
guests.pop(0)
print(f"{guests[-1]}, {apology}")
guests.pop(-1)
print(f"{guests[-3]}, {apology}")
guests.pop(-3)
print(f"{guests[0]}, {apology}")
guests.pop(0)
print(f"{guests[-2]}, {dinnermsg}")
print(f"{guests[-1]}, {dinnermsg}")
del guests[-2]
del guests[-1]
print("Here is my revised guest list: ", guests)

print("------------------Exercise 3-9---------------------------")
print("Added count to exercise 3-6")

