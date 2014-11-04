import random
    # Monster class
class Monster(object):
    """Monster"""
    def __init__(self,name,level):
        self.name = name
        self.level = level
        
    # Monsters
Green_Blob = Monster("Green Blob","1")
Red_Blob = Monster("Red Blob","2")
Blue_Blob = Monster("Blue Blob","3")
Yellow_Blob = Monster("Yellow Blob","4")
Black_Blob = Monster("Black Blob","5")

def make_monster():
    # 2 = monster in room; else, no monster
    monster_in = random.randrange(3)
    if monster_in == (0 or 1):
        return 0
    monster = random.randrange(5)
    if monster == 0:
        monster = Green_Blob
    elif monster == 1:
        monster = Red_Blob
    elif monster == 2:
        monster = Blue_Blob
    elif monster == 3:
        monster = Yellow_Blob
    elif monster == 4:
        monster = Black_Blob
    return monster

    # Room class
class Room(object):
    """ Room """
    def __init__(self,name,description,monster_y_n):
            self.name = name
            self.description = description
            self.monster_y_n = monster_y_n
            if self.monster_y_n == "y":
                monster = make_monster()
                self.monster = monster
    # Rooms
    # last input is coordinates (n,e,s,w)
    #
    # ++++ Room Map +++++
    #
    # ===================
    # | |
    # | |
    # | 1 |
    # | |
    # | 3 2 |
    # | |
    # | |
    # | |
    # | |
    # ===================
    #
    # Template:
    # room# = Room(name,description,monster in it? (y/n))
    # Then add the coordinates below the room creators
    
room1 = Room("Bedroom","You are you in your own bedroom.\nTo the south, there is a garden past the back door.", "n")
room2 = Room("Garden","You are in a garden with many flowers and a narrow stone path. \nTo the north, you see the backdoor of your house that enters your bedroom.\nA pathway leads west.","y")
room3 = Room("Pathway","You are in a narrow stone path with hedges on both sides of you.\nTo the east, there is a garden.","y")
    # Room coordinates (had to create all the rooms to assign them to coordinates)
room1.coordinates = [0,0,room2,0]
room2.coordinates = [room1,0,0,room3]
room3.coordinates = [0,room2,0,0]
    #room4 = Room("Classroom","You are in a classroom with a 5 rows of desks that face a whiteboard.")

# Character class
class Character(object):
    def __init__(self,name,gender,hair,age,location = room1):
        self.name = name
        self.gender = gender
        self.hair = hair
        self.age = age
        self.location = location
        self.inv = []
    def look(self):
        place = self.location
        print (place.description)
        if place.monster_y_n == "y":
            if place.monster != 0:
                room_monster = place.monster
                print ("There is a",room_monster.name,"in the room.\n")
        else:
            print ("")
    #if item == True:
        #print item.description
    #class item(object):
        #def __init__(self,description):
            #self.description = description
            
characters = []
Zyrkan = Character("Zyrkan","m","black",20)
characters.append(Zyrkan)
currentchar = Zyrkan
print ("Welcome to Mouche's first text based game.")
print ('Type "commands" to see the command list')
print ("You are currently:",currentchar.name)
    # Menu
    # "commands" shows the commands available
    # "look" looks around in the current room
    #
while True:
    command = input("")
    if command == "commands":
        print ('"n","e","s", and "w" make your character go north, east, south, and west respectively')
        print ('"end" to break')
        print ('"look" to look around the room')
        print ('"players" to see the player list')
    if command == "look":
        currentchar.look()
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
    if command == "end":
        break
    if command == "players":
        print ("You are",currentchar)
        i = 1
        print ("Players:")
        for player in characters:
            print (player.name,"(" + str(i) + ")")
