import os

path = os.path.join('folder_1', 'folder_2', 'folder_3', 'file.png')

print(path) # returns folder_1/folder_2/folder_3/file.png with appropriate slashes for mac os

print(os.sep) # stores the separator your os will use

print(os.getcwd()) # returns /Users/danielgallagher/python/automate_the_boring_stuff/AutomateTheBoringStuffWithPython/AutomateTheBoringStuff

print(os.chdir('/Users')) #chdir returns NONE although it does change the directory behind the scenes 

print(os.getcwd()) # returns /Users

print(os.chdir('/Users/danielgallagher/python/automate_the_boring_stuff/AutomateTheBoringStuffWithPython/AutomateTheBoringStuff'))

print(os.getcwd()) # returns /Users/danielgallagher/python/automate_the_boring_stuff/AutomateTheBoringStuffWithPython/AutomateTheBoringStuff

print(os.path.abspath('file_path.py')) # returns absolute path of relative file passed in.
# /Users/danielgallagher/python/automate_the_boring_stuff/AutomateTheBoringStuffWithPython/AutomateTheBoringStuff/file_path.py

print(os.path.isabs('AutomateTheBoringStuffWithPython/AutomateTheBoringStuff/file_path.py')) # returns False
# isabs returns boolean value answering if the path passed is indeed an absolute path or not.

print(os.path.relpath('/Users/danielgallagher/python/automate_the_boring_stuff/AutomateTheBoringStuffWithPython/AutomateTheBoringStuff/file_path.py', '/Users/danielgallagher/python'))
# the second arg says "this is the directory we're currently in"
# returns automate_the_boring_stuff/AutomateTheBoringStuffWithPython/AutomateTheBoringStuff/file_path.py

print(os.path.dirname('/Users/danielgallagher/python/automate_the_boring_stuff/AutomateTheBoringStuffWithPython/AutomateTheBoringStuff/file_path.py'))
# returns only directories, no filenames --> /Users/danielgallagher/python/automate_the_boring_stuff/AutomateTheBoringStuffWithPython/AutomateTheBoringStuff

print(os.path.basename('/Users/danielgallagher/python/automate_the_boring_stuff/AutomateTheBoringStuffWithPython/AutomateTheBoringStuff/file_path.py'))
# returns file_path.py aka only the base filename 