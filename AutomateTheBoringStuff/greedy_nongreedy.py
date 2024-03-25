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