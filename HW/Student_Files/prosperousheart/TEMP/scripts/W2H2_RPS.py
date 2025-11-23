# Week 2 Implementation Work:  RPS
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

# ===========================================================
# random is a module we will use to generate a random number
# ===========================================================
import random
from datetime import date  # https://docs.python.org/3/library/datetime.html

# ======================================================================
# create "globals"
# ======================================================================
# date.today() == "YYYY-MM-DD" ==> "YYYYMMDD"
today = "".join(str(date.today()).split("-"))

# ======================================================================
# choices can be updated later to include additional options
# ======================================================================
choices = {1: "rock", 2: "paper", 3: "scissors"}

# =============================================================================
# This section will set up logging. More information on logging found here:
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
# =============================================================================
logging.basicConfig(
    # consider using formatting instead
    filename="PHPBBC-{}.log".format(
        today
    ),  # consider using formatting instead  # noqa: E501
    filemode="w",  # overwrites the file every time
    level=logging.DEBUG,  # lowest logging level
    format="%(asctime)s|%(levelname)s: %(name)s @ %(lineno)d|%(message)s",
)

# setup logging buffer for console
console = logging.StreamHandler()
console.setLevel(logging.WARN)  # all DEBUG or higher will show on console

# set format easy for console to use
formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")
console.setFormatter(formatter)
logging.getLogger(__name__).addHandler(console)
logger = logging.getLogger(__name__)


# ======================================================================
# create a class to be used for a user (or computer) making a "choice"
# Inspired by:  https://stackoverflow.com/a/3694822
#
# This also allows you to grow your options, such as providing a username!
# How would you integrate allowing them to provide their name?
# ======================================================================
class Choice(object):
    """
    This class uses object orientation to wrap "data" in a proper class/obj.

    """

    def __init__(self, start=0):
        """
        This is the constructor function - also known
        as what happens when this class is created.

        """

        logger.debug("Creating new Choice class object...")
        self._choice = start  # could set to None, but we expect this to be INT
        logger.debug("Completed creation of new Choice class object...")

    @property
    def choice(self):
        """
        This function returns the attribute:    choice

        """

        logger.debug("Returning choice attribute data...")
        return self._choice

    @choice.setter
    def choice(self, data):
        """
        This function sets the attribute:   choice

        """
        logger.debug("Checking input ...")
        try:
            data = int(data)
        except ValueError:
            logger.warning("Integer not provided")
            return TypeError("Integer not provided")

        if data not in choices.keys():
            logger.warning("Integer not provided from required input")
            raise ValueError("Please provide a number 1-3")

        logger.debug("Setting Choice class attribute for choice...")
        self._choice = data
        logger.debug("Completed setting Choice class attribute for choice")

    def input(self):
        """
        This function allows user to provide input.
        Assigns response to the choice attribute.

        """

        logger.debug("Requesting input...")
        choice_str = "1 - rock, 2 - paper, 3 - scissors"
        test_bool = True
        while test_bool:
            in_put = input(
                "Please provide your choice ({}):  ".format(choice_str)
            )
            if in_put.isdigit() and int(in_put) in choices.keys():
                test_bool = False
        logger.debug(
            "Correct input received. Returning response:  {}".format(in_put)
        )
        return int(in_put)


def get_user_input():
    """
    This function has no input required, since it will be generating a response
    from the user. This function will only allow a number between 1 and the
    max number of possible options (base is 3), where each number represents
    the choices available and minimizes user error.

    Returns the integer requested.

    """

    logger.debug("Starting get_user_input()...")
    user_obj = Choice()
    user_obj.choice = user_obj.input()
    logger.debug(
        "Ending get_user_input() & returning:  {}".format(user_obj.choice)
    )

    return user_obj.choice


