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

    print("Content has been successfully written to the file.")
except Exception as e:
    print(f"An error occurred: {e}")
