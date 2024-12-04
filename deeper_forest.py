# Import the 'colorama' package to add coloured text to the console, this enhances user experience
import colorama 
# Import specific color-related tools
from colorama import Fore, Style  
# For saving/loading game data in JSON format
import json  
# To create delays for better narrative pacing
import time  
 # Custom function to simulate typewriter effect
from typewrite import typewrite 
# Import the Player class to handle player data
from player import Player  
# Custom function to handle invalid inputs
from error import invalid_input  
 # Function for exploring the structure further
from investigate_structure import investigate_structure 

# Function to handle the player exploring deeper into the forest
def explore_deeper_forest(player):
    """
    Purpose: Guides the player through a narrative sequence as they venture deeper into the forest, leading to the discovery of an ancient structure. Provides choices for the player to continue the adventure.
    
    Parameters:
    player (Player object): The player whose state and choices affect the game progress.
    
    Returns:
    None. The function updates the player's game state and directs them to the next part of the story.
    """

    # Narrative sequence describing the forest exploration
    print("")  # Add a blank line for better readability
    typewrite("You venture deeper into the dense forest. The trees grow more twisted, and the darkness begins to envelop you...\n")
    time.sleep(1)  # Pause for dramatic effect

    typewrite("As you move further in, you hear the rustling of leaves and distant whispers that seem to call your name.\n")
    time.sleep(1)
    typewrite("You can't shake the feeling that you are being watched, but your curiosity propels you onward.\n")
    time.sleep(1)

    typewrite("Suddenly, the trees part, revealing a clearing bathed in an eerie light. In the center of the clearing stands an ancient structure, its stone walls covered in vines and glowing runes.\n")
    time.sleep(1)

    typewrite("You approach the structure cautiously, your heart pounding in your chest. The air feels charged with energy as the locket in your pocket begins to thrum with a familiar warmth.\n")
    time.sleep(1)

    typewrite("You stand before the entrance, the dark doorway beckoning you to enter...\n")
    time.sleep(1)

    # Update the player's game state to indicate they've reached the ancient structure
    player.game_state = "ancient_structure"
    player.save_game(silent=True)  # Save the game silently without displaying a message

    # Loop until the player provides a valid input
    while True:  
        typewrite("Will you enter the structure? (yes/no)\n")  # Prompt the player to make a decision
        choice = input(typewrite("Choose your action: ")).strip().lower()  # Get player's input and normalise it

        if choice == "yes":
            # Player chooses to enter the structure
            typewrite("You gather your courage and step inside the ancient structure...\n")
            time.sleep(1)
            investigate_structure(player)  # Call the function to continue the story inside the structure
            break  # Exit the loop after the action is taken
        elif choice == "no":
            # Player hesitates but is compelled to enter anyway
            typewrite("You hesitate, feeling the weight of your decision. But the pull of the structure is too strong. You feel compelled to explore it further.\n")
            time.sleep(1)
            investigate_structure(player)  # Call the function to continue the story inside the structure
            break  # Exit the loop after the action is taken
        else:
            # Handle invalid inputs
            invalid_input()  # Custom function to handle incorrect input
            typewrite(Fore.RED + "Please enter 'yes' or 'no'.\n" + Style.RESET_ALL)  # Prompt the player to try again
