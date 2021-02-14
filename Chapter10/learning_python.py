print("------------------------------Hands On #1, Exercise 10-1 & 10-2-----------------------------------------")
#directory cannot be found unless full absolute path, even though in same folder 
filename = 'C:/Users/Khyr/Desktop/CIT228/Chapter10/learning_python.txt'

print("Output from reading entire file")
with open (filename) as f:
    contents = f.read()
print(contents)

print("-----------------------------------------")
print("\nOutput from looping over the file object")
with open(filename) as f: 
    for line in f:
        print(line.rstrip())

print("-----------------------------------------")
print("\nOutput from storing lines in a list")
with open(filename) as f:   
    contents = f.readlines()
#prints original list
print("\nOriginal List = ", contents)
#processes each line item in list 
for line in contents:
    print(line.rstrip())
print("-----------------------------------------")
print("Replace can with cannot")
with open(filename) as f:
    for line in f:
        print("Orginal: ", line)
        print("Modified: ", line.replace("can","cannot"))