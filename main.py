import colorama
from colorama import Fore, Style
colorama.init()
import json
import time
from typewrite import typewrite
from player import Player
from enemy import Enemy
from game_utils import save_before_quit
from error import invalid_input
from first_enemy import enemy_encounter, post_enemy_story
from deeper_forest import explore_deeper_forest
from investigate_structure import investigate_structure, castle
from path_of_shadows import path_of_shadows, third_enemy, final_revelation

# Function for the opening sequence
def opening_sequence():
    time.sleep(2)
    print("")
    typewrite("You awaken in a dense forest, the sunlight barely piercing the thick canopy above...\n")
    time.sleep(1)
    typewrite("A sword lies beside you, and sounds of creatures echo in the distance...\n")
    time.sleep(1)
    typewrite("You have no memory of who or where you are...\n")
    time.sleep(1)
    typewrite("As you pick up the sword, you notice a name is engraved in the hilt...\n")
    print("")
    time.sleep(0.5)
    name = input(typewrite("What name is engraved in the sword? "))
    return name

# Function to start a new game
def start_new_game():
    player_name = opening_sequence()
    player = Player(player_name)
    
    print("")
    typewrite(f"Ahhh... your name must be {player_name}\n")
    
    player.game_state = "found_name"
    player.save_game(silent=True)  # Auto-save after finding the sword

    time.sleep(0.5)
    typewrite("You stand up and sheath the sword at your side.\n")
    time.sleep(1)
    print("")
    
    player.add_item("Sword", 1)
    print("")
    time.sleep(1)
    typewrite("A strange sense of familiarity washes over you, as though you’ve been here before...\n")
    time.sleep(0.5)

    typewrite("What would you like to do?\n")
    time.sleep(1)

    while True:
        print("")
        typewrite("1. Explore your surroundings\n")
        typewrite("2. Check inventory\n")
        typewrite("3. Rest\n")
        typewrite("4. Quit the game\n")

        choice = input(typewrite("Choose an action: ")).strip()

        if choice == "1":
            explore(player)
        elif choice == "2":
            player.show_inventory()
        elif choice == "3":
            typewrite("You lay down and close your eyes, falling asleep almost instantly...\n")
            time.sleep(2)
            typewrite("You wake up from your rest... What would you like to do?\n")
            print("")
        elif choice == "4":
            save_before_quit(player)
            break
        else:
            invalid_input()

    game_loop(player)

# Function to load a saved game
def load_game():
    player = Player.load_game()
    if player:
        typewrite(f"Welcome back, {player.name}!\n")
        game_loop(player)  # Resume the game from the player's last saved point
    else:
        typewrite("No saved game found. Starting a new game...\n")
        start_new_game()

# Central game loop
def game_loop(player):
    # Function to handle game state based on the loaded game state
    def resume_game(player):
        if player.game_state == "first_enemy_encounter":
            enemy_encounter(player)
        elif player.game_state == "post_enemy_story":
            post_enemy_story(player)
        elif player.game_state == "investigating_structure":
            investigate_structure(player)
        elif player.game_state == "exploring_forest":
            explore_deeper_forest(player)
        elif player.game_state == "found_locket":
            enemy_encounter(player)
        elif player.game_state == "solved_puzzle":
            castle(player)
        elif player.game_state == "second_enemy_encounter":
            path_of_shadows(player)
        elif player.game_state == "third_enemy_encounter":
            third_enemy(player)
        elif player.game_state == "final_revelation":
            final_revelation(player)
        else:
            explore(player)

    # Call resume_game to handle the loaded game state
    resume_game(player)

# Function for exploring the surroundings
def explore(player):
    print("")
    typewrite("You're standing in the heart of a dense, mysterious forest. The air is thick with the smell of moss and damp earth, while towering trees with gnarled, twisted trunks rise high above, their leaves forming a canopy that blocks out most of the sunlight...\n")
    time.sleep(1)
    typewrite("To your left, you can make out the faint outline of an overgrown path. \nTo your right, the trees form a near-impenetrable wall, and the faint sound of rushing water can be heard.\n")
    time.sleep(1)
    typewrite("Which way would you like to go?\n")

    while True:
        typewrite("1. Go left\n")
        typewrite("2. Go right\n")
        typewrite("3. Show Inventory\n")
        typewrite("4. Quit the game\n")

        choice2 = input(typewrite("Choose an action: ")).strip()

        if choice2 == "1":
            print("")
            typewrite("You push through the dense forest along the path. The sound of running water seems to be getting further away.\n")
            time.sleep(1)
            typewrite("What would you like to do?\n")

            while True:
                print("")
                typewrite("1. Continue forward\n")
                typewrite("2. Go back\n")

                choice3 = input(typewrite("Choose an action: ")).strip()

                if choice3 == "1":
                    continue_forward(player)
                    break
                elif choice3 == "2":
                    return
                else:
                    invalid_input()

        elif choice2 == "2":
            right_to_water(player)
            break
        elif choice2 == "3":
            player.show_inventory()
        elif choice2 == "4":
            save_before_quit(player)
            break
        else:
            invalid_input()

