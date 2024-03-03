# The proper way to modify a string is to create a new string using slices
name = 'Navi a dog'
newName = name[0:5] + 'the' + name[6:10]

print(newName)