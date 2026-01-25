<a href='http://www.learntocodeonline.com/'><img src='https://github.com/ProsperousHeart/TrainingUsingJupyter/blob/master/IMGs/learn-to-code-online.png?raw=true'></a>

# Business Unit (BU) Ask - Project 1:  Calculator

This is your "homework" - or opportunities to implement what you've been learning.

Your BU has requested a simple calculator. Why not use what they already have?

_The world may never know._

For now, you're mission (should you choose to accept it) is to:

1. create a new python file titled:  `W1H1-Calc.py`

2. make this python file one that can be run from a command line

3. have your command prompt ask for a user's input - use [input()](https://docs.python.org/3/library/functions.html#input)

    - Ask what mathematical operation they would like to run (give them options in your prompt) (consider utilizing [random.choice](https://docs.python.org/3/library/random.html#random.choice) in your code)
    
        ```python
        # example to run from python IDE
        from random import choice
        choice([1, "two", "set", 4])
        ```
    
    - Provide an opportunity for the user to give input on any, all or none of the values
    
        - for sake of time, feel free to use [random.randint](https://docs.python.org/3/library/random.html#random.randint) to provide random inputs for this calculator
        
        - this intention behind this first assignment is to familiarize yourself with the bare minimum basics, but feel free to be as extensive and forward thinking (_"how can I improve my work or anticipate what the 'business unit' may need?"_) as you'd like with this

4. Complete the computation and return the following:

    - initial request
    - final response
    
# Additional Opportunities For Growth

Here are some questions to think about for improving the request from the "Business Unit":

- Will they need to save data? If so, how far back?

    _If more than from most recent run, please note we will be covering this in [week 3](../../Week_3)._

- How might you improve the menu?

- Do they want the ability to use it again until otherwise indicated?