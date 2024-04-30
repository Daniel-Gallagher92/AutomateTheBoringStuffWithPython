import requests, os, pdb

response = requests.get("https://automatetheboringstuff.com/files/rj.txt")

print(response.status_code) # returns 200! Okay!

# .text var will hold large string of the ENTIRE play

print(len(response.text)) # returns 178978 the length of every character in the script



print(response.text[:500]) 

# returns the first 500 characters of the script 

# The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

# This eBook is for the use of anyone anywhere at no cost and with
# almost no restrictions whatsoever.  You may copy it, give it away or
# re-use it under the terms of the Project Gutenberg License included
# with this eBook or online at www.gutenberg.org/license


# Title: Romeo and Juliet

# Author: William Shakespeare

# Posting Date: May 25, 2012 [EBook #1112]
# Release Date: November, 1997  [Etext #1112]

# Language: Eng





# raising an exception if download fails 

badResponse = requests.get("https://automatetheboringstuff.com/asdhufosuhdfoih")

response.raise_for_status() # returns nothing since this was a successful download 
# badResponse.raise_for_status() 

# ALWAYS COMMENT OUT RAISED EXCEPTIONS

# IF YOU RAISE AN EXCEPTION, THE REST OF YOUR PROGRAM WILL NOT EXECUTE

# since the download fails, this exception is returned in the terminal 

# Traceback (most recent call last):
#   File "/Users/danielgallagher/python/automate_the_boring_stuff/AutomateTheBoringStuffWithPython/AutomateTheBoringStuff/requests_exercise.py", line 42, in <module>
#     badResponse.raise_for_status()
#   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/requests/models.py", line 1021, in raise_for_status
#     raise HTTPError(http_error_msg, response=self)
# requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://automatetheboringstuff.com/asdhufosuhdfoih

file_path = os.path.join(os.getcwd(), 'RomeoAndJuliet.txt')
# pdb.set_trace()
playFile = open(file_path, 'wb')
for chunk in response.iter_content(100000):
  playFile.write(chunk)

playFile.close()