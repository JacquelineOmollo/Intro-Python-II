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
#
# If the user enters "q", quit the game.
name = input("Tell me your name, Human")
player = Player(name, room["outside"])
print(f"Hello {name}. Walk into te rooms and collect the coins {player.room.name}")

while True:
    direction = {"n": "n_to", "s": "s_to", "w": "w_to", "e": "e_to", "q": "quit"}
    print(player.room.description)

    movement = input("Choose year direction", {name})
    walking = direction[movement]

    if direction == "n" or direction == "N":
        your_move = player.room.n_to
        if your_move == None:
            print("You can't go that direction. Try a different direction.")
    else:
        player = Player(name, your_move)
        print(player)

    elif direction == "s" or direction == "S":
        your_move = player.room.s_to
        if your_move == None:
            print("You can't go that direction. Try a different direction.")
    else:
        player = Player(name, your_move)
        print(player)

    elif direction == "e" or direction == "E":
         your_move = player.room.e_to
         if your_move == None:
             print("You can't go that direction. Try a different direction.")
    else:
         player = Player(name, your_move)
         print(player)

    elif direction == "w" or direction == "W":
         your_move = player.room.w_to
         if your_move == None:
         print("You can't go that direction. Try a different direction.")

    else:
        player = Player(name, your_move)
        print(player)