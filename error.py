# Importing
import colorama
from colorama import Fore, Style
import json
import time
from typewrite import typewrite
from player import Player


# Created a function for the invalid choice to reduce repetition

def invalid_input():
    typewrite("Invalid choice. Try again!")