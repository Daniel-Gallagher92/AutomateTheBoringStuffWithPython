import requests

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





