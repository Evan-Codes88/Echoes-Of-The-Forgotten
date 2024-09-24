# Importing
import colorama
from colorama import Fore, Style
import json
import time
from typewrite import typewrite
from player import Player
from error import invalid_input
from game_utils import save_before_quit
from path_of_shadows import path_of_shadows

def investigate_structure(player):
    player.game_state = "investigating_structure"
    player.save_game(silent=True)
    
    typewrite("You walk cautiously toward the crumbling stone structure. The air grows colder, and you feel the weight of something watching you.\n")
    time.sleep(0.5)
    
    typewrite("The entrance to the structure is a dark archway covered in vines. \nAs you step inside, the dim light reveals a large, circular chamber. The walls are lined with ancient symbols, and in the center of the room stands an imposing stone pedestal.\n")
    typewrite("On the pedestal lies a rusted, ornate key, seemingly important. \nHowever, as you reach for it, a low rumbling sound echoes through the chamber. The walls begin to shift, and a voice, deep and ethereal, fills the space.\n")
    time.sleep(1)
    
    typewrite(Fore.CYAN + "'The path forward is one of nature’s cycle. Begin with the dawn of creation and end with the shadows of time.'\n" + Style.RESET_ALL)
    time.sleep(1)
    
    typewrite("\nYou notice that the symbols on the wall are now glowing faintly. \nThey represent different elements: Rain, Shadow, Growth, Sun, and Seed. On the pedestal, just below the key, are five small slots, each shaped like one of the elemental symbols.\n")
    typewrite("It seems you need to arrange the elements in the correct order to claim the key...\n")

    # Puzzle clue
    typewrite(Fore.YELLOW + "Clue: The voice mentioned 'nature’s cycle' and to 'begin with the dawn of creation and end with the shadows of time.' Perhaps the order follows the life cycle of something in nature?\n" + Style.RESET_ALL)

    # Puzzle Solution
    correct_order = ["sun", "rain", "seed", "growth", "shadow"]

    # Player input loop for solving the puzzle
    while True:
        typewrite("\nEnter the five elements in the correct order (separated by commas):\n")
        input_elements = input("> ").lower().split(", ")  # convert answer to lowercase to avoid errors
        
        # Validate input length
        if len(input_elements) != 5:
            typewrite(Fore.RED + "\nYou must enter exactly five elements.\n" + Style.RESET_ALL)
            continue

        # Validate if input elements are valid
        valid_elements = ["sun", "rain", "seed", "growth", "shadow"]
        for element in input_elements:
            if element not in valid_elements:
                typewrite(Fore.RED + f"\n'{element}' is not a valid element. Please enter valid elements: {', '.join(valid_elements)}.\n" + Style.RESET_ALL)
                break
        else:  # This executes if the for loop completes without a break
            if input_elements == correct_order:
                typewrite(Fore.GREEN + "\nThe key glows brightly, and the voice returns:\n" + Style.RESET_ALL)
                typewrite(Fore.CYAN + "'You have chosen wisely. The key is yours, but nature’s balance can never be restored.'\n" + Style.RESET_ALL)
                typewrite("The rumbling stops, and the key loosens from the pedestal. You carefully take it and place it in your inventory.\n")
                player.add_item("Ancient Key")
                castle(player)
                player.game_state = "solved_puzzle"
                player.save_game(silent=True)
                break
            else:
                typewrite(Fore.RED + "\nThe symbols flash angrily as you hear the voice again:\n" + Style.RESET_ALL)
                typewrite(Fore.CYAN + "'Incorrect. You must understand the cycle to unlock the truth.'\n" + Style.RESET_ALL)

