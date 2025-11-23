print(
    "Welcome to the magic calculator. Please select the following options: A) Addition B) Subtraction C) Multiplication D) Division"  # noqa: E501
)
selection = input("Please input a letter: ")
if selection not in ["A", "B", "C", "D"]:
    print("Wrong letter type, please select A, B, C or D")
else:
    print("What two numbers would you like to work with?")
    Number1 = int(input("Type the first number: "))
    Number2 = int(input("Type the second number: "))
if selection == "A":
    answer = Number1 + Number2
elif selection == "B":
    answer = Number1 - Number2
elif selection == "C":
    answer == Number1 * Number2
elif selection == "D":
    answer = Number1 / Number2

print(answer)
