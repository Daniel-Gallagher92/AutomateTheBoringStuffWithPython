# print('Enter the first number to add:')
# first = int(input())
# print('Enter the second number to add:')
# second = int(input())
# print('Enter the third number to add:')
# third = int(input())
# print('The sum of you numbers is: ', first + second + third )

# # setting up breakpoints (red dots) and using the debugger showed the input was storing our integers as strings
# # and this was returning the 3 numbers string concatenated, not mathematically added 
# # by the debugger exposing the data type, this reminds us to store our input as int(input()) to ensure storage as an integer

# # Step into
# def blahBlahBlah():
#   print('blah')
#   print('blah')
#   print('blah')
#   moreBlah() # use Step Into to enter this function call with debugger and Step Out whe you are ready to continue past that function
#   print('blah')
#   print('blah')
#   print('blah')
#   print('blah')
#   moreBlah() # use Step Over to skip entering this function call 
#   print('blah')
#   print('blah')

# def moreBlah():
#   print('more blahs')
#   print('more blahs')
#   print('more blahs')

# print(blahBlahBlah())

# # Step Out will execute the rest of that function and return to the next piece of code in line to execute

# Breakpoint exercise 

import random

heads = 0 

for i in range (1,1000):
  if random.randint(0,1) == 1:
    heads += 1
  if i == 500:
    print('Halfway there!') # Setting a breakpoint here allows us to skip 500 iterations of that loop to measure the performance.

print('Heads came up ' + str(heads) + ' times.')