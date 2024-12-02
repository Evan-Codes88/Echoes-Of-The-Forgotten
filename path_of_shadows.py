import colorama
from colorama import Fore, Style
import json
import time

# Import Typewriter
from typewrite import typewrite
# Import story elements
from player import Player
from enemy import Enemy
from error import invalid_input
from game_utils import save_before_quit

def path_of_shadows(player):
    typewrite("You leave the structure, stepping out into the forest once more. The sun is low on the horizon, casting long shadows across the ground. You set off toward the Path of Shadows, the locket heavy in your pocket...\n")
    time.sleep(1)
    typewrite("The air grows colder, and the trees around you become twisted, almost as if they are watching you. A strange energy fills the air, urging you forward.\n")
    time.sleep(1)

    player.game_state = "second_enemy_encounter"
    player.save_game(silent=True)

    # First enemy encounter
    enemy = Enemy("Shadow Wraith", 60)
    sword_damage = 25
    enemy_attack_damage = 15

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

        if choice == "1":
            player.attack(enemy, sword_damage)

            if enemy.health > 0:
                typewrite("The Shadow Wraith hisses and lashes out with its ethereal claws!\n")
                while True:
                    typewrite("\nThe wraith lunges at you! Quick, dodge!\n")
                    typewrite("1. Dodge left\n")
                    typewrite("2. Dodge right\n")

                    dodge_choice = input(typewrite("Choose your dodge: ")).strip()

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
                        typewrite(Fore.RED + "Please choose '1' to dodge left or '2' to dodge right.\n" + Style.RESET_ALL)

        elif choice == "2":
            player.show_inventory()

        elif choice == "3":
            typewrite("You try to run away, but the wraith blocks your escape!\n")

        else:
            invalid_input()
            typewrite(Fore.RED + "Please choose '1', '2', or '3'.\n" + Style.RESET_ALL)

    if enemy.health <= 0:
        typewrite(Fore.GREEN + "You have defeated the Shadow Wraith!\n" + Style.RESET_ALL)
        # Continue to the next enemy encounter
        third_enemy(player)
    elif player.health <= 0:
        typewrite(Fore.RED + "You have been defeated by the Shadow Wraith...\n" + Style.RESET_ALL)
        return


def third_enemy(player):
    player.game_state = "third_enemy_encounter"
    player.save_game(silent=True)

    typewrite("After defeating the wraith, a strange symbol glows faintly on the path ahead. The locket in your pocket pulses, resonating with the symbol.\n")
    time.sleep(1)
    typewrite("'I'm getting closer,' you whisper to yourself, your heartbeat quickening as you continue down the path.\n")
    
    enemy = Enemy("Shadow Sentinel", 90)
    sword_damage = 30
    enemy_attack_damage = 20

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

        elif choice == "2":
            player.show_inventory()

        elif choice == "3":
            typewrite("You try to run away, but the sentinel blocks your path!\n")

        else:
            invalid_input()
            typewrite(Fore.RED + "Please choose '1', '2', or '3'.\n" + Style.RESET_ALL)

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


def ending():
    typewrite("Thank you for playing!!")
    time.sleep(2)
    quit()