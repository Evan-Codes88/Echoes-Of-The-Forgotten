import json
from typewrite import typewrite
import colorama
from colorama import Fore, Style

class Player:
    def __init__(self, name, health=100, game_state="beginning"):
        self.name = name
        self.health = health
        self.inventory = {}
        self.game_state = game_state  # Store the player's current game state

    # Method to reduce the player's health and handle death
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            typewrite(Fore.RED + f"{self.name} has died!\n" + Style.RESET_ALL)
            typewrite("Game Over.\n")
            quit()  # Terminate the game when health reaches zero
        else:
            typewrite(f"{self.name} now has {self.health} health.\n")

    # Method for attacking an enemy
    def attack(self, enemy, damage):
        typewrite(Fore.YELLOW + f"{self.name} attacks {enemy.name} for {damage} damage!\n" + Style.RESET_ALL)
        enemy.take_damage(damage)

    # Method to add items to the player's inventory
    def add_item(self, item_name, quantity=1):
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
        typewrite(Fore.GREEN + f"{item_name} added to your inventory.\n" + Style.RESET_ALL)

    # Method to show the player's inventory
    def show_inventory(self):
        if self.inventory:
            typewrite("Your inventory contains:\n")
            for item, quantity in self.inventory.items():
                typewrite(f"- {item}: {quantity}\n")
        else:
            typewrite("Your inventory is empty.\n")

    # Method to save the game state to a JSON file
    def save_game(self, filename="savefile.json", silent=False):
        data = {
            'name': self.name,
            'health': self.health,
            'inventory': self.inventory,
            'game_state': self.game_state  # Save the player's current game state
        }
        try:
            with open(filename, 'w') as file:
                json.dump(data, file)
            if not silent:
                typewrite(Fore.CYAN + "Game saved successfully!\n" + Style.RESET_ALL)
        except Exception as e:
            typewrite(Fore.RED + f"Error saving game: {e}\n" + Style.RESET_ALL)

    # Load the game from a file
    @classmethod
    def load_game(cls, filename="savefile.json"):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                player = cls(
                    name=data['name'],
                    health=data['health'],
                    game_state=data['game_state']  # Load saved game state
                )
                player.inventory = data['inventory']  # Load inventory
                return player
        except FileNotFoundError:
            typewrite(Fore.RED + "No saved game found. Starting a new game...\n" + Style.RESET_ALL)
            return None
        except json.JSONDecodeError:
            typewrite(Fore.RED + "Error loading saved game. The file may be corrupted.\n" + Style.RESET_ALL)
            return None
