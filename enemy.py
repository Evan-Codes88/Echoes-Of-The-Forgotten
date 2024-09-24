from typewrite import typewrite
import colorama
from colorama import Fore, Style

# Simple Enemy class
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
