print("------------------Exercise 3-10---------------------------")
print("--------List of Stardew Valley Ocean Fish-----------------")

fishes = ["Anchovy", "Flounder", "Halibut", "Albacore", "Herring", "Red Snapper", "Pufferfish", "Tilapia", "Tuna"]  
print("Original List: ", fishes)

fishes.insert(-1, "Sardine")
fishes.insert(-1, "Red Snapper")
fishes.insert(-1, "Sea Cucumber")
fishes.insert(0, "Super Cucumber")
print("List after additions: ", fishes)

del fishes[-1]
del fishes[-2]
del fishes[-3]
print("List after deletions: ", fishes)

print("List with Temp Sorting: ", sorted(fishes))

fishes.reverse()
print("List sorted in reverse: ", fishes)

print("List sorted in alphabetical order: ", sorted(fishes))

print("There are", len(fishes), "in the final list.")