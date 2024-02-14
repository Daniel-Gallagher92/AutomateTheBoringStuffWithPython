#In the example below I took the previous version of the game and made it as DRY as possible
# I learned to use the .format() function for string formatting. See gist for more explanation 

import random

def print_welcome_message(): #asks user's name and the function will return the user's input
    print('Hey there, what\'s your name?')
    return input() #the return value of the entire function will come from this line 

def print_guess_message(chances):
    print('You get {} tries. Can you guess what number I\'m thinking of?'.format(chances))
    print()

def get_guess():
    return int(input())

def print_remaining_chances(chances):
    if chances > 1:
        print('{} more chances left.'.format(chances - 1))
    elif chances == 1:
        print('Only 1 more chance!!!')
    print()

def play_game():
    print('Well, {}, I\'m thinking of a number between 1 and 100...'.format(myName))
    print()
    secretNumber = random.randint(1, 100)
    chances = 6

    for guessesTaken in range(1, chances + 1):
        print_guess_message(chances)
        guess = get_guess()

        if guess < secretNumber:
            print('Your guess is too low')
        elif guess > secretNumber:
            print('Your guess is too high')
        else:
            print('Congratulations, you guessed the correct number!')
            break

        print_remaining_chances(chances)
        chances -= 1
    else:
        print('Sorry, you ran out of luck! The number I was thinking of was', secretNumber)

    print('\nYou took', guessesTaken, 'guesses.')

myName = print_welcome_message()
play_game()
