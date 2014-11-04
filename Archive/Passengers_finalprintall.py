import time

# Rooms

teleport_species = 0
return_ship = 0

class Room(object):
    """ Rooms """
    def __init__(self,name,item):
            self.name = name
            self.item = item

def room_map_blank():
    print(
                """
               --------------
               |            |   
               |---|    |---|    : Security Door
               |            |
           |------------|   |
           |       :        |
           -----    ---------
               |   |
               -----
            """ )

def ship_knowledge():
    print(
     """
    Ship: PROCYON #59.
    Captain: Oghathi.
    Mission: Collect and catalogue all known intelligent species.
    Year began: 5804.
    Completion: 38%.
    """)

# Room (name, item)
cargo = Room("Cargo Hold",["Sonic Screwdriver"])
corr1 = Room("Corridor #1","none")
engine = Room("Engine Room","Tardis")
console = Room("Console Room",["Console"])
corr2 = Room("Corridor #2",["Map"])
security = Room("Security",["Guard"])
corr3 = Room("Corridor #3","Door East")
corr4 = Room("Corridor #4","Door West")
control = Room("Control Room",["Control Panel"])
passenger = Room ("Passenger Room",["Pods"])
teleport = Room ("Teleportation Room",["Teleporters"])

# Room coordinates [n,e,s,w]

cargo.coordinates = [0,corr1,0,0]
corr1.coordinates = [0,engine,corr2,cargo]
engine.coordinates = [0,0,0,corr1]
console.coordinates = [0,corr2,0,0]
corr2.coordinates = [corr1,security,0,console]
security.coordinates = [0,0,control,corr2]
corr3.coordinates = [0,corr4,teleport,passenger]
corr4.coordinates = [0,control,0,corr3]
control.coordinates = [security,0,0,corr4]
passenger.coordinates = [0, corr3, 0, 0]
teleport.coordinates = [corr3, 0, 0, 0]


# Items and Barriers

class Items(object):
    def __init__(self, name):
        self.name = name
    def get_sonic_screwdriver(self):
        print("You hear the familiar buzz of your Sonic Screwdriver.")
        input("You open up a nearby wooden box and pick it up.")
        doctor.inv.append("Sonic Screwdriver")
        self.location.item.remove("Sonic Screwdriver")
        input("Sonic Screwdriver has been added to your inventory.")
    def see_tardis(self):
        print("You can barely see the Tardis hidden amongst the engines.")
    def use_console(self):
        print("You log on to a console.")
        time.sleep(1.5)
        print("...")
        print("PROCYON #59.")
        time.sleep(1.5)
        print("CAPTAIN: Oghathi.")
        time.sleep(1.5)
        print("PROCYON MISSION:")
        time.sleep(1.5)        
        print("Collect and catalogue all known intelligent species.")
        time.sleep(1.5)
        print("YEAR OF COMMENCEMENT: 5804.")
        time.sleep(1.5)
        print("COMPLETE: 38%.")
        time.sleep(1.5)
        input("...")
        time.sleep(1.5)
        print("You log off the console.")
        if "Knowledge" not in doctor.inv:
            doctor.inv.append("Knowledge")
            input("Knowledge has been added to your inventory.")
        else:
            pass
    def use_teleporters(self):
        global teleport_species
        if "Clara" in doctor.inv and teleport_species == 0:
            teleport_species = 1
            print("Hundreds of species crowd onto the teleportation grid.")
            print("You key in the controls and set it to the nearest planet.")
            print("...")
            time.sleep(2)
            print("The teleportation is successful.")
            print("CLARA: 'Let's get back to the Tardis'")
            print("DOCTOR: 'We need to head to Main Control first'")
        else:
            print("Nobody to teleport.")
    def use_control_panel(self):
        global return_ship
        if "Clara" in doctor.inv and teleport_species == 1 and return_ship == 0:
            return_ship = 1
            print("You boot up the main controls.")
            print("You set the ship to return to its origin")
            input("COUNTDOWN: 3 minutes")
            print("You send a message to the rest of the fleet: ")
            print("The Doctor is watching...")
            print("DOCTOR: Let's get back to the Tardis")
        else:
            print("You have no reason to use the Main Control console.")
            
    def room_map(self):
        input("You see a map on the wall in front of you.")
        room_map_blank()
        input("You memorize the map.")
        doctor.inv.append("Map")
        self.location.item.remove("Map")
        input("Map has been added to your inventory.")
    def guard_block(self):
        print("A guard is blocking your path to the South")
        input("GUARD: Only those with clearance shall pass")
        doctor.location.coordinates = [0, 0, 0, corr2]  
    def pods_block(self):
        print("You see Clara suspended in a Stasis Pod")
        print("She is unconscious but her vital signs are stable") 
    def door_block_west(self):
        passcode = "5804" or "5 8 0 4"
        print("A door blocks your path.")
        passcode_correct = input("ENTER 4 DIGIT PASSCODE: ")
        time.sleep(1)
        print("...")
        time.sleep(2)
        if passcode_correct == passcode:
            input("ACCESS GRANTED ")
            print("You go through the door.")
            doctor.location = corr3
            doctor.room_descrip()
        else:
            doctor.location = corr4
            doctor.location.coordinates = [0, control, 0, 0]
            print("ACCESS DENIED ")
    def door_block_east(self):
        passcode = "5804" or "5 8 0 4"
        print("A door blocks your path")
        passcode_correct = input("ENTER 4 DIGIT PASSCODE: ")
        time.sleep(1)
        time.sleep(1)
        print("...")
        if passcode_correct == passcode:
            input("ACCESS GRANTED ")
            print("You go through the door.")
            doctor.location = corr4
            doctor.room_descrip()
        else:
            doctor.location = corr3
            doctor.location.coordinates = [0, 0, teleport, passenger]
            print("ACCESS DENIED ")
        

