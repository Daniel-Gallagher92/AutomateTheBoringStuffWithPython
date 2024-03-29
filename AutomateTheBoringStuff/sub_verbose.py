import re

# findall() using \w+ for finding one or more words (names) after 'Agent' 

namesRegex = re.compile(r'Agent \w+')

mo = namesRegex.findall('Agent Alice gave the secret documents to Agent Bob')

print(mo) # returns ['Agent Alice', 'Agent Bob']