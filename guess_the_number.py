"""
The code is a Python program for a "Guess the Number"
game where the player selects a difficulty level and tries to guess
a randomly generated number within a certain number of attempts.
Returns:
    int: A random number between 1 and 100.
"""

from random import randrange


def generate_random():
    """Function generating a random number between 1 and 100"""
    guess = randrange(1, 101)
    return guess


answer = generate_random()

print("Welcome to the Guess the Number game! Let's get started.")
print("I'm thinking of a number between 1 and 100.")
print("Please select the Difficulty level:")
print("(1): Easy ( 10-chances)")
print("(2): Medium ( 5-chances)")
print("(3): Hard ( 3-chances)")

while True:
    try:
        select = int(input("Enter your choice (1,2,3):"))
        if select in [1, 2, 3]:
            break
        else:
            print("Error: Enter a valid option (1,2,3).")
    except ValueError:
        print("Error: Please enter a number (1,2,3).")


def check_result(x, y):
    """
    Checks the player's guess against the correct answer.

    Args:
        x (int): The player's guessed number.
        y (int): The current attempt number.

    Returns:
        bool: True if the guess is correct, False otherwise.
    """
    if answer == x:
        print(f"Congratulations! You guessed the correct number "
              f"in {y} attempts.")
        return True
    elif answer > x:
        print(f"Incorrect! The number is greater than {x}")
    elif answer < x:
        print(f"Incorrect! The number is less than {x}")


if select == 1:
    print("Great! You have selected Easy (10-chances) difficulty level.")
    print("Let's start the game!")
    easy = 10
    for i in range(easy):
        numb = int(input("Enter your guess:"))
        result = check_result(numb, i)
        if result is True:
            break
    print("The Correct number was: ", answer)
elif select == 2:
    print("Great! You have selected Medium (5-chances) difficulty level.")
    print("Let's start the game!")
    Medium = 5
    for i in range(Medium):
        numb = int(input("Enter your guess:"))
        Result = check_result(numb, i)
        if Result is True:
            break
    print("The Correct number was: ", answer)
elif select == 3:
    print("Great! You have selected Hard (3-chances) difficulty level.")
    print("Let's start the game!")
    hard = 3
    for i in range(hard):
        numb = int(input("Enter your guess:"))
        Result = check_result(numb, i)
        print("debug: Result=", Result)
        if Result is True:
            break
    print("The Correct number was: ", answer)
else:
    print("Error: Enter a valid option(1,2,3).")
