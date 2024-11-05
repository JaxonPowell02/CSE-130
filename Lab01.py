# 1. Name: 
#    Jaxon Powell
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    This program is designed to generate a random number and prompt the user for input
#    to guess the right number until they do guess the right number.
# 4. What was the hardest part? Be as specific as possible.
#    This assignment went well for me, it was something that I was comfortable creating. 
#    I have have made a program that did something very similar,
#    so I have had practice with completing a task similar. 
# 5. How long did it take for you to complete the assignment?
#    Over all this assignment took me 60 minutes to complete. 


# Reflection:

# There wasn't really a hard part with the syntax for me. 
# But one thing that stopped me for a second was rememebr the : after the if and elif statement. 

# I didn't find anything that was particulally hard to solve. 

# I didn't come across any bugs in the program. 

# The thing that I found the most confusing with the instructions
# is what i need to submit and where to put everything. for example. 
# I am putting the reflection here becuase it said that I needed to have a reflection
# but it didn't specify where that should be put.



import random

# Game introduction.
# Give the user instructions as to what he or she will be doing.
instructions = """For this game you will enter a number to decide the difficulty
(the higher the number the more difficult). Once you enter a number you will be prompted
to guess a number. The goal of the game is to guess the number that the computer randomally
generated between 1 and the number that you gave for the difficulty."""

print(f"{instructions}")



# Prompt the user for how difficult the game will be. Ask for an integer.
difficulty = int(input("How difficult do you want the game to be? (Please enter an integer)"))

# Generate a random number between 1 and the chosen value.
value_random = random.randint(1, difficulty)

# Initialize the sentinal and the array of guesses.

guessed_numbers = []

# Play the guessing game.
number_of_guesses = 0
guess = 0

while guess != value_random:

    print(f"The number that you have guessed already are {guessed_numbers}")
    
    # Prompt the user for a number.
    guess = int(input("Please enter a number: "))

        #if statements that print out something different if the number is higher or lower.
    if guess < value_random:
        print('Your guess was to low.')
        number_of_guesses += 1
    else:
        print('Your guess was to high.')
        number_of_guesses += 1 
    print("")

    # Store the number in an array so it can be displayed later.
    guessed_numbers.append(guess)
    # Make a decision: was the guess too high, too low, or just right.

# Give the user a report: How many guesses and what the guesses where.
print(f"Congratulations! You guessed the right number!")
print(f"It took you {len(guessed_numbers)} guesses, and you guessed the numbers: {guessed_numbers}")
print(f"The random number was {value_random}")



