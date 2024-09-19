# Importing
import colorama
from colorama import Fore, Style
import json
import time
from typewrite import typewrite
from player import Player
from error import invalid_input

def investigate_structure(player):
        print("")
        typewrite("You walk cautiously toward the crumbling stone structure. The air grows colder, and you feel the weight of something watching you.\n")

        player.game_state = "investigating_structure"