spam = 'hello world!'

print(spam.upper()) # Returns HELLO WORLD! 

print(spam) # Still prints original string 'hello world!' because strings are immutable and not able to be modified in place

# If you wanted to modify the value permanently you'd have to do something like: 

spam = spam.upper()

print(spam) # Returns HELLO WORLD! and spam now ONLY contains the uppercase string value

# lower() does the opposite and follow the same rules. 

spam = spam.lower()

print(spam) # Returns 'hello world!'
print()
### these are helpful when it's necessary to make a case insensitive comparison
# Think of a game that asks if you want to play again? 
# print('Would you like to play again?')
# answer = input()

# if answer == 'yes': # The program will break unless the user types exactly 'yes' with that exact casing. 
#   print('Playing again')

# print()

# print('Would you like to play again?')
# answer = input()

# if answer.lower() == 'yes': # Now the program will execute without any issues
#   print('Playing again')

spam = 'hello world!' 
print(spam.islower()) # Returns True since the whole string is lowercase 

spam = 'Hello world!' 
print(spam.islower()) # Returns False since even just one letter is uppercase 

spam = 'HELLO WORLD!'
print(spam.isupper()) # Returns True since the whole string is uppercase 