# Function to go forward into the forest
def continue_forward(player):
    player.game_state = "continue_forward"
    player.save_game(silent=True)

    print("")
    typewrite("You decide to continue forward, away from the sound of the water. The forest thickens around you, the trees growing more twisted and gnarled as the sunlight fades behind the dense canopy...\n")
    time.sleep(1)
    typewrite("With every step, the air grows colder, and an eerie silence descends, broken only by the occasional snap of a twig underfoot.\n")
    time.sleep(1)
    typewrite("Suddenly, you feel the ground beneath you soften, your boots sinking slightly into the mud. Strange, you think—the ground was dry just moments ago.\n")
    time.sleep(1)
    typewrite("You push forward, but soon, the smell of damp earth overwhelms your senses, and the sound of rushing water—now louder than before—returns, this time directly ahead of you.\n")
    time.sleep(1)
    typewrite("Confused, you break through the dense brush and find yourself at a riverbank.\n")
    time.sleep(0.5)
    typewrite("How is this possible? You were walking in the opposite direction...\n")
    time.sleep(1)
    typewrite("You feel a strange pull toward the river, as though it was calling you back.\n")
    time.sleep(1)
    typewrite("At the water’s edge, a glimmer catches your eye—a small, ornate locket half-submerged in the mud. You kneel down to investigate.\n")
    time.sleep(1)
    typewrite("As your fingers brush against the cold metal, a flood of memories rushes through your mind—faces, places, and voices long forgotten.\n")
    time.sleep(0.5)
    typewrite('"This locket… it feels familiar."\n')
    typewrite("You open it to reveal a faded photograph inside. It’s you... but there's another person beside you, their face scratched out.\n")
    time.sleep(0.5)
    typewrite("A voice echoes in your mind, faint but unmistakable: 'Find me.'\n")
    time.sleep(0.5)
    typewrite("Shaken, you pocket the locket, realizing that the truth lies with the person in the photograph.\n")
    time.sleep(0.5)
    print("")
    player.add_item("Locket")
    player.game_state = "found_locket"
    player.save_game(silent=True)
    enemy_encounter(player)  # Start the enemy encounter after finding the locket

# Function for going towards the water
def right_to_water(player):
    print("")
    typewrite("You carefully step onto the overgrown path. As you weave through the trees, step over branches, and duck under vines, you hear the sound of rushing water becoming louder...\n")
    time.sleep(1)
    typewrite("Eventually, the trees open up to reveal a shimmering river, its surface reflecting the light filtering through the canopy. At the river’s edge, half-submerged in the mud, you spot something gleaming faintly.\n")
    time.sleep(1)
    typewrite("You kneel down to investigate and pull out a small, ornate locket.\n")
    time.sleep(0.5)
    typewrite("The moment your fingers touch the cold metal, a rush of memories floods your mind...\n")
    time.sleep(1)
    typewrite("This locket... it feels familiar.\n")
    time.sleep(1)
    typewrite("You open it to reveal a faded photograph inside, but the face beside yours has been scratched out...\n")
    time.sleep(0.5)
    typewrite("A voice echoes in your mind, faint but unmistakable: 'Find me.'\n")
    time.sleep(0.5)
    player.add_item("Locket")
    player.game_state = "found_locket"
    player.save_game(silent=True)
    enemy_encounter(player)  # Start the enemy encounter after finding the locket

# Main entry point
if __name__ == "__main__":
    print("")
    typewrite("Welcome to Silent Hollow!\n")
    time.sleep(1)

    while True:
        typewrite("1. Start a new game\n")
        typewrite("2. Load a saved game\n")
        typewrite("3. Quit the game\n")

        choice = input(typewrite("Choose an action: ")).strip()

        if choice == "1":
            start_new_game()
            break
        elif choice == "2":
            load_game()
            break
        elif choice == "3":
            print("")
            typewrite("Thanks for playing! Goodbye!\n")
            break
        else:
            invalid_input()
