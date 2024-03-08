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

print('Hello'.upper()) # Returns 'HELLO'

print('Hello'.upper().isupper()) # Returns True

print()
# Other "is" methods 

print('hello'.isalpha()) # Returns True
print('hello123'.isalpha()) #Returns False

print('hello123'.isalnum()) #Returns True

print('23'.isdecimal()) #Returns True

print('   '.isspace()) #Returns True

print('hello world!'.isspace()) #Returns False

#However you can use index to check for spaces

print('hello world!'[5].isspace()) #Returns True

print('This Is Title Case'.istitle()) #Returns True ONLY if EVERY word in string begins with uppercase and is followed by lowercase chars

print('hello world'.title()) # Returns 'Hello World'
print()

# startswith() endswith()

print('Hello world'.startswith('Hello')) #Returns True

print('Hello world'.startswith('H')) #Returns True

print('Hello world'.startswith('ello')) #Returns False

print('Hello world!'.endswith('world!')) #Returns True

print('Hello world!'.endswith('world')) #Returns False since we're missing the exclamation point
print()

# join()

print(', '.join(['cats', 'rats', 'bats'])) # Returns 'cats, rats, bats' instead of 'catsratsbats'

print('\n \n'.join(['cats', 'rats', 'bats'])) #prints them on new lines 

# split()

print('My name is Daniel'.split()) #Returns ['My', 'name', 'is', 'Daniel']

# it automatically splits it on whitespace characters unless passing it a value

print('My name is Daniel'.split('a')) #Returns ['My n', 'me is D', 'niel']

# note: this will remove the argument that is passed. all a's are now gone