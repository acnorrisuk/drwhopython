import random, time


class Room(object):
    """ Rooms """
    def __init__(self,name,description,item):
            self.name = name
            self.description = description
            self.item = item


                
    # ++++ Room Map +++++
    #
    # ===================
    # 
    # | 1 - 2  - 3 |
    #  ---  |   ---
    # | 4 - 5  - 6 |
    #  --- ---   |
    # | 7 - 8  - 9 |
    #   
    # ===================

# room = Room(name,description,item))

    
room1 = Room("Cargo #32","There are crates piled from floor to ceiling.\
             \nYou hear the familiar buzz of your Sonic Screwdriver\
             \ncoming from a metallic box on the floor.", "Sonic Screwdriver")
room2 = Room("Corridor #12","You are in a dark grey corridor.\
             \nA sign on the wall says #12","n")
room3 = Room("Corridor #13","You are in a dark grey corridor.\
             \nA sign on the wall says #13","Tardis")
room4 = Room("???","You are in a room which resembles an art gallery.\
             \nThere is a stone tablet on the wall","Tablet")
room5 = Room("Corridor #22","You are in a dark grey corridor.\
             \nA sign on the wall says #22.\
             \nFrom here you can travel in any direction","n")
room6 = Room("Corridor #23","You are in a dark grey corridor.\
             \nA sign on the wall says #23 \
             \nA guard is blocking your path to the East","Guard")
room7 = Room("Jail","You see Clara unconscious on the floor of a cell.\
             \nIt looks like it has an electronic lock","Jail")
room8 = Room("Corridor #32","You are in a dark grey corridor.\
             \nA sign on the wall says #32\
             \nA door blocks your path to the west.","Door")
room9 = Room("Corridor #33","You are in a dark grey corridor.\
             \nA sign on the wall says #33","n")


# Room coordinates [n,e,s,w]
room1.coordinates = [0,room2,0,0]
room2.coordinates = [0,room3,room5,room1]
room3.coordinates = [0,0,0,room2]
room4.coordinates = [0,room5,0,room4]
room5.coordinates = [room2,room6,0,room4]
room6.coordinates = [0,0,room9,room5]
room7.coordinates = [0,room8,0,0]
room8.coordinates = [0,room9,0,room7]
room9.coordinates = [room6,0,0,room8]

# item class
class Items(object):
    def __init__(self, name):
        self.tardis = tardis

    def tardis(self):
        print("You see the Tardis")

# Character class
class Character(object):
    def __init__(self,name,location = room3):
        self.name = name
        self.location = location

    def look(self):
        place = self.location
        print (place.description)

    def examine(self):
        if self.location.item == "Tardis":
            Items.self.tardis            
        else:
            print ("There is nothing of interest here.")

    def inventory(self):
        inv = ["Psychic Paper"]
        for item in inv:
            print("You are carrying:\n",item)

currentchar = Character("The Doctor")



print ("Episode 6: The Sinking Ship.")
print ("You are currently The Doctor")



# help
def help_function():
    print ("\nGAME COMMANDS")
    print ("\n"'"n","e","s", and "w" to move your character.')
    print ('"exam" to examine the objects in the room')
    print ('"inv" to see your inventory')
    print ('"end" to quit the game. All progress will be lost.')
    print ('"help" to see this list again.')
        

# main game
help_function()
while True:
    command = input("\n>>>  ")
    command.lower
    if command == "look":
        currentchar.look()
    if command == "examine":
        currentchar.examine()
    if command == "inv":
        currentchar.inventory()
    if command == ("n" or "north"):
        if currentchar.location.coordinates[0] == 0:
            print ("You cannot go that way.")
        else:
            currentchar.location = currentchar.location.coordinates[0]
            currentchar.look()
    if command == ("e" or "east"):
        if currentchar.location.coordinates[1] == 0:
            print ("You cannot go that way.")
        else:
            currentchar.location = currentchar.location.coordinates[1]
            currentchar.look()
    if command == ("s" or "south"):
        if currentchar.location.coordinates[2] == 0:
            print ("You cannot go that way.")
        else:
            currentchar.location = currentchar.location.coordinates[2]
            currentchar.look()
    if command == ("w" or "west"):
        if currentchar.location.coordinates[3] == 0:
            print ("You cannot go that way.")
        else:
            currentchar.location = currentchar.location.coordinates[3]
            currentchar.look()
    if command == ("help"):
        help_function()            
    if command == "end":
        break


