# raise Exception('This is the helpful error message')

# AFTER ALL THIS DEBUGGING AND FINDING NOTHING......
# It turns out the raise Exception line when left in will break the program and nothing else will run
# comment it out and the boxPrint function works!

# returns in terminal:
#Traceback (most recent call last):
  #File "/Users/danielgallagher/python/automate_the_boring_stuff/AutomateTheBoringStuffWithPython/AutomateTheBoringStuff/raise_and_except.py", line 1, in <module>
    #raise Exception('This is the helpful error message')
#Exception: This is the helpful error message

# def boxPrint(symbol, width, height):
#   if len(symbol) != 1:
#     raise Exception('"symbol" needs to be a string of length 1.')
#   if (width < 2 ) or (height < 2):
#     raise Exception('"width" and "height" must be greater or equal to 2.')
  
#   print(symbol * width)

#   for i in range(max(height - 2,0)):
#     print(symbol + (' ' * (width - 2)) + symbol) 

#   print(symbol * width)


# boxPrint('*', 1, 1)


# Getting the Traceback as a String

import traceback

try:
  raise Exception('This is the error message.')
except: 
  errorFile = open('error_log.txt', 'a')
  errorFile.write(traceback.format_exc())
  errorFile.close()
  print('The traceback info was written to error_log.txt')

