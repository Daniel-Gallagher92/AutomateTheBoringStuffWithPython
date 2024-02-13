def div42by(divideBy):
  try:
    return 42 / divideBy
  except ZeroDivisionError:
    print('Error: You tried to divide by zero.')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1)) 
print('\n')
#Or you can choose to have a simple except statement that will catch all errors and move past them.

def div42by(divideBy):
  try:
    return 42 / divideBy
  except:                 # <------------ no specified error
    print('Error: You tried to divide by zero.')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

#This code could be useful for Input Validation

print('How many pets do you have?')
numPets = input()
try:
  if int(numPets) >= 4:
    print('That\'s a lot of aminals!')
  elif int(numPets) < 0: # This line detects negative numbers and returns a more clear message to user
    print('You can\'t have negative pets, ya goof!')
  elif int(numPets) == 0: # This line detects lonely people ;(
    print('Aww, maybe you could use a pal?')
  else:
    print('That\'s not that many pets')
except ValueError:
  print('Please enter a valid number')