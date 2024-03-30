#!/bin/zsh python3 

import pyperclip, re

# create regex for phone numbers

phoneRegex = re.compile(r''' 
# 415-555-1234, 515,1234, (415) 555-1234, 555-0000 ext 12345,  555-0000 ext. 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))? # area code (optional)
(\s|-)              # seperator
\d\d\d              # first three digits
-                   # seperator 
\d\d\d\d            # last four digits 
(((ext(\.)?\s)|x)   # extension word-part (optional)
  (\d{2,5}))?       # extension number part (optional)
)
''', re.VERBOSE)


# create regex for email addresses 
emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.com

[a-zA-Z0-9_.+]+          # name part
@                        # @ symbol
[a-zA-Z0-9_.+]+          # domain name part
''',re.VERBOSE)



# todo: copy extracted phone nums and emails to clipboard 

