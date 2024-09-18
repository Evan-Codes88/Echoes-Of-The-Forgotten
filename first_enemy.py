# Importing
import colorama
from colorama import Fore, Style
import json
import time
from typewrite import typewrite
from player import Player
from error import invalid_input

# Created a new file with the enemy encounter to keep things neat and tidy and manage enemies that have different statistics

# Create a simple Enemy class
class Enemy:
    def __init__(self, name, health=50):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            typewrite(Fore.RED + f"{self.name} has been defeated!\n" + Style.RESET_ALL)
        else:
            typewrite(f"{self.name} now has {self.health} health.\n")


# Function for the enemy encounter at the water's edge
# Initialise the enemy with 50 health
def enemy_encounter(player):
    enemy = Enemy("Shadow Beast")
    sword_damage = 25
    enemy_attack_damage = 10

    time.sleep(1)
    print("")
    typewrite("As you stand by the water’s edge, a low growl rumbles from behind you...\n")
    time.sleep(1)
    typewrite("You turn to see a large, shadowy creature emerging from the trees. Its eyes gleam with menace as it prepares to attack!\n")
    time.sleep(1)

    while enemy.health > 0:
        print("")
        typewrite(f"Enemy Health: {enemy.health}\n")
        typewrite(f"Your Health: {player.health}\n")
        print("")

         # Update game state to reflect first enemy encounter
        player.game_state = "first_enemy_encounter"
        player.save_game()  # Auto-save before the first enemy encounter

        typewrite("What would you like to do?")
        print("")
        typewrite("1. Attack with Sword\n")
        typewrite("2. Check Inventory\n")
        typewrite("3. Run away\n")

        choice = input(typewrite("Choose an action: ")).strip()

        if choice == "1":
            # Player attacks with sword
            player.attack(enemy, sword_damage)

            if enemy.health > 0:
                typewrite("The creature snarls in pain but quickly strikes back!\n")
                time.sleep(1)

                # Enemy attacks and player gets to dodge
                while True:
                    print("")
                    typewrite("The creature lunges at you! Quick, dodge!\n")
                    print("")
                    typewrite("1. Dodge left\n")
                    typewrite("2. Dodge right\n")

                    dodge_choice = input(typewrite("Choose your dodge: ")).strip()

                    if dodge_choice == "1":
                        typewrite("You dodge left, narrowly avoiding the creature's claws!\n")
                        break
                    elif dodge_choice == "2":
                        typewrite("You try to dodge right, but the creature catches you with a vicious swipe!\n")
                        player.take_damage(enemy_attack_damage)
                        break
                    else:
                        invalid_input()

        elif choice == "2":
            player.show_inventory()

        elif choice == "3":
            typewrite("You try to run away, but the creature blocks your path!\n")

        else:
            invalid_input()
