#In the example below I took the previous version of the game and made it as DRY as possible
# I learned to use the .format() function for string formatting. See gist for more explanation 

import random

def welcome_message(): #asks user's name and the function will return the user's input
    print('Hey there, what\'s your name?\n')
    return input() #the return value of the entire function will come from this line 

# def guess_message(chances):
#     print('You get {} tries. Can you guess what number I\'m thinking of?'.format(chances))
#     print() # Turns out you can use the print() function with an empty arg to create new line!

# def guess_message(chances):
#     if chances == 1:
#         print('1 more chance!')
#     else:
#         print('You get {} tries. Can you guess what number I\'m thinking of?\n'.format(chances))
# #Or you can just insert a \n new line character at the end of existing strings for readability
        
def guess_message(chances):
    message = '1 more chance!' if chances == 1 else 'You get {} tries. Can you guess what number I\'m thinking of?'.format(chances)
    print(message + '\n')
    
def get_guess():
    while True:
        try:
          return int(input('\n'))
        except ValueError:
            print('Please enter a valid number.\n')
            

def remaining_chances(chances):
  if chances == 1:
        print('1 more chance!!!\n')
  else:
        print('{} more chances left.\n'.format(chances - 1))

def play_game():
    print()
    print('Well, {}, I\'m thinking of a number between 1 and 100...\n'.format(myName))
    secretNumber = random.randint(1, 100)
    chances = 6

    guess_message(chances)

    for guessesTaken in range(1, chances + 1): # + 1 added to chances to ensure the proper range is covered
        guess = get_guess()

        if guess < secretNumber:
            print('Your guess is too low\n')
        elif guess > secretNumber:
            print('Your guess is too high\n')
        else:
            print('Congratulations, you guessed the correct number!')
            break

        remaining_chances(chances)
        chances -= 1

    else:
        print('Sorry, you ran out of luck! The number I was thinking of was', secretNumber)

    print('\nYou took', guessesTaken, 'guesses.')

myName = welcome_message()
play_game()
