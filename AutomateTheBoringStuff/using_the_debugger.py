print('Enter the first number to add:')
first = int(input())
print('Enter the second number to add:')
second = int(input())
print('Enter the third number to add:')
third = int(input())
print('The sum of you numbers is: ', first + second + third )

# setting up breakpoints (red dots) and using the debugger showed the input was storing our integers as strings
# and this was returning the 3 numbers string concatenated, not mathematically added 
# by the debugger exposing the data type, this reminds us to store our input as int(input()) to ensure storage as an integer

# Step into
def blahBlahBlah():
  print('blah')
  print('blah')
  print('blah')
  moreBlah() # use Step Into to enter this function call with debugger and Step Out whe you are ready to continue past that function
  print('blah')
  print('blah')
  print('blah')
  print('blah')
  moreBlah() # use Step Over to skip entering this function call 
  print('blah')
  print('blah')

def moreBlah():
  print('more blahs')
  print('more blahs')
  print('more blahs')

print(blahBlahBlah())
