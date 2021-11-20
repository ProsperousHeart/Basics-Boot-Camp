<a href='https://www.learntocodeonline.com/'><img src='https://github.com/ProsperousHeart/TrainingUsingJupyter/blob/master/IMGs/learn-to-code-online.png?raw=true'></a>

# Business Unit (BU) Asks - Week 2, Project 2:  Rock Paper Scissors (With Functions)

As of _Nov 18, 2021_ this is still under construction. It is a copy of week 1's assignment #2 and has not yet been updated to reflect the next BU ask.

## Main Requirements

Your business unit has requested that you make a rock, paper, scissors
game that employees' kids can play when they visit their parents.

And they want it done in a month.

That's all they want, have at it.

Well ... great. So let's talk about what's possible.

### Base Needs

Start from ground floor. What are the base requirements of a simple
rock, paper, scissors game?

1. 2 players (at least one requires manual input)
2. there are some number of combinations to create a tie / winner
3. 3 options for each "player" to choose from (rock, paper, scissors)
4. need some way to view the winner

### Additional Requirements

- create a new python file titled:  `W1H2-RPS.py`
- make this python file one that can be run from a command line

## Nice To Have (More Complexity)

What are some things that would make this a better user experience?
- more options (Lizard or Spock, anyone?)
- support for multi-players
- ability to have best X out of Y games
- scoreboard
- ability to email or print result
- visualize the number of games and compare results and losses
- allow user to play multiple times without having to run script each time
    (no database required for this one since you're not storing anything)

# Resources Needed

Python is a given.

Will you need another module to be able to complete something? Like pyxlsx
to create an Excel file, or sqlite3 / mongoDB to create a database?

_Please note - the bootcamp does not cover the above trainings. These are just examples of possiblities._

Gather all requirements beforehand, including any documentation you feel you may need when you're ready to work on those pieces.

## Logic

You will also need to do a logical mapping of winning combinations:

             | ROCK  |   PAPER  | SCISSORS
    ROCK     |  tie  |   paper  | rock
    PAPER    | paper |    tie   | scissors
    SCISSORS |  rock | scissors | tie

If you decide to expand on your options, be sure to redo your logic.

Or leverage your time by using someone else's work like [this fine specimen](https://www.liquidfractal.org/gallery/image/196-rock-paper-scissors-lizard-spock-spider-man-batman-wizard-glock)!

Also, it may benefit you to know [PEP 634 - structural pattern matching](https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching). It is in no way required - everything you've learned so far should be enough to complete this assignment. This is just another option.

**REMEMBER:** there is no 1 right way to code

# Timelines

This is really based on how often the BU wants an update.

## In "The Real World"
 
It is suggested to meet with the "business unit" (at minimum the end user) at least once a week to:
- provide major accomplishments
- share roadblocks

You should also consider having a [daily scrum](https://www.scrum.org/resources/what-is-a-daily-scrum) update with key stakeholders. Takes about 15 minutes
where you and your team meet up to share:
- accomplishments
- what you're working on that day
- any road blocks you may have

This not only keeps your team accountable, but you will have a better grasp
on the situation if you're not meeting deadlines.

## For Our Bootcamp

Work at least 15 minutes a day on this exercise until completed.

Utilize the Discord server or Facebook group when you have questions.