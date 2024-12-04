import colorama
from colorama import Fore, Style
# imports the colorama library to print different colours and fonts in the terminal

import json
# imports json module, this allows the game the save progress in json format that can be loaded on command

import time

from typewrite import typewrite
# Imports the function 'typewriter', when called give a typewriter affect when printing text in the terminal

from enemy import Enemy
# imports the enemy class, used for defining an enemy character and its attributes in game. expanded explanation in enemy.py

from error import invalid_input
# imports invalid_input function, tells the user if their input is valid or not

from game_utils import save_before_quit
# imports save_before_quit function, allows user to save game progress

def path_of_shadows(player):
    typewrite("You leave the structure, stepping out into the forest once more. The sun is low on the horizon, casting long shadows across the ground. You set off toward the Path of Shadows, the locket heavy in your pocket...\n")
    time.sleep(1)
    typewrite("The air grows colder, and the trees around you become twisted, almost as if they are watching you. A strange energy fills the air, urging you forward.\n")
    time.sleep(1)

    """
    Purpose: This function handles the players experience along the path of shadows
    
    parameters: player (object), handles attributes like players state, health points current inventory and any saved progress. currently path of shadows 
    
    Returns: moves to ending() if player is defeated, if not player is continued onto third_enemy(player)
    """

    player.game_state = "second_enemy_encounter"
    player.save_game(silent=True)

    """
    players current state is now 'second enemy encounter'
    
    silent=True, saving the game progress without explicit confirmation in terminal
    """

    # First enemy encounter
    enemy = Enemy("Shadow Wraith", 60)
    sword_damage = 25
    enemy_attack_damage = 15

    """
    enemy variable,
    
    creates instance of the enemy class to represent the first enemy encounter in the game, 'shadow wraith', defines 60 health points, 25 sword damage and 25 attack damage. 
    """


    time.sleep(1)
    typewrite("\nSuddenly, the ground trembles. A shadowy figure darts across the path and stops in front of you, blocking the way.\n")
    time.sleep(1)
    typewrite(Fore.RED + "A Shadow Wraith emerges, its form flickering like smoke in the wind." + Style.RESET_ALL)

    while enemy.health > 0 and player.health > 0:
        typewrite(f"\nEnemy Health: {enemy.health}\n")
        typewrite(f"Your Health: {player.health}\n")
        
        typewrite("\nWhat would you like to do?\n")
        typewrite("1. Attack with Sword\n")
        typewrite("2. Check Inventory\n")
        typewrite("3. Run away\n")

        choice = input(typewrite("Choose an action: ")).strip()

        """
        while loops to handle the repetitive actions of the game: display health and damage and player actions.
        
        if the enemy heath drops to 0 they;re defeated, if player health drops to 0, player is defeated. enemy or player will die.
        """

        if choice == "1":
            player.attack(enemy, sword_damage)

            """
              Purpose: this handles the players decisions during the battle with first enemy, attacks, counter attacks and damage dealt and received. 
              choice '1', player attacks with sword, 
              
              parameters: enemy (current enemy object), sword_damage )the damage inflicted by the players sword.
              
              """

            if enemy.health > 0:
                typewrite("The Shadow Wraith hisses and lashes out with its ethereal claws!\n")
                while True:
                    typewrite("\nThe wraith lunges at you! Quick, dodge!\n")
                    typewrite("1. Dodge left\n")
                    typewrite("2. Dodge right\n")
                    dodge_choice = input(typewrite("Choose your dodge: ")).strip()

                    """ 
                    checks if the enemy is still alive, if they are continue to more choices
                    """

                    if dodge_choice == "1":
                        typewrite("You dodge left, narrowly avoiding the wraith's attack!\n")
                        break
                    elif dodge_choice == "2":
                        typewrite("You try to dodge right, but the wraith's claws graze you!\n")
                        player.take_damage(enemy_attack_damage)
                        if player.health <= 0:
                            typewrite(Fore.RED + "You have been defeated...\n" + Style.RESET_ALL)
                            return
                        break
                    else:
                        invalid_input()
                        typewrite(Fore.RED + "Please choose '1' to dodge left or '2' to dodge right.\n" + Style.RESET_ALL)\

                        """
                        this loops through the players options, either narrowly escaping the enemy or being defeated.
                        """

        elif choice == "2":
            player.show_inventory()

        elif choice == "3":
            typewrite("You try to run away, but the wraith blocks your escape!\n")

            """
            choice 2 and 3 are showing inventory and attempting to escape
            """

        else:
            invalid_input()
            typewrite(Fore.RED + "Please choose '1', '2', or '3'.\n" + Style.RESET_ALL)

            """
            returns input error if invalid 
            """

    if enemy.health <= 0:
        typewrite(Fore.GREEN + "You have defeated the Shadow Wraith!\n" + Style.RESET_ALL)
        # Continue to the next enemy encounter
        third_enemy(player)
    elif player.health <= 0:
        typewrite(Fore.RED + "You have been defeated by the Shadow Wraith...\n" + Style.RESET_ALL)
        return

    """
    if the enemy health is = 0, continue to third enemy, if defeated continues to exit and end game
    """


