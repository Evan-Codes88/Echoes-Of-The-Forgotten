import json
from typewrite import typewrite
import colorama
from colorama import Fore, Style
import time


# Function to save the game before quitting
def save_before_quit(player):
    save_choice = input(typewrite("Would you like to save your game before quitting? (yes/no): ")).strip().lower()
    if save_choice == "yes":
        player.save_game()
    typewrite("Goodbye!\n")
    time.sleep(1)
    quit()