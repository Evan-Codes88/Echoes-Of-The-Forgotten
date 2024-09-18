import json
from typewrite import typewrite
import colorama
from colorama import Fore, Back, Style
colorama.init()

# Create a class for the player. This class will store the name, health, game state, and have an empty inventory that can be added to later
class Player:
    def __init__(self, name, health=100, game_state="beginning"):
        self.name = name
        self.health = health
        self.inventory = {}
        self.game_state = game_state  # New game state attribute

    # Reduce the player's health by a certain amount and end the game if health reaches 0
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            typewrite(Fore.RED + f"{self.name} has died!\n" + Style.RESET_ALL)
            typewrite("Game Over.\n")
            quit()  # End the game here to avoid further execution
        else:
            typewrite(f"{self.name} now has {self.health} health.\n")

    def attack(self, enemy, damage):
        typewrite(Fore.YELLOW + f"{self.name} attacks {enemy.name} for {damage} damage!\n" + Style.RESET_ALL)
        enemy.take_damage(damage)

    # Add items to the inventory
    def add_item(self, item_name, quantity=1):
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
        typewrite(Fore.GREEN + f"{item_name} added to your inventory.\n" + Style.RESET_ALL)

    # Display the inventory
    def show_inventory(self):
        if self.inventory:
            typewrite("Your inventory contains:\n")
            for item, quantity in self.inventory.items():
                typewrite(f"{item}: {quantity}\n")
        else:
            typewrite("Your inventory is empty.\n")

    # Save the game to a file
    def save_game(self, filename="savefile.json", silent=False):
        data = {
            'name': self.name,
            'health': self.health,
            'inventory': self.inventory,
            'game_state': self.game_state
        }
        with open(filename, 'w') as file:
            json.dump(data, file)
        
        if not silent:  # Only print if silent is False
            print("Game saved successfully!")

    # Load the game from a file
    @classmethod
    def load_game(cls, filename="savefile.json"):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                player = cls(
                    name=data['name'],
                    health=data['health'],
                    game_state=data['game_state']
                )
                player.inventory = data['inventory']  # Load inventory
                return player
        except FileNotFoundError:
            typewrite(Fore.RED + "No saved game found. Starting a new game...\n" + Style.RESET_ALL)
            return None