def third_enemy(player):
    player.game_state = "third_enemy_encounter"
    player.save_game(silent=True)

    """
    Purpose: defines the third enemy encounter of the player, changing game state to 'third_enemy_encounter' and changing silent to 'True' and saving progress.
    
    parameters: player (object), defines the area the player is in. currently 'third_enemy_encounter'
    
    Returns: None, updates game state
    """

    typewrite("After defeating the wraith, a strange symbol glows faintly on the path ahead. The locket in your pocket pulses, resonating with the symbol.\n")
    time.sleep(1)
    typewrite("'I'm getting closer,' you whisper to yourself, your heartbeat quickening as you continue down the path.\n")
    
    enemy = Enemy("Shadow Sentinel", 90)
    sword_damage = 30
    enemy_attack_damage = 20

    """
    enemy variable,
    
    creates instance of the enemy class to represent the third enemy encounter in the game, 'Shadow Sentinel', defines 90 health points, 30 sword damage and 20 attack damage. 
    """


    time.sleep(1)
    typewrite("\nThe forest seems to grow darker with each step. Ahead, a hulking figure emerges from the shadows, its eyes gleaming with malice.\n")
    time.sleep(1)
    typewrite(Fore.RED + "A Shadow Sentinel blocks your way, towering over you with immense strength." + Style.RESET_ALL)

    while enemy.health > 0 and player.health > 0:
        typewrite(f"\nEnemy Health: {enemy.health}\n")
        typewrite(f"Your Health: {player.health}\n")

        typewrite("\nWhat would you like to do?\n")
        typewrite("1. Attack with Sword\n")
        typewrite("2. Check Inventory\n")
        typewrite("3. Run away\n")

        choice = input(typewrite("Choose an action: ")).strip()

        """
         while loops to handle the repetitive actions of the game: display health and damage and player actions.
    
        if the enemy heath drops to 0 they're defeated, if player health drops to 0, player is defeated. enemy or player will die.
        """

        if choice == "1":
            player.attack(enemy, sword_damage)

            if enemy.health > 0:
                typewrite("The Shadow Sentinel roars in pain and charges at you!\n")
                while True:
                    typewrite("\nThe sentinel rushes at you! Quick, dodge!\n")
                    typewrite("1. Dodge left\n")
                    typewrite("2. Dodge right\n")

                    dodge_choice = input(typewrite("Choose your dodge: ")).strip()

                    if dodge_choice == "1":
                        typewrite("You dodge left, barely avoiding the sentinel's charge!\n")
                        break
                    elif dodge_choice == "2":
                        typewrite("You try to dodge right, but the sentinel's massive arm catches you!\n")
                        player.take_damage(enemy_attack_damage)
                        if player.health <= 0:
                            typewrite(Fore.RED + "You have been defeated...\n" + Style.RESET_ALL)
                            return
                        break
                    else:
                        invalid_input()
                        typewrite(Fore.RED + "Please choose '1' to dodge left or '2' to dodge right.\n" + Style.RESET_ALL)


                """
                choice '1' results in enemy attacking and charging at player.
                 2 options to choose from, avoiding the attack or being defeated.s
                """

        elif choice == "2":
            player.show_inventory()

        elif choice == "3":
            typewrite("You try to run away, but the sentinel blocks your path!\n")

            """
            choice '2' and '3' show inventory and attempting to flee
            """

        else:
            invalid_input()
            typewrite(Fore.RED + "Please choose '1', '2', or '3'.\n" + Style.RESET_ALL)

            """
            returns input error if invalid 
            """

    if enemy.health <= 0:
        typewrite(Fore.GREEN + "You have defeated the Shadow Sentinel!\n" + Style.RESET_ALL)
        final_revelation(player)  # Continue to final revelation
    elif player.health <= 0:
        typewrite(Fore.RED + "You have been defeated by the Shadow Sentinel...\n" + Style.RESET_ALL)
        return

    typewrite("You narrowly defeat the sentinel, your body aching from the battle. The path grows even darker, but in the distance, you see a faint light.\n")
    time.sleep(1)
    typewrite("You approach cautiously, and as you do, the locket begins to glow brighter, almost pulling you toward the source of the light.\n")
    player.game_state = "final_revelation"
    player.save_game(silent=True)


    """
    if enemy heath drops to 0 they are defeated and player progress is saved and continues to final_revelation, if they are defeated game ends/
    """


