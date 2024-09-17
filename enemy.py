# enemy.py

from typewrite import typewrite
import colorama
from colorama import Fore, Style
colorama.init()

class Enemy:
    def __init__(self, name, health=50, damage=5):
        self.name = name
        self.health = health
        self.damage = damage

    def take_damage(self, amount):
        # Reduces the enemy's health by a certain amount
        self.health -= amount
        if self.health <= 0:
            typewrite(Fore.RED + f"{self.name} has been defeated!\n" + Style.RESET_ALL)
        else:
            typewrite(f"{self.name} now has {self.health} health.\n")

    def attack(self, player):
        # Enemy attacks the player
        typewrite(Fore.RED + f"{self.name} attacks {player.name}!\n" + Style.RESET_ALL)
        player.take_damage(self.damage)
