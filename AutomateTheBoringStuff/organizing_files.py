import shutil

shutil.copy('/Users/danielgallagher/python/automate_the_boring_stuff/AutomateTheBoringStuffWithPython/AutomateTheBoringStuff/organizing_files.py', '/Users/danielgallagher/python/delicious')

# below is an example of renaming the file being copied by adding new filename to end of destination.

shutil.copy('/Users/danielgallagher/python/automate_the_boring_stuff/AutomateTheBoringStuffWithPython/AutomateTheBoringStuff/organizing_files.py', '/Users/danielgallagher/python/delicious/spamalot.txt')

# below is an example of copying an entire folder using the shutil.copytree() function

# shutil.copytree('/Users/danielgallagher/python/delicious', '/Users/danielgallagher/python/delicious_backup')


# NOTE: 

# The following code will move the entire directory of delicious_backup, so the logic that follows will return a FileNotFoundError 
# because the file has been moved and DOES NOT EXIST in delicious_backup when it gets called to move again

import os

source_dir = '/Users/danielgallagher/python/delicious'
destination_dir = '/Users/danielgallagher/python/delicious_backup'

# Check if the destination directory exists
if os.path.exists(destination_dir):
    # Remove the destination directory and its contents
    shutil.rmtree(destination_dir)

# Copy the source directory to the destination directory
shutil.copytree(source_dir, destination_dir)

# Now, you can move the file to the destination directory
# shutil.move('/Users/danielgallagher/python/delicious_backup/spam.txt', '/Users/danielgallagher/python/delicious/spam.txt')

# below is an example of moving and renaming a file to a new location without making a copy

shutil.move('/Users/danielgallagher/python/delicious/spam.txt', '/Users/danielgallagher/python/delicious/walnut/waffles/fresh_spam.txt')
# the first execution moves and renames the file. Running this script multiple times will ALWAYS error out
# because the file can only be moved once, then the file paths must be changed

shutil.move('/Users/danielgallagher/python/delicious/walnut/waffles/fresh_spam.txt', '/Users/danielgallagher/python/delicious/spam.txt')

# after adding this second line, running with first move command commented out will return the file to the original location
# each time you run it now, the file bounces back and forth quickly, resulting in NO CHANGES, but also NO ERROR.

# Be careful with your order of logic when moving files around like this. It's unlikely to happen in the wild, since this exercise just teaches the basics.
# But it's also very easy to overwrite files in this case as well.