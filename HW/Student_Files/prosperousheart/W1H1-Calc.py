"""Python Basics Bootcamp Week 1 HW 1 - Simple Calculator
https://github.com/ProsperousHeart/Basics-Boot-Camp/blob/main/HW/Requirements/W1H1-Calc.md

This script allows a user to utilize the command prompt (console)
to do simple computations.

This tool provides options on screen. When user input is received
from command prompt, a certain action will take place.

This script will require that module Math be installed.
However, the initial phase of this will be uploaded to GitHub
with just the bare code as per this training:


This file can not yet be imported as a module with functions
- functions are covered in week 2.

Learn more about documenting python code here:
https://realpython.com/documenting-python-code/
"""

# This section wil allow python file to be run from command line
if __name__ == "__main__":
    """
    This function is only executed if run as a script.
    
    """

    print("Thank you for starting your W1H1-Calc program!\n")

    # Start Loop - want to continue until they decide to quit
    not_done = True
    while not_done:

        # Provide Expected Input Menu
        print("Please make your choice:")
        print("1 - exit")
        print("2 - add numbers")
        print("3 - multiply numbers")
        print("4 - subtract numbers")
        print("5 - divide numbers")

        # Get Response
        usr_input = int(input())        # assuming input always INT

        # Compare User Input & Respond Appropriately
        if usr_input == 1:
            not_done = False
            print("\nThank you, come again! ^_^")
        else:
            print("\nSorry - we do not recognize your input. Please try again.\n")

# everything after this is not run unless it is called on
# (functions covered in week 2)