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

atRegexWithRange = re.compile(r'.{1,2}at') # note the use of range stating that we may match one or two characters proceeding 'at' wildcard 
matchList = atRegexWithRange.findall('The cat in the hat sat on a flat mat')
print(matchList) # returns [' cat', ' hat', ' sat', 'flat', ' mat'] note we picked up the 'f' on flat, and the other 3 letter words, some whitespace characters



# Matching everything with dot star pattern .*

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
matchList = nameRegex.findall('First Name: Daniel Last Name: Gallagher')
print(matchList) # returns tuple [('Daniel', 'Gallagher')] since we have 2 or more groups


# greedy and non-greedy matching with .* and .*?

serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
matchList = nongreedy.findall(serve)
print(matchList) # returns ['To serve humans'] since we match the <> chars, we fulfill requirements even if there is another > char later on

greedy = re.compile(r'<(.*)>')
matchList = greedy.findall(serve)
print(matchList) # returns ['To serve humans> for dinner.'] since another > char occurs at the end

# matching EVERYTHING with re.DOTALL second arg

prime = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
dotStar = re.compile(r'.*')
mo = dotStar.search(prime)
print(mo.group()) # Only returns Serve the public trust. since .* alone cannot pick up on newline char

prime = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
dotStar = re.compile(r'.*', re.DOTALL) # note the second arg re.DOTALL
mo = dotStar.search(prime)
print(mo.group())  # returns Serve the public trust.
                           # Protect the innocent.
                           # Uphold the law.

# using the re.DOTALL second arg truly tells the dot char to accept ALL chars including newline chars


# case insensitive search using re.IGNORECASE or re.I for short

vowelRegex = re.compile(r'[aeiou]', re.I) # instead of typing out [aeiouAEIOU] to match upper and lower case
matchList = vowelRegex.findall('Al, why does your programming book talk about Robocop so much?')
print(matchList) # returns ['A', 'o', 'e', 'o', 'u', 'o', 'a', 'i', 'o', 'o', 'a', 'a', 'o', 'u', 'o', 'o', 'o', 'o', 'u'] 
# note the capital A the was included 