# exercise 1- use your own first and last name 
print("---------------------------------------------")
print("Exercise 1")
name= "christine largent"
print("---------------------------------------------")
print(name.title())
print(name.upper())
print(name.lower())
print("My first initial is: ", name[0].upper())

# exercise 2- make up your own noun, adjective, verb and ending
# use concatentation to create sentence1
# use an f-string to create sentence 2 
print("---------------------------------------------")
print("Exercise 2")
noun = "cat"
adj = "zippy"
verb = "pounced"
ending = "from the couch"
sentence1 = "the " + adj + " fluffy " + noun + " " + verb + " " + ending
senetnce2 = f"the {adj} fluffy {noun} {verb} {ending}"
print("---------------------------------------------")
print(sentence1.upper())
print(senetnce2.lower())

# exercise 3- Dune Quote  
print("---------------------------------------------")
print("Exercise 3")
noun = "I"
verb = "must"
adv = "not"
verb2 = "fear"
verb3 = "is"
article = "the"
adj = "that"
tverb = "obliteration"
ending = "will permit it to pass over and through me"
sentence1 = f"{noun} {verb} {adv} {verb2}. {verb2} {verb3} {article} mind-killer.\n{verb2} {verb3} {article} little-death {adj} brings total {tverb}.\n{noun} will face my {verb2}.\n{noun} {ending}." 
print("---------------------------------------------")
print(sentence1.lower())

# exercise 4- Two column printout using \t and \n  
print("---------------------------------------------")
print("Exercise 4")
color1 ="Blue"
color2 ="Yellow"
color3 ="Red"
house1 ="Blue Lions"
house2 ="Golden Hind"
house3 ="Imperial Eagles"
sentence1 ="Colors\t\t\tHouses\n"+color1+"\t\t\t"+house1+"\n"+color2+"\t\t\t"+house2+"\n"+color3+"\t\t\t"+house3
print("---------------------------------------------")
print(sentence1)
