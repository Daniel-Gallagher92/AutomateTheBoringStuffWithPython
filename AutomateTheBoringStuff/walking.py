import os


for folderName, subfolders, filenames in os.walk('/Users/danielgallagher/python/delicious'):
  print('The folder is ' + folderName)
  print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
  print('The filenames in ' + folderName + ' are: ' + str(filenames))
  print()


# the code below will check if any subfolders are named Eggs, and if so, delete them. 
  #can confirm, this works

  for subfolder in subfolders:
    if 'eggs' in subfolder:
      subfolderPath = os.path.join(folderName, subfolder)
      os.rmdir(subfolderPath)