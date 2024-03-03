spam = ['hey there', 'hello', 'hiya', 'hey!', 'hey there']

print(spam.index('hello')) #returns 1

print(spam.index('hey!')) #returns 3

print(spam.index('hey there')) #returns the index position of the first time it sees the given value

spam2 = ['cat', 'dog', 'bat']

print(spam2)

spam2.append('moose')

print(spam2)

spam2.insert(2, 'wombat')

print(spam2) #inserts wombat at index position 2

spam2.remove('moose')

print(spam2) #returns same list without moose, no matter the index position

# remove() only accepts 1 arg at a time 

spam3 = [8, 2, 5, 3.14, 1, -8]

spam3.sort()

print(spam3) #returns values sorted in ascending order

spam4 = ['cat', 'aardvaark', 'dogs', 'badger', 'elephant']

print(spam4)

spam4.sort()

print(spam4) # returns values sorted in alphabetical order 

spam4.sort(reverse=True)

print(spam4) # returns values sorted in reverse alphabetical order 

spam5 = ['a', 'z' , 'A' , 'Z']
spam5.sort(key=str.lower) #returns true alphabetical order it "sorts normally"

print(spam5)