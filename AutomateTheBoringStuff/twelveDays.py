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

vowelRegex = re.compile(r'[aeiouAEIOU]')

matchedObject = vowelRegex.findall('Robocop eats babyfood')

print(matchedObject) # returns ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o']