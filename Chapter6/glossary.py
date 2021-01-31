print("------------------Chapter 6, Exercise 6-3---------------------------")
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

print("------------------Chapter 6, Exercise 6-4---------------------------")
print ("\t\t\tDictionary")
for key, value in glossary.items():
    print(f"\n{key} :")
    print(f"\t{value}")