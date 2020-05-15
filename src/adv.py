from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.

# If the user enters "q", quit the game.
name = input("Tell me your name, Human: ")

#current room name
player = Player(name, room["outside"])
print(f"Hello {name}. Walk into the rooms and collect the coins. You are currently in the {player.room.name}")

while True:
    directions = input("Please pick a direction using:  'n' , 's' , 'w', 'e', 'q to quit'")
    print(player.room.description)

    movement = input("Choose year direction: ")
     
    walking = directions[movement]
    
    if directions == "n" or directions == "N":
        player.room = player.room.n_to
        if player.room == None:
            print("You can't go that direction. Try a different direction.")
    
        else:
            player = Player(name, player.room)
            print(player)
        

    elif directions == "s" or directions == "S":
        player.room= player.room.s_to
        if player.name == None:
            print("You can't go that direction. Try a different direction.")
             
        else:
            player = Player(name,player.room)
            print(player)

    elif directions == "e" or directions == "E":
       player.room = player.room.e_to 
       if player.room == None:
            print("You can't go that direction. Try a different direction.")
        
        else:
            player = Player(name,player.room)
            print(player)

    elif directions == "w" or directions == "W":
       player.room = player.room.w_to
        ifplayer.room == None:
           print("You can't go that direction. Try a different direction.")

        else:
            player = Player(name,player.room)
            print(player)
            
    elif directions == "q" or directions == "Q":
            print("Have a nice day human")
            break