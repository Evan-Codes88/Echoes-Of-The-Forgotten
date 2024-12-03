# Import the 'json' module to handle saving and loading game data in JSON format
import json
# Import the 'typewrite' function from a custom module named 'typewrite,py' to display text with a typewriter effect
from typewrite import typewrite
# Import the 'colorama' package to add coloured text to the console, this enhances user experience
import colorama
# Import specific features from 'colorama' for colour formatting and style resetting
from colorama import Fore, Style


# The Player class represents a player in the game. It manages the player's attributes (name, health, inventory, and game state) and provides methods to interact with the game world, such as taking damage, attacking enemies, managing inventory, and saving/loading the game state.
class Player:
    def __init__(self, name, health=100, game_state="beginning"):
        """
        Purpose: Creates a new player with a name, health, inventory, and game state.
        
        Parameters:
        name (str): The player's name.
        health (int, optional): The starting health of the player, default is 100.
        game_state (str, optional): The current state of the game, default is "beginning".
        
        Returns:
        None. Sets up the player's initial attributes.
        """
        # Holds the player's name, provided when the player is created (variable)
        self.name = name
        
        # Represents the player's health. It is initialized to 100 by default, but can be reduced by taking damage (variable)
        self.health = health
        
        # A dictionary that holds the items the player owns (variable)
        self.inventory = {}
        
        # Represents the current state of the game. For example, it could be "beginning", "midgame", or "endgame". This helps keep track of the player's progress (variable)
        self.game_state = game_state


    def take_damage(self, amount):
        """
        Purpose: Reduces the player's health by the given amount. If health reaches zero or less, the game ends.
        
        Parameters:
        amount (int): The amount of damage the player takes.
        
        Returns:
        None. Prints a message and ends the game if the player's health is zero or below.
        """
        # Reduce the player's health by the given amount
        self.health -= amount

        # Check if the player's health is zero or less
        if self.health <= 0:
            # Print a death message and end the game
            typewrite(Fore.RED + f"{self.name} has died!\n" + Style.RESET_ALL)
            typewrite("Game Over.\n")
            quit()  # Ends the game when the player dies
        else:
            # Print the player's remaining health
            typewrite(f"{self.name} now has {self.health} health.\n")


    def attack(self, enemy, damage):
        """
        Purpose: Perform an attack on an enemy, reducing their health by the given damage amount.
        
        Parameters:
        enemy (object): The enemy being attacked. The enemy must have a `take_damage` method to handle the attack.
        damage (int): The amount of damage to deal to the enemy.
        
        Returns:
        None. The method prints a message about the attack and then reduces the enemy's health using their `take_damage` method.
        """
        # Print a message saying the player is attacking the enemy
        typewrite(Fore.YELLOW + f"{self.name} attacks {enemy.name} for {damage} damage!\n" + Style.RESET_ALL)

        # Call the enemy's 'take_damage' method to reduce their health by the damage amount
        enemy.take_damage(damage)


    def add_item(self, item_name, quantity=1):
        """
        Purpose: Adds an item to the player's inventory. If the item is already in the inventory, it increases the quantity.
        
        Parameters:
        item_name (str): The name of the item to add.
        quantity (int, optional): How many of the item to add (default is 1).
        
        Returns:
        None. A message is printed to confirm the item has been added.
        """
        if item_name in self.inventory:
            self.inventory[item_name] += quantity  # Increase the quantity if the item is already in inventory
        else:
            self.inventory[item_name] = quantity  # Add the item if it's not in the inventory yet
        typewrite(Fore.GREEN + f"{item_name} added to your inventory.\n" + Style.RESET_ALL)


    def show_inventory(self):
        """
        Purpose: Shows the player's inventory and lists the items and their quantities.
        
        Parameters:
        None.
        
        Returns:
        None. Prints the inventory items and quantities, or a message if the inventory is empty.
        """
        if self.inventory:
            typewrite("Your inventory contains:\n")
            for item, quantity in self.inventory.items():
                typewrite(f"- {item}: {quantity}\n")  # Print each item and its quantity
        else:
            typewrite("Your inventory is empty.\n")  # Print message if the inventory is empty


    def save_game(self, filename="savefile.json", silent=False):
        """
        Purpose: Saves the player's information (name, health, inventory, and game state) to a file.
        
        Parameters:
        filename (str, optional): The name of the file where the game will be saved. Defaults to "savefile.json".
        silent (bool, optional): If set to True, no success message will be shown. Defaults to False.
        
        Returns:
        None. It prints a success message if the game is saved successfully or an error message if something goes wrong.
        """
        data = {
            'name': self.name,
            'health': self.health,
            'inventory': self.inventory,
            'game_state': self.game_state
        }
        
        try:
            # Attempt to open the file in write mode ('w') where game data will be saved.
            with open(filename, 'w') as file:
                # The json.dump() function serialises the 'data' dictionary into a JSON format and writes it to the specified file.
                json.dump(data, file)  
            
            # If the file was written successfully, and if 'silent' is not True, display a success message.
            if not silent:
                typewrite(Fore.CYAN + "Game saved successfully!\n" + Style.RESET_ALL)
        
        except Exception as e:
            # If an error occurs during the file writing process, it will be caught here.
            # The exception is stored in the variable 'e', which contains the error message.
            # This block will print an error message to the screen, including details of the error.
            typewrite(Fore.RED + f"Error saving game: {e}\n" + Style.RESET_ALL)


    @classmethod
    def load_game(cls, filename="savefile.json"):
        """
        Purpose: Loads the player's saved game data from a file and creates a Player object with that data.
        
        Parameters:
        filename (str, optional): The name of the file to load the saved game data from. Defaults to "savefile.json".
        
        Returns:
        Player object: A Player object with the loaded data if the file exists and is valid.
        None: If the file doesn't exist or is corrupted, it returns None and prints an error message.
        """
        try:
            # Try to open the file and load the game data
            with open(filename, 'r') as file:
                data = json.load(file)  # Load the data from the file

                # Create a Player object using the data from the file
                player = cls(
                    name=data['name'],
                    health=data['health'],
                    game_state=data['game_state']
                )
                player.inventory = data['inventory']  # Add the loaded inventory to the player object
                return player  # Return the player object with all the loaded data

        except FileNotFoundError:
            # If the file doesn't exist, print an error and return None
            typewrite(Fore.RED + "No saved game found. Starting a new game...\n" + Style.RESET_ALL)
            return None
        except json.JSONDecodeError:
            # If the file is corrupted, print an error and return None
            typewrite(Fore.RED + "Error loading saved game. The file may be corrupted.\n" + Style.RESET_ALL)
            return None
