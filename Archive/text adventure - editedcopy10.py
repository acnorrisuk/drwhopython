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

cargo = Room("Cargo","You are in a large room.\
             \nThere are crates piled from floor to ceiling.", ["Sonic Screwdriver"])
corr1 = Room("Corridor #1","You are in a metallic grey corridor.","none")
engine = Room("Engine room","You are in an engine room.\
             \nIt is eerily quiet","Tardis")
office = Room("Capt. Office","You are in a small room with a desk.\
             \nThere is a bookshelf in the corner",["Book"])
corr2 = Room("Corridor #2","Two corridors join together.\
             \nFrom here you can travel any direction but South","none")
security = Room("Security","You are in a security room.",["Guard"])
corr3 = Room("Corridor #3", "You are in a metallic grey corridor.","Door East")
corr4 = Room("Corridor #4","You are in a metallic grey corridor.","Door West")
control = Room("Control room","You are in a room marked 'Controls'",["Map"])
passenger = Room ("Passenger room","A sign above reads: 'PASSENGERS'\
            \nYou see rows and rows of stasis pods.\
            \nInside each one is a different species.\
            \nSycorax, Krillitanes, Ood, Weevils, Tritovores...\
            \nAll unconscious and being monitored",["Pods"])
captQ = Room ("Capt.Quarters","You are in the Captain's Quarters.",["Calendar"])

# Room coordinates [n,e,s,w]

cargo.coordinates = [0,corr1,0,0]
corr1.coordinates = [0,engine,corr2,cargo]
engine.coordinates = [0,0,0,corr1]
office.coordinates = [0,corr2,0,office]
corr2.coordinates = [corr1,security,0,office]
security.coordinates = [0,0,control,corr2]
corr3.coordinates = [0,corr4,captQ,passenger]
corr4.coordinates = [0,control,0,corr3]
control.coordinates = [security,0,0,corr4]
passenger.coordinates = [0, corr3, 0, 0]
captQ.coordinates = [corr3, 0, 0, 0]


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
        doctor.location.coordinates = [0, 0, 0, corr2]  
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
            doctor.location = corr3
            doctor.room_descrip()
        else:
            doctor.location = corr4
            doctor.location.coordinates = [0, control, 0, 0]
            print("ACCESS DENIED")
    def door_block_east(self):
        passcode = "2804" or "2 8 0 4"
        print("A door blocks your path")
        passcode_correct = input("ENTER PASSCODE: ")
        if passcode_correct == passcode:
            print("\nACCESS GRANTED")
            print("You go through the door\n")
            doctor.location = corr4
            doctor.room_descrip()
        else:
            doctor.location = corr3
            doctor.location.coordinates = [0, 0, captQ, passenger]
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

doctor = Character("The Doctor", engine,["Tardis Key", "Psychic Paper"])

print ("PASSENGERS.\n")
print ("You are the Doctor")
print ("Clara has been taken.")
print ("She was carrying your Sonic Screwdriver")
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
            if doctor.location == security and doctor.location.item == ["Guard"]:
                doctor.location.item.remove("Guard")
                print("GUARD: Level 5 Clearance granted. You may pass.")
                doctor.location.coordinates = [0, 0, control, corr2] 
            else:
                print("It had no effect")
        else:
            pass

    if command == "use sonic screwdriver":
        if "Sonic Screwdriver" in doctor.inv:
            if doctor.location == passenger and doctor.location.item == ["Pods"]:
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
        if doctor.location == engine:
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
        if doctor.location == corr3:
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
        if doctor.location == corr4:
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
    #                               1. cargo
    # ===================           2. corr1
    #       --------------          3. engine
    #       | 1   2    3 |          4. office
    #       |---|    |---|          5. corr2   
    #       | 4   5    6 |          6. security
    #   |------------|   |          7. passenger
    #   | 7   8   9   10 |          8. corr3
    #   -----    ---------          9. corr4
    #       | 11 |                  10. control 
    #       -----                   11. captQ
    # ===================
