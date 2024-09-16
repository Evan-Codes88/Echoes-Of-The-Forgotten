# Importing
import colorama
from colorama import Fore, Back, Style
import json
import time
from typewrite import typewrite
from player import Player

def opening_sequence():
    typewrite("You awaken in a dense forest, the sunlight barely piercing the thick canopy above...\n")
    time.sleep(1)
    typewrite("A sword lies beside you, and sounds of creatures echo in the distance...\n")
    time.sleep(1)
    typewrite("As you pick up the sword, you notice a name is engraved in the hilt...\n")
    time.sleep(0.5)
    name = input(typewrite("What name is engraved in the sword? "))
    return name

def start_game():

    # Call the opening sequence and get the player's name
    player_name = opening_sequence()
    
    # Create the Player object with the name from the opening sequence
    player = Player(player_name)
    
    typewrite(f"Ahhh...your name must be, {player_name}\n").strip()
    time.sleep(0.5)
    typewrite("You stand up and sheath the sword at your side.\n")
    time.sleep(1)
    player.add_item("Sword", 1)
    time.sleep(1)
    typewrite("You have no memory of who or where you are...\n")
    time.sleep(1)
    typewrite("What would you like to do?\n")

    while True:

        typewrite("1. Explore your surroundings\n")
        typewrite("2. Check inventory\n")
        typewrite("3. Rest\n")
        typewrite("4. Quit the game!\n")

        choice = input(typewrite("Choose an action: ")).strip()

        if choice == "1":
            pass
        elif choice == "2":
            player.show_inventory()
        elif choice == "3":
            pass
        elif choice == "4":
            typewrite(f"Your adventure ends here. Farewell {player_name}\n")
            break
        else:
            typewrite("Invalid choice. Try again\n")












# Start the game
if __name__ == "__main__":
    start_game()





