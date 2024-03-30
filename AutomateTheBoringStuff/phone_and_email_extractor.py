#!/bin/zsh python3 

import pyperclip, re


re.compile(r''' 
# 415-555-1234, 515,1234, (415) 555-1234, 555-0000 ext 12345,  555-0000 ext. 12345, ext. 12345, x12345

((\d\d\d)|(\(\d\d\d\)))? # area code (optional)
(\s|-)              # seperator
\d\d\d              # first three digits
-                   # seperator 
\d\d\d\d            # last four digits 
(((ext(\.)?\s)|x)   # extension word-part (optional)
  (\d{2,5}))?       # extension number part (optional)
''', re.VERBOSE)


# todo: create regex for email addresses 

# todo: get the text off of the clipboard

# todo: extract email and phone num's

# todo: copy extracted phone nums and emails to clipboard 

