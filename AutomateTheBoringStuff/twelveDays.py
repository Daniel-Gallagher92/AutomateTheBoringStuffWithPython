import re

lyrics = '''
12 drummers drummin'
11 pipers pipin'
10 lords a leapin'
9 ladies dancin'
8 maids milkin'
7 swans a swimmin'
6 geese a layin'
5 golden rings!
4 calling birds
3 french hens
2 turtle doves
And 1 partridge in a pear tree!
'''

xmasRegex = re.compile(r'\d+\s\w+') # \d for numeric digits 0-9, \s for space, \w for any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)

matchedObject = xmasRegex.findall(lyrics)

print(matchedObject)

# Creating your own custom regex using square bracket syntax 

# Note that inside the square brackets, the normal regular expression symbols are not interpreted as such.
# This means you do not need to escape the ., *, ?, or () characters with a preceding backslash.

vowelRegex = re.compile(r'[aeiouAEIOU]')

matchedObject = vowelRegex.findall('Robocop eats babyfood')

print(matchedObject) # returns ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o']


# matching two characters in a row with curly brace syntax 

vowelRegex = re.compile(r'[aeiouAEIOU]{2}') # add curly brace with x num of sequential occurrences to search for

matchedObject = vowelRegex.findall('Robocop eats babyfood')

print(matchedObject) # returns ['ea', 'oo'] from 'eats babyfood' 

# negative character classes

# now we search for everything that is NOT a vowel including punctuation marks, spaces and digits

consonantsRegex = re.compile(r'[^aeiouAEIOU]') # Note the caret char immediately after opening square bracket

matchedObject = consonantsRegex.findall('Robocop eats babyfood')

print(matchedObject) # returns ['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', 'f', 'd'] aka everything that is NOT a vowel