# Week 2 Implementation Work:  Input / Output
# https://github.com/ProsperousHeart/Basics-Boot-Camp/blob/main/HW/Requirements/W3H1-IO.md
#
# Here is the process I follow for this phase (see HW1 Week 2) ...
#
#   1 - write out the comments of expected functions
#   2 - create those functions with proper docstrings, logging, and pass ONLY
#       NOTE:  pass is a null operation (nothing happens) and is therefore
#              only used as a placeholder when no code needs to be executed
#              such as when a function doesn't do anything yet or have logging
#   3 - tie the functions together in your __main__
#   4 - test the logic with print or logging statements
# =============================================================================

# ===========================================================
# module that allows us to do logging in our files
# LIBRARY:  https://docs.python.org/3/library/logging.html
# HOWTO:    https://docs.python.org/3/howto/logging.html
# ===========================================================
import logging

# Additional required Libraries
import re  # https://docs.python.org/3/library/re.html
from datetime import date  # https://docs.python.org/3/library/datetime.html
from pathlib import Path

# ======================================================================
# create "globals"
# ======================================================================
# date.today() == "YYYY-MM-DD" ==> "YYYYMMDD"
today = "".join(str(date.today()).split("-"))

input_file = "../Files/Alice In Wonderland Text.txt"

# =============================================================================
# This section will set up logging. More information on logging can be found here:
#   www.blog.pythonlibrary.org/2012/08/02/python-101-an-intro-to-logging
#   www.digitalocean.com/community/tutorials/how-to-use-logging-in-python3
#   www.loggly.com/ultimate-guide/python-logging-basics
# =============================================================================
#   NOTES:
#       - some of the logging is not consistent throughout ... this is
#           intentional so you can see other ways of leaving breadcrumbs
#           for your future self
#       - as mentioned before, there is no one right way to code, so several
#           different styles have been shared here
#       - logging levels:  https://docs.python.org/3/library/logging.html#logging-levels
# =============================================================================
logging.basicConfig(
    filename="PHPBBCW3-{}.log".format(today),  # consider using formatting instead
    filemode="a+",  # overwrites the file every time
    level=logging.DEBUG,  # lowest logging level
    format="%(asctime)s|%(levelname)s: %(name)s @ %(lineno)d|%(message)s",
)

# setup logging buffer for console
console = logging.StreamHandler()
# console.setLevel(logging.DEBUG)  # all DEBUG or higher will show on console
console.setLevel(logging.WARNING)  # all DEBUG or higher will show on console

# set format easy for console to use
formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")
console.setFormatter(formatter)
logging.getLogger(__name__).addHandler(console)
logger = logging.getLogger(__name__)


def read_n_match(file_in, pttrn):
    """
    Reads in a txt file. Will attempt to match an input pattern,
    and if found add to a list.

    Required inputs:
    : file_in - a txt file to have a pattern matched to lines
    : pattern - a string to match against line in file_in

    Returns a list.

    """

    logger.debug("Starting read_n_match()...")
    lines_list = []
    line_cnt = 0

    try:
        logger.debug("Attempting to read in TXT file:  '{}'".format(file_in))
        with open(file_in, "r") as file_in:
            for line in file_in:
                # str.rstrip([chars])
                line = str.rstrip(line)

                # if pattern in line:
                if re.search(pttrn, line):
                    lines_list.append((str(line_cnt), line))

                line_cnt += 1

    except IOError:
        logger.critical("File does not exist.")

    logger.debug("... Ending read_n_match()")
    return lines_list


def print_to_file(line_list, pttrn, file_name="output.txt"):
    """
    This function will take a list of lines found from read_and_match() function,
    then print to a text file.

    Required inputs:
    : line_list - list of lines returned from read_and_match() function
    : pttrn - text to locate in the file
    : filename_in

    """

    logger.debug("Starting print_to_file()...")
    if file_name[-4:] != ".txt":
        logger.warning("File is not a TXT file!")
        logger.debug("Adding appropriate extension - did not check for others.")
        file_name = file_name + ".txt"

    path = Path(file_name)
    logger.debug("Checking to see if new file or appending...")
    if path.is_file():
        logger.info("File was already created! Adding divider.")
        divider = "\n{}\n\n".format("=" * 69)
    else:
        logger.info("File was not yet created. No divider needed.")
        divider = ""

    with open(file_name, "a+") as output_file:
        logger.debug("Writing to output file ...")
        output_file.write(divider)
        # output_file.write('The pattern you requested was ' + pattern + '\nYour count was:\t ' + str(len(line_list)))
        output_file.write("The pattern you asked to search for is:\t{}\n".format(pttrn))
        output_file.write(
            "The pattern was found in {} lines.\n\n".format(len(line_list))
        )

        output_file.write("*****" * 3 + "\n\n")

        for item in line_list:
            # file_object.write('string')
            output_file.write(item[0] + "\t" + item[1] + "\n")

    print(
        "File created with {} lines found that match '{}'.".format(
            len(line_list), pttrn
        )
    )
    print("Please locate the following in your folder:\n{}".format(file_name))
    # print(file_name)
    logger.debug("... Ending print_to_file()")


# ===================================================================
# 1. read in file - eventually ask for location of file
# 2. search for text phrase
# 3. keep a log file
#     - Have a new file created for each day - no overwrite
#     - Be sure to ALWAYS include the following:
#       - search phrase used
#       - number of times found (if any)
#       - separator for when you have multiple runs
#     - If not found, notate in log file.
#     - If found, notate line number in log file.
# ===================================================================
# Nice to haves:
#   - Ability for user to turn on or off printing line in log file.
#   - Ability to print synopsis of run on CLI
#   - Ability to choose whether capitalization matters
# ===================================================================
if __name__ == "__main__":
    """
    This function is only executed if run as a script.
    It will read in a file, and then attempt to locate a pattern.
    If pattern is found, the line it was found in will be written
    to a txt file.

    """
    logger.debug("Starting {}()...".format(__name__))
    print("You are about to read in:\t{}".format(input_file))
    logger.debug("Searching in:\t{}".format(input_file))

    ptrn2find = input("What pattern would you like to look for?\n")
    logger.debug("Searching for:\t{}".format(ptrn2find))
    print()

    list_of_lines = read_n_match(input_file, ptrn2find)
    print_to_file(list_of_lines, ptrn2find, "PHPBBCW3-{}.txt".format(today))

    logger.debug("Ending {}()...\n".format(__name__))
