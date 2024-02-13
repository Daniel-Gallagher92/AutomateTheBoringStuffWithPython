def hello():
  print('Well Hello!')
  print('Hiya!')
  print('HowDEEEE!!!!')
  print('\n')

hello()
hello()
hello()

#new example to include argument within hello function
def hello(name): # For clarity, the variable inside of the function is called a parameter
  print('Well Hello! ' + name)
  print('Hiya! ' + name)
  print('HowDEEEE!!!! ' + name)
  print('\n')

hello('Brittani') #  and the string values seen here are called arguments
hello('Daniel')
hello('Valerie')

#Function calls can be used inside of expressions. Example below
#str and len are both function calls 

print('Hello has ' + str(len('Hello')) + ' letters in it.')
print('\n')
#Return statement example

def plusOne(number):
  return number + 1

newNumber = plusOne(32)

print(newNumber)
print('\n')

#Fun with None!

ham = print()
print(ham) #When this program is run None is printed in the console

print(ham == None) #When this line is run it returns True in the console
print('\n')

#The print function automatically adds a new line character '\n' to the end of each print statement, 
#which prints the next print statement on a new line
#You can alter this behavior with a new keyword argument like end in this example

print("Hello", end='')
print("World")

#So instead of:
# Hello
# World

#Python prints HelloWorld

# When you pass multiple string values to print(), the print function will automatically separate them with a single space character 
print('\n')
print('cat', 'dog', 'mouse') #returns cat dog mouse
print('\n')
print('cat', 'dog', 'mouse', sep='ABC') #returns catABCdogABCmouse
