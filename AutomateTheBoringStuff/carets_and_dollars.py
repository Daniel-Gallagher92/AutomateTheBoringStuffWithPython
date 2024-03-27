import re 

beginsWithHelloRegex = re.compile(r'^Hello')

matchedObject = beginsWithHelloRegex.search('Hello World!')

print(matchedObject) # returns <re.Match object; span=(0, 5), match='Hello'>

print(beginsWithHelloRegex.search('He says "Hello"') == None) # returns True since the string does NOT BEGIN with Hello