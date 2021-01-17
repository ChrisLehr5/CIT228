print("------------------Chapter 4, Exercise 4-8---------------------------")
cubes = [] 
for value in range(1,11): 
    cube = value **3
    cubes.append(cube)
print(cubes)
print("------------------Chapter 4, Exercise 4-9---------------------------")
cubes = [value **3 for value in range (1,11)] 
print(cubes)