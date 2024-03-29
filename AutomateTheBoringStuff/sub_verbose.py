import re

# findall() using \w+ for finding one or more words (names) after 'Agent' 

namesRegex = re.compile(r'Agent \w+')

mo = namesRegex.findall('Agent Alice gave the secret documents to Agent Bob')

print(mo) # returns ['Agent Alice', 'Agent Bob']

# sub() method use case. First arg is what you will SUB in for other words, Second arg is the string you search

mo = namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob')

print(mo) # returns REDACTED gave the secret documents to REDACTED