import re

# findall() using \w+ for finding one or more words (names) after 'Agent' 

namesRegex = re.compile(r'Agent \w+')

mo = namesRegex.findall('Agent Alice gave the secret documents to Agent Bob')

print(mo) # returns ['Agent Alice', 'Agent Bob']

# sub() method use case. First arg is what you will SUB in for other words, Second arg is the string you search

mo = namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob')

print(mo) # returns REDACTED gave the secret documents to REDACTED

# substituting using groups from original text with \1

namesRegex = re.compile(r'Agent (\w)\w*')

mo = namesRegex.sub(r'Agent \1******', 'Agent Alice gave the secret documents to Agent Bob')

# note that the above line passes a raw string. By adding the r prefix to the replacement pattern string,
# you ensure that backslashes are treated as literal characters, allowing \1 to be interpreted correctly.


print(mo) # returns Agent A****** gave the secret documents to Agent B******


# Managing complex regex with multiline string and re.VERBOSE second arg

phoneRegex = re.compile(r'''
(\d\d\d-)|    # Area code without parens, but with a dash
(\(\d\d\d\) ) # |or area code WITH parens and WITHOUt a dash 
(\d\d\d)      # first three digits
-             # dash in main phone number
(\d\d\d\d)    # last four digits in main phone number
\sx\d{2,4}    # if there is an extension, we can match a space followed by 'x' and a number of digits between 2 and 4 chars
''', re.VERBOSE) # this argument is what allows us to make notes on a multiline string for managing complicated regex 


# note how much easier it is to break down and make notes on complicated regex patterns. 