 # Importing
import colorama
from colorama import Fore, Style
import json
import time
from typewrite import typewrite
from player import Player
from error import invalid_input

def explore_deeper_forest(player):
        print("")
        typewrite("You venture deeper into the dense forest. The trees grow more twisted, and the darkness begins to envelop you...\n")

        player.game_state = "deeper_forest"