# Character

class Character(object):
    def __init__(self,name,location,inv):
        self.name = name
        self.location = location
        self.inv = inv
        
    def room_descrip(self):
        if self.location.name == "Cargo Hold":
            print("You are in a large room.")
            print("There are crates piled from floor to ceiling.")
        elif self.location.name == "Corridor #1":
            print("You are in a metallic grey corridor.")
        elif self.location.name == "Engine Room":
            print("You are in an engine room.")
            print("The Tardis is well hidden here.")
        elif self.location.name == "Console Room":
            print("You are in a small room.")
            print("There are 3 consoles in the middle.")
        elif self.location.name == "Corridor #2":
            print("Two corridors join together.")
            print("From here you can travel any direction but South.")
        elif self.location.name == "Security":
            print("You are in a security room.")
            if self.location.item == ["Guard"]:
                Items.guard_block(object)
            else:
                pass
        elif self.location.name == "Corridor #3":
            print("You are in a metallic grey corridor.")
        elif self.location.name == "Corridor #4":
            print("You are in a metallic grey corridor.")
        elif self.location.name == "Control Room":
            print("You are in a room marked 'Main Control'.")
        elif self.location.name == "Passenger Room":
            if "Clara" not in doctor.inv:
                print("You are in a room marked: 'PASSENGERS'.")
                input("You see rows after row of Stasis Pods.")
                print("Inside each one is a different species.")
                print("Silurians, Menoptera, Ood, Argolins, Hath...")
                print("Categorised and catalogued.")
            else:
                print("You see rows of empty Stasis Pods")
        elif self.location.name == "Teleportation Room":
            print("This room has a huge teleportation grid.")
            print("It is designed to teleport masses of people at once.")
        else:
            pass
        
    def look(self):
        if self.location.item == ["Sonic Screwdriver"]:
            Items.get_sonic_screwdriver(self)
        elif self.location.item == "Tardis":
            Items.see_tardis(self)
        elif self.location.item == ["Console"]:
            Items.use_console(self)
        elif self.location.item == ["Pods"]:
            Items.pods_block(self)
        elif self.location.item == ["Map"]:
            Items.room_map(self)
        elif self.location.item == ["Control Panel"]:
            Items.use_control_panel(self)
        elif self.location.item == ["Teleporters"]:
            Items.use_teleporters(self)
        elif self.location.item == "Door West":
            print("There is a door blocking your path to the west.")
        elif self.location.item == "Door East":
            print("There is a door blocking your path to the east.")
        elif self.location.item == "none":
            print ("There is nothing of interest here.")
        else:
            print("There is nothing of interest here.")
            
    def inventory(self):
        print("You are carrying: ")
        for item in doctor.inv:
            print(item)

