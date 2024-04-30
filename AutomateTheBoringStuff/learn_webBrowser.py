# import webbrowser, sys, pyperclip

# # webbrowser.open('https://automatetheboringstuff.com')

# sys.argv #['mapit.py', '870', 'Valencia', 'St.']

# if len(sys.argv) > 1:
#   address = ' '.join(sys.argv[1:])
# else:
#   address = pyperclip.paste()

# webbrowser.open('https://www.google.com/maps/place' + address)

# # all working code and shell scripts are located in MyPythonScripts folder 

# The following code is the working code

# Not included in the course is urllib.parse module.... I've got it to work without it just by adding a forward slash after 'place' in google maps url

import webbrowser, sys, pyperclip, urllib.parse

# webbrowser.open('https://automatetheboringstuff.com')

# sys.argv #['mapit.py', '870', 'Valencia', 'St.']

if len(sys.argv) > 1:
  address = ' '.join(sys.argv[1:])
else:
  address = pyperclip.paste()


# encoded_address = urllib.parse.quote(address)

webbrowser.open('https://www.google.com/maps/place/' + address)