print("------------------Chapter 6, Hands On #3 Nested List---------------------------")
rivers = { 
    "Mekong": ["China", "Myanmar","Thailand", "Loas", "Cambodia", "Vietnam"],
    "Congo": "Africa",    
    "Rio Grande": ["United States", "Mexico"]      
}
print("---------------------Rivers & Countries-----------------------------")
for key, value in rivers.items():
    if type(value)==list:
        print(f"The {key.title()} river flows through: ")
        for v in value:
            print("\t\t\t\t",v)
    else:
        print(f"The {key.title()} river flows through {value.title()}")
print("---------------------Rivers & Countries-----------------------------")

print("---------------------------Rivers-----------------------------------")
for key in rivers.keys():
    print(key.title())
print("---------------------------Countries-----------------------------------")
for value in rivers.values():
    if type(value)==list:
        for v in value:
            print(v)
        else:
            print(value)