doctor = Character("The Doctor", engine,["Tardis Key", "Psychic Paper"])

print ("\t\tDOCTOR WHO: PASSENGERS")
print ("\t\tA Text Based Adventure\n\n")
print ("Clara has been kidnapped.")
print ("Fortunately, she was carrying your Sonic Screwdriver.")
print ("You have locked on to the signal and have landed nearby.")
input ("It is up to you to rescue Clara and escape in the Tardis.\n")

print ("Clara has been kidnapped. Fortunately, she was carrying\
       \nyour Sonic Screwdriver.You have locked on to the signal and\
       \nhave landed nearby.It is up to you to rescue Clara and escape\
       \nin the Tardis.")
time.sleep(1)

#Help

def help_function():
    print("""
             ~~~~~~~~~~~~~~~~~~~
    """)
    print ("\t\tGAME COMMANDS")
    print ("\n"'"n","e","s", and "w" to move.')
    print ('"look" to look around the room.')
    print ('"inv" to see your inventory.')
    print ('"use <item>" to use an item or object.')
    print ('"end" to quit the game. All progress will be lost.')
    print ('"help" to see this list again.')
        

# Main Game Loop

help_function()
input("\nPress enter to begin ")
time.sleep(1)
print("""
             ~~~~~~~~~~~~~~~~~~~
    """)
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
                input("GUARD: Level 5 Clearance granted. You may pass.")
                doctor.location.coordinates = [0, 0, control, corr2] 
            else:
                print("It had no effect")
        else:
            pass

    if command == "use sonic screwdriver":
        if "Sonic Screwdriver" in doctor.inv:
            if doctor.location == passenger and doctor.location.item == ["Pods"]:
                doctor.location.item.remove("Pods")
                print("A buzzer sounds and the Stasis doors open.")
                print("The 'passengers' begin to regain consciousness.")
                print("You tell them to head to the Teleportation Room")
                print ("You help Clara up and out of her Pod.")
                doctor.inv.append("Clara")
            else:
                print("It had no effect.")
        else:
            print("You do not have your Sonic Screwdriver.")

    if command == "use tardis key":
        if doctor.location == engine:
            if "Clara" in doctor.inv and teleport_species == 1 and return_ship == 1:
                print("WHIIIRRRRR...")
                time.sleep(2)
                print("WHIIIIIIIIRRRRRR...")
                time.sleep(2)
                print("WHIIIIIIIIIRRRRRRRRRR...")
                time.sleep(2)
                print("The Tardis fades out of the room.")
                time.sleep(2)
                print("The Doctor and Clara have escaped.")
                time.sleep(3)
                input("I hope you have enjoyed the adventure.\
                      \nThanks for playing.\n")
                time.sleep(2)
                break
            elif "Clara" in doctor.inv and teleport_species == 1 and return_ship == 0:
                print("You need to send a message first.")
                print("Head to the Main Control room")
            elif "Clara" in doctor.inv and teleport_species == 1 and return_ship == 0:
                print("You need to save the other species")
                print("Head to the teleportation room")
            elif "Clara" in doctor.inv and teleport_species == 0 and return_ship == 0:
                print("You need to save the other species")
                print("Head to the teleportation room")
            elif "Clara" not in doctor.inv:
                print("You can't leave without Clara")
        else:
            print("The Tardis is not in this room.")

    if command == "use console":
        if doctor.location == console:
            Items.use_console(object)
        else:
            pass

    if command == "use main control":
        if doctor.location == control:
            Items.use_control_panel(object)
        else:
            pass

    if command == "use teleporter":
        if doctor.location == teleport:
            Items.use_teleporters(object)
        else:
            pass

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
    if command == ("use knowledge"):
        if "Knowledge" in doctor.inv:
            ship_knowledge()
        else:
            print("You do not have that information.")
    if command == "end":
        break

input("\nPress enter to exit")

# end

    # ++++ Room Map +++++
    #                               1. cargo
    # ===================           2. corr1
    #       --------------          3. engine
    #       | 1   2    3 |          4. console
    #       |---|    |---|          5. corr2   
    #       | 4   5    6 |          6. security
    #   |------------|   |          7. passenger
    #   | 7   8   9   10 |          8. corr3
    #   -----    ---------          9. corr4
    #       | 11 |                  10. control 
    #       -----                   11. teleport
    # ===================