def castle(player):
    typewrite("With the ancient key now in your possession, the atmosphere in the chamber changes. The rumbling ceases, and an eerie stillness fills the room.\n")
    time.sleep(0.5)
    
    typewrite("As you glance around, you notice that the symbols on the walls have stopped glowing, but something new catches your attention. \nA faint outline of a door appears on the far side of the chamber, as though it has been hidden for centuries.\n")
    time.sleep(0.5)
    
    typewrite("With the key in hand, you approach the door, and as you get closer, the ancient stone grinds slowly open, revealing a narrow corridor leading deeper into the structure.\n")
    time.sleep(0.5)

    typewrite(Fore.CYAN + "'They are waiting... You must remember...'\n" + Style.RESET_ALL)

    typewrite("\nThe voice echoes in your mind, more familiar now, almost comforting in its strangeness. \nYou feel a pulse of recognition, as though the words have stirred something deep within your memories.\n")
    time.sleep(0.5)
    
    typewrite("Suddenly, a fragmented memory flashes before your eyes...\n")
    time.sleep(1)

    # Flashback memory
    typewrite(Fore.YELLOW + "In your vision, you see a shadowy figure standing in the doorway of a similar structure, beckoning you forward. There’s a feeling of urgency and sadness. \nThe figure’s voice, though distant, feels like someone you once knew, but their face remains a blur.\n" + Style.RESET_ALL)
    time.sleep(0.5)
    
    typewrite(Fore.YELLOW + "'I’ll be here, waiting for you. Find me before it’s too late.'\n" + Style.RESET_ALL)
    time.sleep(0.5)
    
    typewrite("You snap back to the present, your heart racing. \nThe figure in the vision must be connected to the person you’re searching for, but who are they?\n")
    typewrite("With a renewed sense of purpose, you step into the dark corridor, your footsteps echoing softly as you descend further into the depths of the ancient structure.\n")
    time.sleep(0.5)
    
    typewrite("The walls narrow, and the air grows colder as you proceed. \nFaint carvings of constellations and celestial patterns cover the walls, as if this place once held some significance to the stars.\n")
    time.sleep(0.5)
    
    typewrite("After what feels like an eternity, you come across another chamber, smaller than the first, \nbut filled with intricate murals depicting scenes of someone wandering through forests, rivers, and mountains.\n")
    time.sleep(0.5)
    
    typewrite("In the center of the room, there is a large stone tablet, covered in dust. \nYou wipe it clean, revealing a cryptic message etched into the surface.\n")
    time.sleep(0.5)

    # Message on the stone tablet (hint)
    typewrite(Fore.CYAN + "'The one you seek follows the path of shadows, through places forgotten by the sun. \nTheir fate is tied to the locket, and only in the light of the full moon will their truth be revealed.'\n" + Style.RESET_ALL)
    time.sleep(0.5)
    
    typewrite("The words send a chill down your spine. Could this be a clue about the locket you found earlier? \nAnd the 'path of shadows'... what does it mean?\n")
    time.sleep(0.5)

    typewrite("As you ponder the meaning of the message, another memory flickers at the edge of your consciousness.\n")
    time.sleep(0.5)

    typewrite(Fore.YELLOW + "You see the locket in your hand, but it’s different, new and unbroken. The same voice from before speaks, only now it’s clearer.\n" + Style.RESET_ALL)
    typewrite(Fore.YELLOW + "'This locket... It holds everything you need to find me. When the time comes, follow the moon and the stars. Don’t forget me.'\n" + Style.RESET_ALL)
    time.sleep(0.5)

    typewrite("The vision fades, but this time, the sense of urgency remains. \nYou realize that the locket is not just a trinket but a key to finding the person you’ve been searching for. \nThe murals around the chamber depict a journey that mirrors your own, and the 'path of shadows' must be a clue to where they’ve gone.\n")
    time.sleep(0.5)

    typewrite("You pocket the locket once more, determined to unlock its secrets when the full moon rises.\n")
    time.sleep(0.5)

    typewrite(Fore.YELLOW + "There must be more to uncover in this place. Perhaps the murals and the stars will lead the way.\n" + Style.RESET_ALL)
    time.sleep(0.5)

    typewrite("You decide to investigate the murals more closely, tracing your fingers over the patterns. \nOne of the murals shows a map of the surrounding area, with a trail marked as 'The Path of Shadows' \nwinding through the forest towards an old castle.\n")
    time.sleep(0.5)

    typewrite(Fore.CYAN + "It seems that the path leads to your next destination.\n" + Style.RESET_ALL)

    path_of_shadows(player)

