import os

path = os.path.join('folder_1', 'folder_2', 'folder_3', 'file.png')

print(path) # returns folder_1/folder_2/folder_3/file.png with appropriate slashes for mac os

print(os.sep) # stores the separator your os will use

print(os.getcwd()) # returns /Users/danielgallagher/python/automate_the_boring_stuff/AutomateTheBoringStuffWithPython/AutomateTheBoringStuff