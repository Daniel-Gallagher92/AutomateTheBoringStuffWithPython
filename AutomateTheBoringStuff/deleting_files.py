import os

# # permanently deleting single file

# # you can pass relative path if you know you're in that directory, otherwise, specify absolute path

print(os.getcwd()) # you are not in the directory to delete following file, must pass abspath

# os.unlink('/Users/danielgallagher/python/delicious_backup/spamalot.txt') # confirm: deleted spamalot in given dir

# # permanently delete empty folder, WILL NOT WORK IF ANY FILES OR FOLDERS ARE IN FOLDER TO BE DELETED 

# os.rmdir('/Users/danielgallagher/python/delicious/walnut/waffles') # confirm deletion of delicious walnut waffles 

# # permanently delete folder and ALL OF ITS CONTENTS :::DANGER!!::: 

import shutil

# shutil.rmtree('/Users/danielgallagher/python/delicious_backup') # confirm deletion of entire backup folder ;(



# RECOMMENDED: DRY RUN

# os.chdir('/Users/danielgallagher/python/delicious')

# for filename in os.listdir():
#   if filename.endswith('.txt'):
#     #os.unlink(fileName)
#     print(filename) # returns filler2.txt
#                             spam.txt
#                             spamalot.txt
#                             filler.txt
#     If all the returned filenames are the ones you intend to delete, uncomment call to os.link(fileName)

# NOT PERMANENTLY DELETING

# send2trash module sends them to recycling bin

import send2trash

send2trash.send2trash('/Users/danielgallagher/Desktop/learn_struggle_master.jpeg') # confirm via GUI; jpeg image was sent to trash