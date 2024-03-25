import re

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group()) # returns Batman 

mo = batRegex.search('The Adventures of Batwoman')
print(mo.group()) # returns Batwoman

mo = batRegex.search('The Adventures of Batwowowowowoman') # returns None since there is no match