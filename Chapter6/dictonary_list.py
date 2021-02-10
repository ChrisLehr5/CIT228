# print("------------------Chapter 6, Hands On #3---------------------------")
# consoles = { 
#     "Sony": ["Playstation", "Playstation 2", "Playstation 3", "Playstation 4", "Playstation 5", "Vietnam"],
#     "Sega": ["Genesis", "Game Gear", "Sega CD", " 32X", "Sega Saturn", "Dreamcast"],
#     "Nintendo": ["Super Nintendo", "Nintendo 64", "GameCube", "Wii", "Wii U", "Switch"],      
# }
# mascot = {
#     "Sony Mascot": ["Crash Bandicoot", "Kratos", "Nathan Drake", "Sackboy"],
#     "Sega Mascot" : ["Sonic", "Tails", "Knuckles"],
#     "Nintendo Mascot": ["Mario", "Luigi", "Peach", "Bowser", "Yoshi"],
# }
# games = {
#     "Playstation 4 Games": ["Uncharted", "Last of Us"],
#     "Sega Gensis Games": ["Rocket Knight", "Buster Busts Loose", "Acrobat"],
#     "Nintendo Switch Games" : ["Fire Emblem", "Beach Volleyball", "Disgaea Remastered"],
# }

# gaming = [consoles, mascot, games]
# for g in gaming:    
#     print(f"\n{g} :")

#I'm pretty sure I did this one wrong >.< 
# So I tried again below  

print("------------------Chapter 6, Hands On #3 2nd Attempt---------------------------")

systems= {
    "Sony":{ 
    "Console": "Playstation 5",
    "Mascots": ["Crash Bandicoot", "Kratos", "Nathan Drake", "Sackboy"],
    "Price": "499.99",      
    "Best Games": ["Crash Bandicoot", "Kratos", "Nathan Drake", "Sackboy"],
},
    "Sega": {
    "Console": "Sega Genesis",
    "Mascots" : ["Sonic", "Tails", "Knuckles"],
    "Price": "299.99",
    "Best Games": ["Rocket Knight", "Buster Busts Loose", "Acrobat"],
},
    "Nintendo" : {
    "Console": "Nintendo Switch",
    "Mascots": ["Rocket Knight", "Buster Busts Loose", "Acrobat"],
    "Price" : "299.99",
    "Best Games" : ["Fire Emblem", "Beach Volleyball", "Disgaea Remastered"],
},
}

for system, info in systems.items():
    print(f"\n\tSystem: {system}")
    console = info['Console']
    mascot = info['Mascots']
    price = info['Price']

    print(f"Console: {console}")
    print(f"Mascots: {mascot}")
    print(f"Price: ${price}")
