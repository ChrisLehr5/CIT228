
print("------------------Chapter 4, Exercise 4-13---------------------------")
buffet = ("eggs", "fruit", "waffles", "hashbrowns", "bacon")
print("<<<<<<<<<<<<<< Buffet Menu >>>>>>>>>>>>>>>>>>")
for food in buffet:
    print(food)
#buffet[0] = "sausage"

print("<<<<<<<<<<<<<< New Buffet Menu >>>>>>>>>>>>>>>>>>")
buffet = ("eggs", "sausage", "waffles", "pears", "bacon")
for food in buffet:
    print(food)