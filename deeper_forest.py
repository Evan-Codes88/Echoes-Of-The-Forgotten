# Importing
import colorama
from colorama import Fore, Style
import json
import time
from typewrite import typewrite
from player import Player
from error import invalid_input
from investigate_structure import investigate_structure

def explore_deeper_forest(player):
    print("")
    typewrite("You venture deeper into the dense forest. The trees grow more twisted, and the darkness begins to envelop you...\n")
    time.sleep(1)

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

    # Update the player's game state to indicate they've reached the structure
    player.game_state = "ancient_structure"
    player.save_game(silent=True)

    while True:  # Loop until a valid input is received
        typewrite("Will you enter the structure? (yes/no)\n")
        choice = input(typewrite("Choose your action: ")).strip().lower()

        if choice == "yes":
            typewrite("You gather your courage and step inside the ancient structure...\n")
            time.sleep(1)
            investigate_structure(player)
            break  # Exit the loop after the action is taken
        elif choice == "no":
            typewrite("You hesitate, feeling the weight of your decision. But the pull of the structure is too strong. You feel compelled to explore it further.\n")
            time.sleep(1)
            investigate_structure(player)
            break  # Exit the loop after the action is taken
        else:
            invalid_input()  # Call the invalid input handler
            typewrite(Fore.RED + "Please enter 'yes' or 'no'.\n" + Style.RESET_ALL)  # Provide additional feedback