def get_comp_choice():
    """
    This function randomly generates a number between 1 up to and including
    the max number of options. If base, it should be 3. If expanded, it
    will depend on the number of options and logic you have created.

    Returns the integer "chosen" by the computer/randomizer.

    """

    # =====================================================================
    # FOOD FOR THOUGHT:  If we used a class variable for the user's input ...
    # couldn't you create a function in that class to automatically
    # generate the computer response? :-O
    #   - why or why would this NOT be a good idea?
    # =====================================================================

    logger.debug("Starting get_comp_choice()...")
    random_int = random.randint(1, len(choices.keys()))  # nosec
    logger.debug(
        "Ending get_comp_choice() & returning:  {}".format(random_int)
    )
    # pass

    return random_int


def calc_winner(user: int, comp: int):
    """
    This function takes 2 integer inputs user and comp. Utilizing the logic
    of your particular RPS game, it will then choose a winner.

    Returns a dictionary like this:

        {
            'winner': 'user' or 'comp',
            'user': {some integer}
            'comp': {some integer}
        }

    To get fancy, you could create a class to have variables - but no need
    other than for practice.

    """

    def compare(user: int, comp: int):
        """
        Compares values and returns a string of who won.

        From our STEP1-BU-Requirements.md file:

                           1         2          3
                       | ROCK  |   PAPER  | SCISSORS
            1 ROCK     |  tie  |   paper  | rock
            2 PAPER    | paper |    tie   | scissors
            3 SCISSORS |  rock | scissors | tie

        """

        logger.debug("Ending calc_winner()...")
        if user == comp:
            return "N/A - tie"
        elif (
            (user == 1 and comp == 2)
            or (user == 2 and comp == 3)
            or (user == 3 and comp == 1)
        ):
            return "Computer Wins!"
        else:
            return "You win!"

    logger.debug("Starting calc_winner()...")
    dict2rtn = dict()
    dict2rtn["user"] = user
    dict2rtn["comp"] = comp
    logger.debug("Attempting to call compare()...")
    dict2rtn["winner"] = compare(user, comp)
    logger.debug("Ending calc_winner()...")

    return dict2rtn


def print_winner(data_dict: dict):
    """
    This function takes in a dictionary and prints to screen/CLI:
        - who chose what
        - who was the winner

    Input dictionary example:

        {
            'winner': 'user' or 'comp',
            'user': {some integer}
            'comp': {some integer}
        }

    Returns nothing ... unless you add the data to a file.
    Then you could return the filename to allow them to access it's location.

    """

    logger.debug("Starting print_winner()...")
    print(data_dict["winner"], "\n")
    logger.debug("Ending print_winner()...")
    # pass


def prnt_menu():
    menu = "Please select from one of the following menu options:\n"
    menu += "1. Play RPS\n"
    menu += "2. Exit RPS\n"
    return menu


if __name__ == "__main__":
    """
    This function is only executed if run as a script.
    This particular bare bones STEP3 will only utilize base requirements.
    """

    logger.debug("Starting {}()...".format(__name__))

    # keep going until they want to stop
    stop_game = False

    print("Welcome to the latest RPS game!\n")
    while not stop_game:
        user = input(prnt_menu())
        if user not in ["1", "2"]:
            print("Please provide a valid input.\n")
        elif user == "2":
            stop_game = True
            print("OK, thanks for playing!\n")
        else:
            # ==========================================================
            # The functions needed are as follows:
            #   - get user input
            #   - generate choice for computer
            #   - calculate winner
            #   - print winner
            #
            #   NOTE:  Be sure that you ALWAYS check the data returned
            #          This ensures you are getting the excct type of
            #          data expected as well as avoid future bugs.
            #          See "complete.py" for everything.
            # ==========================================================
            user = get_user_input()
            print("You have chosen:\t{}".format(user))
            comp = get_comp_choice()
            print("Computer has chosen:\t{}".format(comp))
            data_dict = calc_winner(user, comp)
            print_winner(data_dict)

    # ================================================
    # Nice to have needs:
    #   - way to store info (database)
    #   - way to retrieve info (to show scoreboard)
    #   - way to email
    #   - expanded logic for additional options
    #   - possibly Jinja2 for a nice HTML look
    #   - ability to play more than once (even if not storing data)
    #   - ability for user to turn on/off debug mode
    # ================================================

    logger.debug("Ending {}()...".format(__name__))
