# Importing
import colorama
from colorama import Fore, Style
import json
import time
from typewrite import typewrite
from player import Player

# Function to save the game before quitting
def save_before_quit(player):
    save_choice = input(typewrite("Would you like to save your game before quitting? (yes/no): ")).strip().lower()
    if save_choice == "yes":
        player.save_game()
    else:
        typewrite("Goodbye!\n")
        quit

# Function for the opening sequence
def opening_sequence():
    time.sleep(1)
    typewrite("You awaken in a dense forest, the sunlight barely piercing the thick canopy above...\n")
    time.sleep(1)
    typewrite("A sword lies beside you, and sounds of creatures echo in the distance...\n")
    time.sleep(1)
    typewrite("You have no memory of who or where you are...\n")
    time.sleep(1)
    typewrite("As you pick up the sword, you notice a name is engraved in the hilt...\n")
    time.sleep(0.5)
    name = input(typewrite("What name is engraved in the sword? "))
    return name

# Function to start a new game
def start_new_game():
    player_name = opening_sequence()
    player = Player(player_name)
    typewrite(f"Ahhh...your name must be, {player_name}\n")
    time.sleep(0.5)
    typewrite("You stand up and sheath the sword at your side.\n")
    time.sleep(1)
    player.add_item("Sword", 1)
    time.sleep(1)
    typewrite("A strange sense of familiarity washes over you, as though you’ve been here before...\n")
    typewrite("What would you like to do?")
    time.sleep(1)
    game_loop(player)

# Function to load a saved game
def load_game():
    player = Player.load_game()
    if player:
        typewrite(f"Welcome back, {player.name}!\n")
        game_loop(player)

# Central game loop
def game_loop(player):
    while True:
        typewrite("1. Explore your surroundings\n")
        typewrite("2. Check inventory\n")
        typewrite("3. Rest\n")
        typewrite("4. Quit the game\n")
        
        choice = input(typewrite("Choose an action: ")).strip()

        if choice == "1":
            explore(player)
        elif choice == "2":
            player.show_inventory()
        elif choice == "3":
            typewrite("You lay down and close your eyes, falling asleep almost instantly...\n")
            time.sleep(2)
        elif choice == "4":
            save_before_quit(player)
            break
        else:
            typewrite("Invalid choice. Try again.\n")

# Function for exploring the surroundings
def explore(player):
    typewrite("You're standing in the heart of a dense, mysterious forest. The air is thick with the smell of moss and damp earth, while towering trees with gnarled, twisted trunks rise high above, their leaves forming a canopy that blocks out most of the sunlight...\n")
    time.sleep(1)
    typewrite("To your right, you can make out the faint outline of an overgrown path. To your left, the trees form a near-impenetrable wall. Far ahead, the faint sound of rushing water can be heard.\n")
    time.sleep(1)
    typewrite("Which way would you like to go?\n")

    while True:
        typewrite("1. Go left\n")
        typewrite("2. Go right\n")
        typewrite("3. Show Inventory\n")
        typewrite("4. Quit the game\n")

        choice2 = input(typewrite("Choose an action: ")).strip()

        if choice2 == "1":
            typewrite("You push through the dense forest...\n")
            time.sleep(1)
        elif choice2 == "2":
            typewrite("You carefully step onto the overgrown path...\n")
            time.sleep(1)
        elif choice2 == "3":
            player.show_inventory()
        elif choice2 == "4":
            save_before_quit(player)
            break
        else:
            typewrite("Invalid choice. Try again.\n")

# Main menu at the start of the game
def main_menu():
    while True:
        typewrite("Welcome to Echoes of the Past\n")
        print("----------------------------")
        typewrite("1. Start a New Game\n")
        typewrite("2. Load Saved Game\n")
        typewrite("3. Quit\n")
        
        choice = input(typewrite("Select an option: ")).strip()
        
        if choice == "1":
            start_new_game()
            break
        elif choice == "2":
            load_game()
            break
        elif choice == "3":
            typewrite("Goodbye!\n")
            break
        else:
            typewrite("Invalid choice. Try again.\n")

# Start the game
if __name__ == "__main__":
    main_menu()
