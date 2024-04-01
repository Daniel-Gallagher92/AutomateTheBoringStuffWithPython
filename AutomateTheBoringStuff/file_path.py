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

print(os.path.exists('/Users/danielgallagher/python/automate_the_boring_stuff/AutomateTheBoringStuffWithPython/AutomateTheBoringStuff/file_path.py'))
# returns True

print(os.path.exists('/Users/danielgallagher/python/automate_the_boring_stuff/AutomateTheBoringStuffWithPython/AutomateTheBoringStuff/vile_path.py'))
# returns False

print(os.path.isfile('file_path.py')) # returns True

print(os.path.isdir('file_path.py')) # returns False 

print(os.path.isdir('/Users/danielgallagher/python/automate_the_boring_stuff/')) # returns True 

print(os.path.getsize('file_path.py')) # returns 2656 and this number is measured in bytes

print(os.listdir('/Users/danielgallagher/python/automate_the_boring_stuff/AutomateTheBoringStuffWithPython/AutomateTheBoringStuff'))
# returns a list of directories inside of passed arg file path. 
# Think of this as using ls in your terminal 
# returns ['carets_and_dollars.py', 'list_methods.py', 'while_loops.py', 'similarities.py', 'for_loops.py', 'hello_world.py', 'lists.py', 'python_scripts.py', 'for_loops_with_lists.py', 'guessing_game.py', 'phone_and_email_extractor.py', 'greedy_nongreedy.py', 'flow_control.py', 'advanced_string_syntax.py', 'sub_verbose.py', 'my_python_scripts.sh', 'twelveDays.py', 'writing_your_own_functions.py', 'dictionaries.py', 'try_and_except.py', 'sysexit.py', 'data_structures.py', 'python_scripts.sh', 'string_formatting.py', 'character_counting.py', 'file_path.py', 'regular_expressions.py', 'string_methods.py', 'if_else_elif.py', 'dry_guessing_game.py', 'findall.py', 'scope.py']