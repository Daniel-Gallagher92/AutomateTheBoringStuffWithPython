import re

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group()) # returns Batman 

mo = batRegex.search('The Adventures of Batwoman')
print(mo.group()) # returns Batwoman

mo = batRegex.search('The Adventures of Batwowowowowoman') # returns None since there is no match

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # compiles the pattern you are looking for 
mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow') # searches given text
print(mo.group()) # returns 415-555-1234 


# To allow the area code to be optional, use the ()? chars

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d') # make sure you include the dash from the area code in your optional search, or else Nonetype error occurs
mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow')
print(mo.group()) # returns 555-1234


# * asterisk character (zero or more) 

batRegex = re.compile(r'Bat(wo)*man') # the star goes where the question mark was and will match the given pattern more than once time like the question mark
mo = batRegex.search('The Adventures of Batman')
print(mo.group()) # returns Batman

batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group()) # returns Batwoman

batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batwowowowowoman')
print(mo.group()) # returns Batwowowowowoman

# + plus character (one or more)

batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adventures of Batman')
print(batRegex.search('The Adventures of Batman') == None) # returns true since batwoman was required and NOT present.

batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group()) # returns Batwoman 

batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adventures of Batwowowowowowoman')
print(mo.group()) # returns Batwowowowowowoman since (wo) appears one or more times


# Escaping characters in RegEx

regex = re.compile(r'\+\*\?')
mo = regex.search('I learned about +*? regex syntax')
print(mo.group()) # returns +*? since we're using escape chars to search for literal symbols

# with grouping

regex = re.compile(r'(\+\*\?)+') # searching with group and plus character to ensure pattern appears one or more times. Mandatory! 
mo = regex.search('I learned about +*?+*?+*?+*?+*?+*? regex syntax')
print(mo.group()) # returns +*?+*?+*?+*?+*?+*? 

# {x} (exactly x number of times)

haRegex = re.compile(r'(ha){3}') # searching for the pattern of the string 'ha' exactly 3 times
mo = haRegex.search('That was a good joke hahaha')
print(mo.group()) # returns hahaha since ha actually occurs 3 times 

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d') #searching for single phone number with or without area code

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?( )?){3}') #searching for 3 phone numbers, with optional area code and with optional comma separating them and with an optional space
mo = phoneRegex.search('My phone numbers are 407-444-1234, 555-6262, 214-678-1234')
print(mo.group()) # returns 407-444-1234, 555-6262, 214-678-1234

# matching a range of possible repetitions

haRegex = re.compile(r'(ha){3,5}') # searching for the pattern of the string 'ha' 3 - 5  times
mo = haRegex.search('That was a good joke hahahaha')
print(mo.group())

haRegex = re.compile(r'(ha){3,5}') # searching for the pattern of the string 'ha' 3 - 5 times
mo = haRegex.search('That was a good joke hahahahaha')
print(mo.group())

digitRegex = re.compile(r'\d{3,5}')
mo = digitRegex.search('1234567890')
print(mo.group()) # returns 12345 because python will always use GREEDY matching by default. 
# python regex starts recognizing patterns as soon as possible. It will always return from the first to max match 
# Greedy matches match the longest possible string that will match the given pattern.

digitRegex = re.compile(r'\d{3,5}?') # the question mark following curly braces returns NON-GREEDY match
mo = digitRegex.search('1234567890')
print(mo.group()) # returns 123 because that is the minimum value given in our range

