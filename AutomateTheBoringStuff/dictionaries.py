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

print(myDog == myOtherDog) # Evaluates to true because order does not matter in dictionaries 
