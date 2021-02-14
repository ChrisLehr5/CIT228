print("-----------------------------Chapter 10, Hands On #4------------------------------------")
glossary = {
    "Dictionary": "Python data type that stores key:value pairs",
    "String": "A series of characters",
    "Comment": "The comment allows you to write notes within your programs",
    "List": "A collection of items in a particular order",
    "Slice": "Working with specific groups of items within a list",
    "Float": "Number with a decimal",
    "Loop": "Working through collections, one item at a time",
    "Boolean": "A true or false value",
    "Line Length": "Recommended line length in Python is 80 characters",
    "Style Guide" : "The guide that Python programmers refer to when styling code, called Python Enchancement Proposal (PEP)",
}

print("Dictionary:")
print("\t",glossary["Dictionary"])
print("String:")
print("\t",glossary["String"])
print("Comment:")
print("\t",glossary["Comment"])
print("List:")
print("\t",glossary["List"])
print("Slice:")
print("\t",glossary["Slice"])

#print("------------------Chapter 6, Exercise 6-4---------------------------")
print ("\t\t\tDictionary")
for key, value in glossary.items():
    print(f"\n{key} :")
    print(f"\t{value}")

print("--------------------------------------------------------------------------------------------")
import json

def menu():
    selection = int(input("1-create file, 2-read file, 3-add to file, 4-quit  "))
    while selection!=1 and selection!=2 and selection!=3 and selection!=4:
        print("You made an invalid selection, please try again")
        selection = int(input("1-create file, 2-read file, 3-add to file, 4-quit  "))
    return selection

def create(object):
    overwrite = input("You are about to create a new file, existing data will be overwritten (q to quit, any key to continue) ")
    if overwrite !="q":
        with open("C:/Users/Khyr/Desktop/CIT228/Chapter10/glossary.json", "w") as write_file:
            json.dump(object, write_file, indent=4, sort_keys=True)
            print("glossary.json has been created")

def append(new_item):
    with open("C:/Users/Khyr/Desktop/CIT228/Chapter10/glossary.json", "r+") as add_file:
        glossaryDictionary = json.load(add_file)
        glossaryDictionary.update(new_item)
        add_file.seek(0)
        json.dump(glossaryDictionary, add_file, indent=4, sort_keys=True)
        print("Data has been added to glossary.json")

def read():
    try:
        with open("C:/Users/Khyr/Desktop/CIT228/Chapter10/glossary.json") as read_file:
            glossaryDictionary = json.load(read_file)
    except FileNotFoundError:
        print("The file doesn't exist or cannot be found.")
        print("Please make a different menu selection")      
    else: 
        for key, value in glossaryDictionary.items():
            print(key.title(), "  your favorite term is ", value)       
        
def get_key():
    name=input("Enter your first name ")
    firstname=name.split()[0]
    firstname=firstname.lower()
    return firstname

def get_value():
    fav_term=input("Enter your favorite term  ")
    return fav_term

# starting values for dictionary
favTerms = {
    "lisa": "Loop",
    "dan": "Float",
    "danielle": "Loop",
    "dylan": "Float",
    "leighton": "Loop",
}
choice=menu()
while choice != 4:
    if choice == 1:
        create(favTerms)
    elif choice == 2:
        read()
    elif choice == 3:
        user=get_key()
        num=get_value()
        new_dictionary_entry={user:num}
        append(new_dictionary_entry)
    else:
        print("The option you selected is not available, please try again")        
    choice=menu()