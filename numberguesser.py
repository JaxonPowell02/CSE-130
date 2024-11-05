# #Python

# #importing the random function
# import random

# #declaring the play again variable
# play_again = 'yes'

# #first while loop that keeps going as long as the user wants to keep playing
# while play_again.lower() == 'yes':

#     #getting the random number
#     magic_number = random.randint(1,100)

#     #declaring a variable that counts the number of guesses
#     number_of_guesses = 0

#     print('Welcome to the guessing game.')

#     guess = -1

#     #second while loop that keeps going until the user guesses the correct number. 
#     while guess != magic_number:

#         guess = int(input('What is your guess.'))

#         #if statements that print out something different if the number is higher or lower.
#         if guess < magic_number:
#             print('Your guess was to low.')
#             number_of_guesses += 1
#         elif guess > magic_number:
#             print('Your guess was to high.')
#             number_of_guesses += 1 

#     #print statements for when the user guesses the correct number. 
#     print('Congradulations you guess the right number.')
#     print(f'The correct number was {magic_number}')
#     print(f'It took you {number_of_guesses} tries to guess the correct number.')

#     #Asking the user if they want to play again. 
#     play_again = input('Would you like to play again. (yes/no)')

# print('Thanks for playing!')
