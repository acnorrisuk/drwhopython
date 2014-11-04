import time

# Rooms
# room = Room(name,description,item))

def room_map_blank():
    print(
                """
               --------------
               |            |
               |---|    |---|
               |            |
           |------------|   |
           |       :        |
           -----    ---------
               |   |
               -----
            """ )

class Room(object):
    """ Rooms """
    def __init__(self,name,description,item):
            self.name = name
            self.description = description
            self.item = item

room1 = Room("Cargo","You are in a large room.\
             \nThere are crates piled from floor to ceiling.", ["Sonic Screwdriver"])
room2 = Room("Corridor #1","You are in a metallic grey corridor.\,"none")
room3 = Room("Engine room","You are in an engine room.\
             \nIt is eerily quiet","Tardis")
room4 = Room("Capt. Office","You are in a small room with a desk.\
             \nThere is a bookshelf in the corner",["Book"])
room5 = Room("Corridor #2","Two corridors join together.\
             \nFrom here you can travel any direction but South","none")
room6 = Room("Security","You are in a security room.",["Guard"])
room7 = Room("Corridor #3", "You are in a metallic grey corridor.","Door East")
room8 = Room("Corridor #4","You are in a metallic grey corridor.","Door West")
room9 = Room("Control room","You are in a room marked 'Controls'",["Map"])
roomC = Room ("Passenger room","A sign above reads: 'PASSENGERS'\
            \nYou see rows and rows of stasis pods.\
            \nInside each one is a different species.\
            \nSycorax, Krillitanes, Ood, Weevils, Tritovores...\
            \nAll unconscious and being monitored",["Pods"])
roomQ = Room ("Capt.Quarters","You are in the Captain's Quarters.",["Calendar"])

# Room coordinates [n,e,s,w]

room1.coordinates = [0,room2,0,0]
room2.coordinates = [0,room3,room5,room1]
room3.coordinates = [0,0,0,room2]
room4.coordinates = [0,room5,0,room4]
room5.coordinates = [room2,room6,0,room4]
room6.coordinates = [0,0,room9,room5]
room7.coordinates = [0,room8,roomQ,roomC]
room8.coordinates = [0,room9,0,room7]
room9.coordinates = [room6,0,0,room8]
roomC.coordinates = [0, room7, 0, 0]
roomQ.coordinates = [room7, 0, 0, 0]


# Items and Barriers

class Items(object):
    def __init__(self, name):
        self.name = name
    def get_sonic_screwdriver(self):
        print("\nYou hear the familiar buzz of your Sonic Screwdriver\
              \ncoming from a metallic box on the floor. You pick it up.")
        doctor.inv.append("Sonic Screwdriver")
        self.location.item.remove("Sonic Screwdriver")
        print("Sonic Screwdriver has been added to your inventory")
    def see_tardis(self):
        print("You see the Tardis")
    def read_book(self):
        print("One book catches your attention.")
        print("CODES AND CIPHERS")
        print("You pick it up off the shelf and read: ")
        print("...When creating a code, often people choose the date\
              \nof an important event so they can remember it...")
    def read_calendar(self):
        print("You see a calendar on the wall")
        print("The 28th April is circled in red")
        print("Underneath it reads 'Anniversary'")
    def room_map(self):
        print("You see a map on the wall in front of you.")
        room_map_blank()
        print("You memorize the map.")
        doctor.inv.append("Map")
        self.location.item.remove("Map")
        print("Map has been added to your inventory.")
    def guard_block(self):
        print("A guard is blocking your path to the South")
        print("GUARD: Only those with clearance shall pass")
        doctor.location.coordinates = [0, 0, 0, room5]  
    def pods_block(self):
        print("You see Clara suspended in a stasis pod")
        print("She is also unconscious but her vital signs are stable") 
    def door_block_west(self):
        passcode = "2804" or "2 8 0 4"
        print("A door blocks your path")
        passcode_correct = input("ENTER PASSCODE: ")
        if passcode_correct == passcode:
            print("\nACCESS GRANTED")
            print("You go through the door\n")
            doctor.location = room7
            doctor.room_descrip()
        else:
            doctor.location = room8
            doctor.location.coordinates = [0, room9, 0, 0]
            print("ACCESS DENIED")
    def door_block_east(self):
        passcode = "2804" or "2 8 0 4"
        print("A door blocks your path")
        passcode_correct = input("ENTER PASSCODE: ")
        if passcode_correct == passcode:
            print("\nACCESS GRANTED")
            print("You go through the door\n")
            doctor.location = room8
            doctor.room_descrip()
        else:
            doctor.location = room7
            doctor.location.coordinates = [0, 0, roomQ, roomC]
            print("ACCESS DENIED")
        

# Character

class Character(object):
    def __init__(self,name,location,inv):
        self.name = name
        self.location = location
        self.inv = inv
        
    def room_descrip(self):
        print(self.location.description)
        if self.location.item == ["Guard"]:
            Items.guard_block(object)
        else:
            pass
        
    def look(self):
        if self.location.item == ["Sonic Screwdriver"]:
            Items.get_sonic_screwdriver(self)
        elif self.location.item == "Tardis":
            Items.see_tardis(self)
        elif self.location.item == ["Book"]:
            Items.read_book(self)
        elif self.location.item == ["Pods"]:
            Items.pods_block(self)
        elif self.location.item == ["Map"]:
            Items.room_map(self)
        elif self.location.item == ["Calendar"]:
            Items.read_calendar(self)
        elif self.location.item == "Door West":
            print("There is a door blocking your path to the west")
        elif self.location.item == "Door East":
            print("There is a door blocking your path to the east")
        elif self.location.item == "none":
            print ("There is nothing of interest here.")
        else:
            print("There is nothing of interest here.")
            
    def inventory(self):
        print("You are carrying: ")
        for item in doctor.inv:
            print(item)

doctor = Character("The Doctor", room3,["Tardis Key", "Psychic Paper"])

print ("THE SINKING SHIP.\n")
print ("You are the Doctor")
print ("Clara has been taken.")
print ("Luckily she was carrying your Sonic Screwdriver")
print ("You have locked on to the signal and have landed nearby.")
print ("It is up to you to rescue Clara and escape in the Tardis")

# Help

def help_function():
    print ("\nGAME COMMANDS")
    print ("\n"'"n","e","s", and "w" to move your character.')
    print ('"look" to look around the room')
    print ('"inv" to see your inventory')
    print ('"use <item>" to use an item')
    print ('"end" to quit the game. All progress will be lost.')
    print ('"help" to see this list again.')
        

# Main Game Loop

help_function()
input("\nPress enter to begin.\n")
doctor.room_descrip()

while True:
    command = input("\n>>>  ")
    command = command.lower()
    
    if command == "look":
        doctor.look()
    if command == "inv":
        doctor.inventory()
    if command == "use psychic paper":
        if "Psychic Paper" in doctor.inv: 
            if doctor.location == room6 and doctor.location.item == ["Guard"]:
                doctor.location.item.remove("Guard")
                print("GUARD: Level 5 Clearance granted. You may pass.")
                doctor.location.coordinates = [0, 0, room9, room5] 
            else:
                print("It had no effect")
        else:
            pass

    if command == "use sonic screwdriver":
        if "Sonic Screwdriver" in doctor.inv:
            if doctor.location == roomC and doctor.location.item == ["Pods"]:
                doctor.location.item.remove("Pods")
                print("A buzzer sounds and the stasis doors open")
                print("The other 'passengers' begin to regain consciousness\
                      \nYou help Clara up and out of her pod")
                doctor.inv.append("Clara")
            else:
                print("It had no effect")
        else:
            print("You do not have your Sonic Screwdriver")

    if command == "use tardis key":
        if doctor.location == room3:
            if "Clara" in doctor.inv:
                print("WHIIIIIRRRRRRR...")
                print("WHIIIIIIIIRRRRRR...")
                print("The Tardis fades away.")
                print("The Doctor and Clara escape")
                print("I hope you have enjoyed the adventure.\
                      \nThanks for playing")
                break
            else:
                print("You can't leave without Clara")
        else:
            print("The Tardis is not in this room") 

    if command == ("n" or "north"):
        if doctor.location.coordinates[0] == 0:
            print ("You cannot go that way.")
        else:
            doctor.location = doctor.location.coordinates[0]
            doctor.room_descrip()
    if command == ("e" or "east"):
        if doctor.location == room7:
            Items.door_block_east(object)
        elif doctor.location.coordinates[1] == 0:
            print ("You cannot go that way.")
        else:
            doctor.location = doctor.location.coordinates[1]
            doctor.room_descrip()
    if command == ("s" or "south"):
        if doctor.location.coordinates[2] == 0:
            print ("You cannot go that way.")
        else:
            doctor.location = doctor.location.coordinates[2]
            doctor.room_descrip()
    if command == ("w" or "west"):
        if doctor.location == room8:
            Items.door_block_west(object)
        elif doctor.location.coordinates[3] == 0:
            print ("You cannot go that way.")
        else:
            doctor.location = doctor.location.coordinates[3]
            doctor.room_descrip()
            
    if command == ("help"):
        help_function()
    if command == ("use map"):
        if "Map" in doctor.inv:
            room_map_blank()
        else:
            print("You do not have a map")
    if command == "end":
        break


# end

    # ++++ Room Map +++++
    #
    # ===================
    #       --------------
    #       | 1   2    3 |
    #       |---|    |---|
    #       | 4   5    6 |
    #   |------------|   |
    #   | C   7   8    9 |
    #   -----    ---------
    #       | Q |
    #       -----
    # ===================
