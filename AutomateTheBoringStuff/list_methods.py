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