def final_revelation(player):
    # Final revelation and twist
    typewrite("\nAt the end of the path, you find an ancient, glowing portal standing before you. The locket vibrates intensely, and in a flash of light, you remember everything.\n")
    time.sleep(1)
    typewrite(Fore.CYAN + "The person you’ve been searching for... was never someone else. It was you—\n" + Style.RESET_ALL)
    time.sleep(1)
    typewrite(Fore.CYAN + "But not in the way you expected. This whole journey has been a test, a manipulation of your mind by something far darker.\n" + Style.RESET_ALL)

    typewrite("You recall now: you were once part of a powerful order meant to protect the world from beings of shadow. But during one of your missions, you were captured... and your memories were stripped away.\n")
    time.sleep(1)
    typewrite("The locket was not just a key to your memories. It was the very object binding you to this shadow realm.\n")

    typewrite(Fore.RED + "'You were never meant to leave,' a voice echoes from the darkness.\n" + Style.RESET_ALL)
    time.sleep(1)
    typewrite("You turn to see a figure cloaked in shadows, their eyes glowing red. 'I brought you here, and now that you’ve passed the test, you can never return.'\n")
    time.sleep(1)

    """
    the game twist is revealed and it was all a test and the players memory was stripped but it has now returned. You find another enemy
    """

    # Final decision point
    while True:
        typewrite("\n1. Fight the shadow figure\n")
        typewrite("2. Accept your fate\n")
        choice = input(typewrite("Choose your action: ")).strip().lower()

        if choice == "1":
            typewrite(Fore.YELLOW + "You charge at the figure, sword drawn!\n" + Style.RESET_ALL)
            time.sleep(1)
            typewrite(Fore.GREEN + "In a blinding flash, the light from your locket merges with your energy, and you fight with newfound strength...\n" + Style.RESET_ALL)
            time.sleep(1)
            typewrite(Fore.GREEN + "You succeed in vanquishing the shadow figure!\n" + Style.RESET_ALL)
            time.sleep(1)
            ending()

        elif choice == "2":
            typewrite(Fore.RED + "You surrender to the darkness, allowing it to envelop you...\n" + Style.RESET_ALL)
            ending()

        else:
            invalid_input()

            """
            final decision point for the player to either accept fate or fight, if fought players wins continues to ending, if not game ends and player surrenders to darkness
            """


def ending():
    typewrite("Thank you for playing!!")
    time.sleep(2)
    quit()

    """
    Purpose: displays a message when closing the game
    
    Parameters: None
    
    Returns: quit, this function ends the game
    """