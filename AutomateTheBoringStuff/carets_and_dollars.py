import re 

# caret character example for strings that MUST BEGIN with given pattern

beginsWithHelloRegex = re.compile(r'^Hello')

matchedObject = beginsWithHelloRegex.search('Hello World!')

print(matchedObject) # returns <re.Match object; span=(0, 5), match='Hello'>

print(beginsWithHelloRegex.search('He says "Hello"') == None) # returns True since the string does NOT BEGIN with Hello


# dollar sign character example for strings that MUST END with given pattern

endsWithWorldRegex = re.compile(r'world!$')

matchedObject = endsWithWorldRegex.search('Hello world!')

print(matchedObject) # returns <re.Match object; span=(6, 12), match='world!'> 

print(endsWithWorldRegex.search('Hello worldasdasdasdasd!') == None)  # returns True since the string does NOT END with world

allDigitsRegex = re.compile(r'^\d+$')
mo = allDigitsRegex.search('1234567876543245')
print(mo.group()) # returns 1234567876543245 since the string is all uninterrupted digit characters

print(allDigitsRegex.search('123456787xyz6543245') == None) # returns True since the entire string is NOT digits

# wildcard regex character ( . )

atRegex = re.compile(r'.at')
matchList = atRegex.findall('The cat in the hat sat on a flat mat')
print(matchList) # returns ['cat', 'hat', 'sat', 'lat', 'mat'] since the words end with at and can begin with anything