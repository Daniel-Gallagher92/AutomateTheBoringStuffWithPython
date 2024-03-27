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