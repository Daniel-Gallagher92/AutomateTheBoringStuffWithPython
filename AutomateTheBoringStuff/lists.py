#For the slice function, in python, it works the same as the range function in the way that it will go up to,
#but NOT include the last item of the slice

#syntax is 
spam = ['cat','bat','rat', 'elephant']
print(spam[1:3])      #Prints ['bat','rat'] but NOT 'elephant' that lives at index positions 3


#You can also assign values to index values using singular index position OR the slice function


spam = ['10','20','30']

print(spam)

spam[1] = "Mayo"

print(spam)

spam[1:3] = ['CAT','DOG','MONKEY']

print(spam)


#slice shortcut 

#Leaving out the first index of the slice syntax (before colon) is the same as using the first index position
#Leaving out the last index of the slice syntax (after colon) is the same as using the length of the list which goes to the 
#last index position

spam = ['cat','bat','rat', 'elephant']
print(spam[:2])
print(spam[1:])

#use a del statement to delete elements from array 
# the del statement is the "unassignment" statement 

del spam[2]
print(spam) #removed rat

#You may also use the len statement on lists/array's 

print(len([1,2,3,4])) #Prints that the length is 4

#You can also do list concatenation 

print([1,2,3] + [4,5,6]) #prints [1, 2, 3, 4, 5, 6]

#The same applies to replication #The majority of things you may do with strings, you can do with lists

print('Hello' * 3)
print([1,2,3] * 3)

# A list function also exists

print(list('Hello'))

#You may also use the IN or NOT IN operators to determine whether a not an element in included in a list

print('hello' in ['Hey', 'Hiya', 'Hey there', 'Howdy']) #False
print('Howdy' in ['Hey', 'Hiya', 'Hey there', 'Howdy']) #True

print('Howdy' not in ['Hey', 'Hiya', 'Hey there', 'Howdy']) #False
print('hello' not in ['Hey', 'Hiya', 'Hey there', 'Howdy']) #True

#Notes on lists that are different from Ruby

#reminder you can access the list in reverse using negative integers

#The slice has 2 indexes. the returned list will have the first index and then UP TO BUT NOT INCLUDE last index
# the len() function, concatenation, and replication work the same with lists as they do with strings
#You can convert a value to a list passing it to the list() function 