raise Exception('This is the helpful error message')

# returns in terminal:
#Traceback (most recent call last):
  #File "/Users/danielgallagher/python/automate_the_boring_stuff/AutomateTheBoringStuffWithPython/AutomateTheBoringStuff/raise_and_except.py", line 1, in <module>
    #raise Exception('This is the helpful error message')
#Exception: This is the helpful error message

def boxPrint(symbol, width, height):
  print(symbol * width)

  for i in range(max(height - 2,0)):
    print(symbol + (' ' * (width - 2)) + symbol) 

  print(symbol * width)


boxPrint('*', 15, 5)


