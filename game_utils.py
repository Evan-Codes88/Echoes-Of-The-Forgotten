# Import the 'typewrite' function from a custom module named 'typewrite.py' to display text with a typewriter effect
from typewrite import typewrite 
# Import the 'colorama' package to add coloured text to the console, this enhances user experience
import colorama
# Import specific features from 'colorama' for colour formatting and style resetting
from colorama import Fore, Style 
# Importing the time module to pause execution (used for the sleep function) This enhances user experience by allowing players to read at a comfortable speed and allows for breaks
import time

# Function to save the game before quitting
def save_before_quit(player):
    """
    Purpose: Prompts the player to save the game before quitting. If the player chooses to save, the game state is saved.

    Parameters:
    player (object): The player object whose current state will be saved if the player chooses to do so.

    Returns:
    None. If the player chooses to save, the game is saved, then the program exits.
    """
    # Prompt the player with the choice to save the game before quitting
    save_choice = input(typewrite("Would you like to save your game before quitting? (yes/no): ")).strip().lower()
    
    # If the player chooses 'yes', save the game
    if save_choice == "yes":
        player.save_game()  # Calls the save_game method of the player to save the game state
    
    typewrite("Goodbye!\n")  # Prints a goodbye message
    time.sleep(1)  # Pauses for 1 second to give the player time to read the message
    quit()  # Terminates the game
