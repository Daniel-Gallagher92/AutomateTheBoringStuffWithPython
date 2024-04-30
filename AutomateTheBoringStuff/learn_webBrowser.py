import webbrowser, sys, pyperclip

# webbrowser.open('https://automatetheboringstuff.com')

sys.argv #['mapit.py', '870', 'Valencia', 'St.']

if len(sys.argv) > 1:
  address = ' '.join(sys.argv[1:])
else:
  address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place' + address)

# all working code and shell scripts are located in MyPythonScripts folder 

