import re

# Non regex example of finding a phone number

def isPhoneNumber(text):
  if len(text) != 12:
    return False # not phone number sized
  for i in range(0, 3):
    if not text[i].isdecimal():
      return False #no area code 
    if text[3] != '-':
      return False # missing dash 
  for i in range(4,7):
    if not text[i].isdecimal():
      return False # no first 3 digits
  if text[7] != '-':
    return False # missing second dash
  for i in range(8, 12):
    if not text[i].isdecimal():
      return False # missing last 4 digits 
  return True

print(isPhoneNumber('407-555-1234')) # returns True
print(isPhoneNumber('hello')) # returns False

# Finding a phone number inside of a longer string WITHOUT regex 

message = 'Call me at 407-555-8989 tomorrow, or 407-555-1234 for my office line.'
foundNumber = False #will set true when number is found
for i in range(len(message)):
  chunk = message[i:i+12]
  if isPhoneNumber(chunk):
    print('Phone number found: ' + chunk)
    foundNumber = True
if not foundNumber:
  print('Could not find any phone numbers') 

  # The above function returns:
    # Phone number found: 407-555-8989
    # Phone number found: 407-555-1234
  
# same thing using regex
  
message = 'Call me at 407-555-8989 tomorrow, or 407-555-1234 for my office line.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # look for this pattern of text and compile will return this as a regex object
mo = phoneNumRegex.search(message) #search given string
print('Phone number found: ' + mo.group()) # Print the pattern

# The above function will ONLY return the FIRST match found
