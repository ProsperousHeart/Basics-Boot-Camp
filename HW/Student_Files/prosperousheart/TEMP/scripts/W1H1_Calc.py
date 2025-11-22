"""Python Basics Bootcamp Week 1 HW 1 - Simple Calculator
https://github.com/ProsperousHeart/Basics-Boot-Camp/blob/main/HW/Requirements/W1H1-Calc.md

This script allows a user to utilize the command prompt (console)
to do simple computations.

This tool provides options on screen. When user input is received
from command prompt, a certain action will take place.

This script will require that module Math be installed.
However, the initial phase of this will be uploaded to GitHub
with just the bare code -no functions or exception handling.

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

        # ==============================================
        # Get Response:
        # assuming input always INT could introduce bugs
        #           usr_input = int(input())
        # ==============================================

        usr_input = input()

        # Compare User Input & Respond Appropriately
        if usr_input in ["1", "2", "3", "4", "5"]:
            # exit
            if usr_input == "1":
                not_done = False
                print("\nThank you, come again! ^_^")

            # add numbers
            elif usr_input == "2":
                # consider what you would need to do if more than 2 numbers were desired
                add1 = input("\nPlease provide your 1st of 2 numbers:\t")
                add2 = input("Please provide your 2nd of 2 numbers:\t")

                # assuming numbers ONLY provided - will error out and not catch
                print("\n{} + {} = {}\n".format(add1, add2, int(add1) + int(add2)))

            # multiply numbers
            elif usr_input == "3":
                # consider what you would need to do if more than 2 numbers were desired
                add1 = input("\nPlease provide your 1st of 2 numbers:\t")
                add2 = input("Please provide your 2nd of 2 numbers:\t")

                # assuming numbers ONLY provided - will error out and not catch
                print("\n{} * {} = {}\n".format(add1, add2, int(add1) * int(add2)))

            # subtract numbers
            elif usr_input == "4":
                # consider what you would need to do if more than 2 numbers were desired
                add1 = input("\nPlease provide your 1st of 2 numbers:\t")
                add2 = input("Please provide your 2nd of 2 numbers:\t")

                # assuming numbers ONLY provided - will error out and not catch
                print("\n{} - {} = {}\n".format(add1, add2, int(add1) - int(add2)))

            # divide numbers
            elif usr_input == "5":
                # consider what you would need to do if more than 2 numbers were desired
                add1 = input("\nPlease provide your 1st of 2 numbers:\t")
                add2 = input("Please provide your 2nd of 2 numbers:\t")

                # assuming numbers ONLY provided - will error out and not catch
                print("\n{} / {} = {}\n".format(add1, add2, int(add1) / int(add2)))

            # once all items programmed, this section will never be used
            # here to show an option while coding as a "placeholder"
            else:
                print(
                    "\nWARNING:  Your choice has not yet been scripted. Please choose another.\n"
                )
        else:
            print("\nSorry - we do not recognize your input. Please try again.\n")

# everything after this is not run unless it is called on
# (functions covered in week 2)
