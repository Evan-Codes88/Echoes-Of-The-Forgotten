# Importing
import time

# Typewriter function
def typewrite(string):
    liststring = list(string)
    for char in liststring:
        print(char, end="", flush=True)
        time.sleep(0.035)
    return ""