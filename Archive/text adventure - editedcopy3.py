import random, time

game = 0

# Rooms

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
             \ncoming from a metallic box on the floor.", ["Sonic Screwdriver"])
room2 = Room("Corridor #12","You are in a metallic grey corridor.\
             \nA sign on the wall says #12","none")
room3 = Room("Corridor #13","You are in a metallic grey corridor.\
             \nA sign on the wall says #13","Tardis")
room4 = Room("???","You are in a room which resembles an art gallery.\
             \nThere is a stone tablet on the wall","Tablet")
room5 = Room("Corridor #22","You are in a metallic grey corridor.\
             \nA sign on the wall says #22.\
             \nFrom here you can travel in any direction","none")
room6 = Room("Corridor #23","You are in a metallic grey corridor.\
             \nA sign on the wall says #23",["Guard"])
room7 = Room("Jail","You see Clara unconscious on the floor of a cell.\
             \nIt looks like it has an electronic lock","Jail")
room8 = Room("Corridor #32","You are in a metallic grey corridor.\
             \nA sign on the wall says #32\
             \nA door blocks your path to the west.","Door")
room9 = Room("Corridor #33","You are in a metallic grey corridor.\
             \nA sign on the wall says #33","none")


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

# Items and Barriers


class Items(object):
    def __init__(self, name):
        self.name = name
    def use_sonic_screwdriver(self):
        print("You see the Sonic Screwdriver and pick it up")
        doctor.inv.append("Sonic Screwdriver")
        self.location.item.remove("Sonic Screwdriver")
        print("Sonic Screwdriver has been added to your inventory")
    def use_tardis(self):
        print("You see the Tardis")
        if game == 1:
            print("WHIIIIIRRRRRRR WHIIIIIIIIRRRRRR \
                  \nThe Doctor and Clara fly off for another adventure")
        end_game()
    def use_tablet(self):
        print("You see a tablet")
    def use_guard(self):
        print("A guard is blocking your path to the South")
        print("GUARD: Only those with clearance shall pass")
        if command == "s" or "south":
            doctor.location.coordinates[2] = 0    # why not == ?
        elif command == "use psychic paper":   # ignoring
            print("check code")
            self.location.item.remove("Guard")
            doctor.location.coordinates[2]
            print("GUARD: Erm sorry Ambassador. Go right on through")
            
        
    def use_jail(self):
        print("You see a jail with Clara inside")
    def use_door(self):
        print("You see a locked door")



# Character

class Character(object):
    def __init__(self,name,location,inv):
        self.name = name
        self.location = location
        self.inv = inv
        
    def look(self):
        print(self.location.description)
        if self.location.item == "Guard": 
                Items.use_guard(self)
        else:
            pass
            

    def examine(self):
        if self.location.item == ["Sonic Screwdriver"]:
            Items.use_sonic_screwdriver(self)
        elif self.location.item == "Tardis":
            Items.use_tardis(self)
        elif self.location.item == "Tablet":
            Items.use_tablet(self)
        elif self.location.item == "Guard":
            Items.use_guard(self)
        elif self.location.item == "Jail":
            Items.use_jail(self)
        elif self.location.item == "Door":
            Items.use_door(self) 
        elif self.location.item == "none":
            print ("There is nothing of interest here.")
        else:
            print("There is nothing of interest here.")
            
    def inventory(self):
        for item in doctor.inv:
            print("You are carrying:\n",item)

doctor = Character("The Doctor", room3,["Psychic Paper"])

print ("Episode 6: The Sinking Ship.")
print ("You are currently The Doctor")
print ("Rescue Clara and get back into the Tardis")


# Help

def help_function():
    print ("\nGAME COMMANDS")
    print ("\n"'"n","e","s", and "w" to move your character.')
    print ('"exam" to examine the objects in the room')
    print ('"inv" to see your inventory')
    print ('"use <item> to use an item')
    print ('"end" to quit the game. All progress will be lost.')
    print ('"help" to see this list again.')
        

# Main Game Loop

help_function()
while True:
    command = input("\n>>>  ")
    command.lower
    if command == "look":
        doctor.look()
    if command == "exam":
        doctor.examine()
    if command == "inv":
        doctor.inventory()
    if command == ("n" or "north"):
        if doctor.location.coordinates[0] == 0:
            print ("You cannot go that way.")
        else:
            doctor.location = doctor.location.coordinates[0]
            doctor.look()
    if command == ("e" or "east"):
        if doctor.location.coordinates[1] == 0:
            print ("You cannot go that way.")
        else:
            doctor.location = doctor.location.coordinates[1]
            doctor.look()
    if command == ("s" or "south"):
        if doctor.location.coordinates[2] == 0:
            print ("You cannot go that way.")
        else:
            doctor.location = doctor.location.coordinates[2]
            doctor.look()
    if command == ("w" or "west"):
        if doctor.location.coordinates[3] == 0:
            print ("You cannot go that way.")
        else:
            doctor.location = doctor.location.coordinates[3]
            doctor.look()
    if command == ("help"):
        help_function()            
    if command == "end":
        break

# End Game

def end_game():
    input("Thanks for playing. Press enter to exit")


