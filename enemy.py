# Import the 'typewrite' function from a custom module named 'typewrite.py' to display text with a typewriter effect
from typewrite import typewrite 
# Import the 'colorama' package to add coloured text to the console, this enhances user experience
import colorama
# Import specific features from 'colorama' for colour formatting and style resetting
from colorama import Fore, Style  

# Simple Enemy class
class Enemy:
    """
    Purpose: Defines an enemy character in the game, which can take damage and track its health.

    Inherits: This class does not inherit from any other class.

    Variables:
    - name (str): The name of the enemy.
    - health (int): The current health of the enemy (default is 50).

    Methods:
    - __init__: Initialises a new enemy with a name and health.
    - take_damage: Reduces the enemy's health by a given amount and prints messages about the enemy's status.
    """

    def __init__(self, name, health=50):
        """
        Purpose: Initialises a new enemy object with a specified name and health.

        Parameters:
        name (str): The name of the enemy.
        health (int, optional): The starting health of the enemy. Default is 50.

        Returns:
        None. Sets up the enemy's name and health.
        """
        self.name = name  # Sets the enemy's name
        self.health = health  # Sets the enemy's health

    def take_damage(self, amount):
        """
        Purpose: Reduces the enemy's health by the specified damage amount.

        Parameters:
        amount (int): The amount of damage to inflict on the enemy.

        Returns:
        None. Prints the updated health or a defeat message if health reaches zero or below.
        """
        self.health -= amount  # Reduces the enemy's health by the damage amount
        if self.health <= 0:  # If the health drops to zero or below
            typewrite(Fore.RED + f"{self.name} has been defeated!\n" + Style.RESET_ALL)  # Print defeat message
        else:
            typewrite(f"{self.name} now has {self.health} health.\n")  # Print updated health message
