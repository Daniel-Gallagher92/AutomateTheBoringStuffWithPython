import random

print('Hey there, what\'s your name?')
myName = input()
print('\n')

print('Well, ' + myName + ' I\'m thinking of a number between 1 and 100...')
print('\n')

chances = 6

print('You get ' + str(chances) + ' tries. Can you guess what number I\'m thinking of?')
print('\n')
secretNumber = random.randint(1,100)

for guessesTaken in range(1,7):
  print('\n')
  guess = int(input()) #input() always returns a string so you must convert to int() to properly compare

  if guess < secretNumber:
    print('Your guess is too low')
    if chances > 1:
      print(str(chances - 1) + ' more chances left.')
    elif chances == 1:
      print('Only 1 more chance!!!')
    chances -= 1
    print('\n')
  elif guess > secretNumber:
    print('Your guess is too high')
    if chances > 1:
      print(str(chances - 1) + ' more chances left.')
    elif chances == 1:
      print('Only 1 more chance!!!')
    chances -= 1
    print('\n')
    
  else: # The only other condtion is if they correctly guess num, in which case we will break out of the loop
    break

if guess != secretNumber:
  print('Sorry, you ran out of luck! The number I was thinking of was ' + str(secretNumber))
  print('\n')

print('\n')
print('You took ' + str(guessesTaken) + ' guesses.')
