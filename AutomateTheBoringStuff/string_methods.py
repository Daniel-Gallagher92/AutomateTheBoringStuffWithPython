spam = 'hello world!'

print(spam.upper()) # Returns HELLO WORLD! 

print(spam) # Still prints original string 'hello world!' because strings are immutable and not able to be modified in place

# If you wanted to modify the value permanently you'd have to do something like: 

spam = spam.upper()

print(spam) # Returns HELLO WORLD! and spam now ONLY contains the uppercase string value

# lower() does the opposite and follow the same rules. 

spam = spam.lower()

print(spam) # Returns 'hello world!'