# Importing the time module for controlling the speed of the typewriter effect
import time

# Typewriter function -- The purpose of this function is to simulate a typewriter effect by printing each character of the input string one at a time with a slight delay between characters. This can be used to display text gradually, mimicking the effect of someone typing.

def typewrite(string):
# Parameters: string (str): The string to be printed with the typewriter effect. This is the input to the function.

    # Convert the input string into a list of characters
    liststring = list(string)

    # Loop through each character of the string
    for char in liststring:

        # Print the character without a newline, and flush the output immediately
        print(char, end="", flush=True)

         # Pause for 0.035 seconds before printing the next character to create the typewriter effect
        time.sleep(0.035)


    #  Returns: str: An empty string is returned after the string has been printed. The return value is not used as the function's main task is to print the string with the typewriter effect.
    return ""
    