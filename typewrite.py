# Importing the time module for controlling the speed of the typewriter effect
import time

"""
Typewriter function -- The purpose of this function is to simulate a typewriter effect by printing each character of the input string one at a time with a slight delay between characters. This can be used to display text gradually, mimicking the effect of someone typing.
"""

def typewrite(string):
    """
    Parameters:
    string (str): The string that will be printed with the typewriter effect.
    """
    # Convert the input string into a list of characters so each character can be processed individually
    liststring = list(string)

    # Loop through each character in the list
    for char in liststring:

        # Print the current character without adding a newline, and flush the output to immediately display it
        print(char, end="", flush=True)

        # Pause for 0.035 seconds before printing the next character to simulate the typewriter effect
        time.sleep(0.035)

    # Return an empty string as the function's main purpose is to print the text, not to return anything meaningful
    return ""
