import colorama
from colorama import Fore, Style
import time
from typewrite import typewrite
from player import Player
from error import invalid_input
from enemy import Enemy
from game_utils import save_before_quit
from investigate_structure import investigate_structure
from deeper_forest import explore_deeper_forest

# Function for the enemy encounter at the water's edge
def enemy_encounter(player):
    # Update the game state to reflect the start of the encounter
    player.game_state = "first_enemy_encounter"
    player.save_game(silent=True)  # Auto-save before the first enemy encounter
    
    # Initialize the enemy with 50 health
    enemy = Enemy("Shadow Beast")
    sword_damage = 25
    enemy_attack_damage = 10

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

        if choice == "1":
            # Player attacks with sword
            player.attack(enemy, sword_damage)

            if enemy.health > 0:  # Enemy is still alive and counterattacks
                typewrite("The creature snarls in pain but quickly strikes back!\n")
                time.sleep(1)

                # Enemy attacks and player dodges
                while True:
                    typewrite("\nThe creature lunges at you! Quick, dodge!\n")
                    typewrite("1. Dodge left\n")
                    typewrite("2. Dodge right\n")

                    dodge_choice = input(typewrite("Choose your dodge: ")).strip()

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

        elif choice == "2":
            player.show_inventory()

        elif choice == "3":
            typewrite("You try to run away, but the creature blocks your path!\n")
        elif choice == "4":
            save_before_quit()
        else:
            invalid_input()

    # If the player defeats the enemy
    if enemy.health <= 0:
        typewrite(Fore.GREEN + "You have defeated the Shadow Beast!\n" + Style.RESET_ALL)
        post_enemy_story(player)  # Proceed to the next phase of the game
    elif player.health <= 0:
        typewrite(Fore.RED + "You have been defeated by the Shadow Beast...\n" + Style.RESET_ALL)

# Function for what happens after the enemy encounter
def post_enemy_story(player):
    # Update the game state after defeating the enemy
    player.game_state = "post_enemy_story"
    player.save_game(silent=True)  # Auto-save after defeating the enemy

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
