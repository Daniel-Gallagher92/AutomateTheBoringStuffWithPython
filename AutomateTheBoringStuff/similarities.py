# The proper way to modify a string is to create a new string using slices
name = 'Navi a dog'
newName = name[0:5] + 'the' + name[6:10]

print(newName)

spam = [0,1,2,3,4,5]
cheese = spam 

print(spam)

cheese[1] = 'Hello!'
print(cheese)
print(spam) 

# Passing Lists in Function Calls 

def eggs(cheese):
  cheese.append('Sausage')

spam = [1, 2, 3]
eggs(spam) #Here we pass a reference to the list stored in 'spam'
print(spam)