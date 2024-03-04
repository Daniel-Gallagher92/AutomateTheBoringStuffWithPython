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

# In the case you DO want a completely separate list, use the copy.deepcopy() module function
import copy #import the copy module library

spam = ['A', 'B', 'C', 'D']

cheese = copy.deepcopy(spam)
cheese[1] = 42
print(cheese) #This reflects the changes made 
print(spam) # This will print the original, unmodified list

# Line Continuation with lists. Improves readability with longer lists vs one lining 
spam = ['Apples',
        'Oranges',
        'Clementines',
        'Bananas']

print(spam)

# Line Continuation using the '\' new line char

print('In today\'s news...' + \
      'interest rates are down' + \
        ' and entry level jobs are plentiful!!!')

#The above code block prints as normal:
# In today's news...interest rates are down and entry level jobs are plentiful!!!