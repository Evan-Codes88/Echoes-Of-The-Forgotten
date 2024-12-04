from colorama import Fore, Style
# imports the colorama library to print different colours and fonts in the terminal

import time
# imports time module, used to pause for a specified amount of time

from typewrite import typewrite
# Imports the function 'typewriter', when called give a typewriter affect when printing text in the terminal

from error import invalid_input
# imports invalid_input function, tells the user if their input is valid or not

from enemy import Enemy
# imports enemy class, defines an enemy character in the game. expanded explanation in enemy.py

from game_utils import save_before_quit
# imports save_before_quit function, allows user to save game progress

from investigate_structure import investigate_structure
# imports investigate_structure, player state. expanded explanation in investigate_structure.py

from deeper_forest import explore_deeper_forest
# imports deeper_forest function, player state. expanded explanation in deeper_deeper.py

def enemy_encounter(player):
    # Update the game state to reflect the start of the encounter
    player.game_state = "first_enemy_encounter"
    player.save_game(silent=True)  # Auto-save before the first enemy encounter

    """
      purpose: Defines a fight between the player and the first enemy (shadow beast)
    
      parameters: player (object), handles attributes like players state, health points current inventory and any saved progress. 
                    
      Return: none, changes game state.
    """
    
    # Initialize the enemy with 50 health
    enemy = Enemy("Shadow Beast")
    sword_damage = 25
    enemy_attack_damage = 10

    """
    enemy variable,
    
    creates instance of the enemy class to represent the first enemy encounter in the game, 'Shadow Beast', defines 50 health points, 25 sword damage and 10 attack damage. 
    """


    time.sleep(1)
    typewrite("\nAs you stand by the water’s edge, a low growl rumbles from behind you...\n")
    time.sleep(1)
    typewrite("You turn to see a large, shadowy creature emerging from the trees. Its eyes gleam with menace as it prepares to attack!\n")
    time.sleep(1)

    while enemy.health > 0 and player.health > 0:  # Game loop for combat
        typewrite(f"\nEnemy Health: {enemy.health}\n")
        typewrite(f"Your Health: {player.health}\n")
        
        typewrite("\nWhat would you like to do?\n")
        typewrite("1. Attack with Sword\n")
        typewrite("2. Check Inventory\n")
        typewrite("3. Run away\n")
        typewrite("4. Quit the game\n")

        choice = input(typewrite("Choose an action: ")).strip()

        """
               while loops to handle the repetitive actions of the game: display health and damage and player actions.

               if the enemy heath drops to 0 they;re defeated, if player health drops to 0, player is defeated. enemy or player will die.
               
               checks for player keyboard input
               """

        if choice == "1":
            # Player attacks with sword
            player.attack(enemy, sword_damage)

            """
              Purpose: this handles the players decisions during the battle with first enemy, attacks, counter attacks and damage dealt and received. 
              choice '1', player attacks with sword, 
    
              parameters: enemy (current enemy object), sword_damage )the damage inflicted by the players sword.
    
            """

            if enemy.health > 0:  # Enemy is still alive and counterattacks
                typewrite("The creature snarls in pain but quickly strikes back!\n")
                time.sleep(1)

                # Enemy attacks and player dodges
                while True:
                    typewrite("\nThe creature lunges at you! Quick, dodge!\n")
                    typewrite("1. Dodge left\n")
                    typewrite("2. Dodge right\n")
                    dodge_choice = input(typewrite("Choose your dodge: ")).strip()

                    """ 
                    checks if the enemy is still alive, if they are continue to more choices
                    """

                    if dodge_choice == "1":
                        typewrite("You dodge left, narrowly avoiding the creature's claws!\n")
                        break
                    elif dodge_choice == "2":
                        typewrite("You try to dodge right, but the creature catches you with a vicious swipe!\n")
                        player.take_damage(enemy_attack_damage)
                        if player.health <= 0:  # Check if the player dies
                            typewrite(Fore.RED + "You have been defeated...\n" + Style.RESET_ALL)
                            return  # End the encounter if the player is dead
                        break
                    else:
                        invalid_input()

                """
                this loops through the players options, either narrowly escaping the enemy or being defeated.
                """

        elif choice == "2":
            player.show_inventory()

        elif choice == "3":
            typewrite("You try to run away, but the creature blocks your path!\n")
        elif choice == "4":
            save_before_quit()
        else:
            invalid_input()

            """
            choice 2 and 3 are showing inventory and attempting to escape
            """

            """
              returns input error if invalid
            """

    # If the player defeats the enemy
    if enemy.health <= 0:
        typewrite(Fore.GREEN + "You have defeated the Shadow Beast!\n" + Style.RESET_ALL)
        post_enemy_story(player)  # Proceed to the next phase of the game
    elif player.health <= 0:
        typewrite(Fore.RED + "You have been defeated by the Shadow Beast...\n" + Style.RESET_ALL)

        """
            if the enemy health is = 0, continue to third enemy, if defeated continues to exit and end game
        """

# Function for what happens after the enemy encounter
def post_enemy_story(player):
    # Update the game state after defeating the enemy
    player.game_state = "post_enemy_story"
    player.save_game(silent=True)  # Auto-save after defeating the enemy
    
    """
    Purpose: This function handles the players experience along the 'post enemy story'
    
    parameters: player (object), handles attributes like players state
    """

    typewrite("\nAs the dust settles, you look around the area. The river flows calmly again, but something about the locket tugs at your mind...\n")
    time.sleep(1)
    typewrite("Ahead, the path seems to diverge into two directions. One leads deeper into the forest, and the other towards a crumbling stone structure.\n")

    while True:
        typewrite("\n1. Investigate the stone structure\n")
        typewrite("2. Explore deeper into the forest\n")
        typewrite("3. Check inventory\n")

        choice = input(typewrite("Choose an action: ")).strip()

        if choice == "1":
            player.game_state = "investigating_structure"
            player.save_game(silent=True)
            investigate_structure(player)
            break
        elif choice == "2":
            player.game_state = "exploring_forest"
            player.save_game(silent=True)
            explore_deeper_forest(player)
            break
        elif choice == "3":
            player.show_inventory()
        else:
            invalid_input()

         # returns input error if invalid

        """
        player has the choice to either explore the stone structure or forest, chosen will change game state to deeper_forest or investigate structure
        """
