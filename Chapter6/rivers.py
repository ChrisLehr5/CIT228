print("------------------Chapter 6, Exercise 6-5---------------------------")
rivers = { 
    "Mekong": ["China", "Myanmar","Thailand", "Loas", "Cambodia", "Vietnam"],
    "Rio Grande": ["United States", "Mexico"],
    "Congo": "Africa",      
}
print("---------------------Rivers & Countries-----------------------------")
for key, value in rivers.items():
    print(f"The {key.title()} flows through {value}")
print("---------------------------Rivers-----------------------------------")
for key in rivers.keys():
    print(key.title())
print("---------------------------Countries-----------------------------------")
for value in rivers.values():
    print(value)