helloFile = open('/Users/danielgallagher/hello.txt')

print(helloFile.read())

helloFile.close()

# with open('/Users/danielgallagher/hello.txt', 'r') as file:
#     content = file.read()
#     print(content)



import os


# making notes for os module since course changed to pathlib module

# Get the absolute path of the user's home directory
home_directory = os.path.expanduser("~")

# Concatenate the home directory path with the filename
file_path = os.path.join(home_directory, "sonnet29.txt")

# Open the file
sonnetFile = open(file_path)

# Read the lines of the file
lines = sonnetFile.readlines()

# Close the file (recommended)
sonnetFile.close()

# Print the lines
print(lines)

# by using the readlines method, returned, printed in the terminal is the following...
# ["When, in disgrace with fortune and men's eyes,\n", '\n', 'I all alone beweep my outcast state,\n', '\n', 'And trouble deaf heaven with my bootless cries,\n', '\n', 'And look upon myself and curse my fate,\n']

# Opening in Write mode. Pass 'w' as second arg 

# helloFile = open('/Users/danielgallagher/hello.txt', 'w')

# The above line is commented out, but is exactly what you do to write to a file. 

# The below code, error handling is used to ensure a message is returned to prove the code works as expected 

file_path = '/Users/danielgallagher/hello.txt'

try:
    # Open the file in write mode
    with open(file_path, 'w') as hello_file:
        # Write content to the file
        hello_file.write("Hello, world!")
        hello_file.close()

    print("Content has been successfully written to the file.")
except Exception as e:
    print(f"An error occurred: {e}")

    # returns Content has been successfully written to the file.



# Append Mode example using F-Strings 
    
file_path = '/Users/danielgallagher/hello.txt'

try:
    # Open the file in append mode
    with open(file_path, 'a') as hello_file:
        # Write content to the file
        hello_file.write("Hello, world!\n")  # Adding a newline character to separate lines
        hello_file.close()

    print("Content has been successfully appended to the file.")
except Exception as e:
    print(f"An error occurred: {e}")

    # Returns Content has been successfully appended to the file.

# write method to pass an arg to be written to file
    
helloFile = open('/Users/danielgallagher/hello2.txt', 'w')
helloFile.write('HeyHiHellooo!!!!')
helloFile.close()

# Saving Variables with the shelve Module

import shelve

shelfFile = shelve.open('mydata') # on OS X this will create a file called mydata.db in cwd
shelfFile['cats'] = ['Noodle', 'Fatso', 'Ding-Dong', 'Zophie']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'])  # returns ['Noodle', 'Fatso', 'Ding-Dong', 'Zophie']
shelfFile.close()


# Working with shelf file keys and values methods 
shelfFile = shelve.open('mydata') # you must reopen the file to interact with this 
print(list(shelfFile.keys())) # returns ['cats']
print(list(shelfFile.values())) # returns [['Noodle', 'Fatso', 'Ding-Dong', 'Zophie']]


helloFile = open('/Users/danielgallagher/hello2.txt', 'a')
helloFile.write('\nHeyHiHellooo!!!!')
helloFile.close()

helloFile = open('/Users/danielgallagher/hello2.txt', 'r')
content = helloFile.read()
helloFile.close()
print(content)

helloFile = open('/Users/danielgallagher/hello2.txt', 'a')
helloFile.write('\nBacon is not a vegetable.')
helloFile.close()

print('\n')

helloFile = open('/Users/danielgallagher/hello2.txt', 'r')
content = helloFile.read()
helloFile.close()
print(content)