import webbrowser, sys, pyperclip

# webbrowser.open('https://automatetheboringstuff.com')

sys.argv #['mapit.py', '870', 'Valencia', 'St.']

if len(sys.argv) > 1:
  address = ' '.join(sys.argv[1:])
else:
  address = pyperclip.paste()