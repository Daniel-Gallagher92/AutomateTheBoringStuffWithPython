# Key/Value pairs example using previous lesson's new line syntax for readability
myDog = {'size': 'smol',
          'color': 'black/brown',
          'disposition': 'snuggly'}

print(myDog['disposition'])

a = [1, 2, 3]
b = [3, 2, 1]

print(a == b) # Evaluates to false because order in lists matters even with identical values 

myOtherDog = { 'color': 'black/brown',
              'disposition': 'snuggly',
              'size': 'smol'
              }

print(myDog == myOtherDog) # Evaluates to True because order does not matter in dictionaries 


# Using the in and not in operator to see if specific keys exist

print('size' in myOtherDog) # Evaluates to True because key does exist in myOtherDog dictionary

print('name' in myOtherDog) # Evaluates to False because key does NOT exist in myOtherDog dictionary

print('size' not in myOtherDog) # Evaluates to False because key does exist in myOtherDog dictionary

print('name' not in myOtherDog) # Evaluates to True because key does NOT exist in myOtherDog dictionary
