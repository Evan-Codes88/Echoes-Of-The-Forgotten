# Importing
import json 
from typewrite import typewrite
import colorama
from colorama import Fore, Back, Style
colorama.init()


# Create a class for the player. This class will store the name, health and have an empty inventory that can be added to later
class Player:
    def __init__(self, name, health=100):
        self.name = name 
        self.health = health 
        self.inventory = {} 


# Create a function that will reduce the players health by a certain amount
    def take_damage(self, amount): 
        self.health -= amount 
        if self.health <= 0:
            typewrite(Fore.RED + f"{self.name} has died!\n" + Style.RESET_ALL) 
        else:
            typewrite(f"{self.name} now has {self.health} health.\n") 

    def attack(self, enemy, damage):
        typewrite(Fore.YELLOW + f"{self.name} attacks {enemy.name} for {damage} damage!\n" + Style.RESET_ALL)
        enemy.take_damage(damage)

    # Create a function that will add items to the inventory. It should also check if there is any of that item currently and add to it
    def add_item(self, item_name, quantity=1): 
            if item_name in self.inventory: 
                self.inventory[item_name] += quantity 
            else:
                self.inventory[item_name] = quantity 
            typewrite(Fore.GREEN + f"{item_name} added to your inventory.\n" + Style.RESET_ALL)

        
    # Create a function that loops through the inventory and displays the items and their quantities    
    def show_inventory(self):
        if self.inventory:
            typewrite("Your inventory contains:\n")
            for item, quantity in self.inventory.items():
                typewrite(f"{item}: {quantity}\n")
        else:
            typewrite("Your inventory is empty.\n")

    # Create a function that will create a dictionary and save the players name, health and inventory. Then print a message that says "Saved successfully"
    def save_game(self, filename="savefile.json"):
        data = {
            'name': self.name,
            'health': self.health,
            'inventory': self.inventory
        }
        with open(filename, 'w') as file:
            json.dump(data, file)
        typewrite(Back.BLUE + Fore.WHITE + "Game saved successfully!\n")


    # This class method will load a save file from the JSON file. It will also check if there is a save file to prevent errors
    @classmethod
    def load_game(cls, filename="savefile.json"):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            player = cls(data['name'], data['health'])
            player.inventory = data['inventory']
            typewrite(f"Game loaded. Welcome back, {player.name}!\n")
            return player
        except FileNotFoundError:
            typewrite("No save file found.\n")
            return cls("Unnamed")