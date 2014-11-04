class Room(object):
    """ Rooms """
    def __init__(self,name,description,monster_y_n):
            self.name = name
            self.description = description
           # self.monster_y_n = monster_y_n
            #if self.monster_y_n == "y":
             #   monster = make_monster()
              #  self.monster = monster
    # Rooms
    # last input is coordinates (n,e,s,w)
    #
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
    #
    # Template:
    # room# = Room(name,description,monster in it? (y/n))
    # Then add the coordinates below the room creators
    
room1 = Room("Cargo #32","There are crates piled from floor to ceiling. \nYou hear the familiar buzz of your Sonic Screwdriver coming from \na metallic box on the floor.", "n")
room2 = Room("Corridor #12","You are in a dark grey corridor.","n")
room3 = Room("Corridor #13","You are in a dark grey corridor","n")
room4 = Room("???","You are in a room which resembles an art gallery. \nThere is a stone tablet on the wall","n")
room5 = Room("Corridor #22","You are in a dark grey corridor. \nFrom here you can travel in any direction","n")
room6 = Room("Corridor #23","You are in a dark grey corridor. \nA guard is blocking your path to the East","y")
room7 = Room("Jail","You see Clara unconscious on the floor of a cell. \n It looks like it has an electronic lock","n")
room8 = Room("Corridor #32","You are in a dark grey corridor. \nA door blocks your path to the west.","n")
room9 = Room("Corridor #33","You are in a dark grey corridor. \n","y")


    # Room coordinates (had to create all the rooms to assign them to coordinates)
room1.coordinates = [0,room2,0,0]
room2.coordinates = [0,room3,room5,room1]
room3.coordinates = [0,0,0,room2]
room4.coordinates = [0,room5,0,room4]
room5.coordinates = [room2,room6,0,room4]
room6.coordinates = [0,0,room9,room5]
room7.coordinates = [0,room8,0,0]
room8.coordinates = [0,room9,0,room7]
room9.coordinates = [room6,0,0,room8]



input("exit")
