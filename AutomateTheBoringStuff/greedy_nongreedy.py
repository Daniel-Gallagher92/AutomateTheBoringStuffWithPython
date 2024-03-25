import re

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group()) # returns Batman 