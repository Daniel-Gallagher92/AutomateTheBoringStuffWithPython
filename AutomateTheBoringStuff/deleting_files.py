import os

# permanently deleting single file

# you can pass relative path if you know you're in that directory, otherwise, specify absolute path

print(os.getcwd())

os.unlink('/Users/danielgallagher/python/delicious_backup/spamalot.txt')

# permanently delete empty folder, WILL NOT WORK IF ANY FILES OR FOLDERS ARE IN FOLDER TO BE DELETED 

os.rmdir('/Users/danielgallagher/python/delicious/walnut/waffles')

# permanently delete folder and ALL OF ITS CONTENTS :::DANGER!!::: 

import shutil

shutil.rmtree('/Users/danielgallagher/python/delicious_backup')