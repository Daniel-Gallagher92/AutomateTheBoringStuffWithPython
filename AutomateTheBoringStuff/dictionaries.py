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


# Dictionary Methods

# Keys method

print(myDog.keys()) # Returns dict_keys(['size', 'color', 'disposition'])

# Values Method

print(myDog.values()) # Returns dict_values(['smol', 'black/brown', 'snuggly'])

# Items Method 

print(myDog.items()) # Returns dict_items([('size', 'smol'), ('color', 'black/brown'), ('disposition', 'snuggly')])

# If you want to return an ACTUAL list, you must pass to the list function 

print(list(myDog.items())) #Returns [('size', 'smol'), ('color', 'black/brown'), ('disposition', 'snuggly')]

print(list(myDog.values())) #Returns ['smol', 'black/brown', 'snuggly']

print(list(myDog.keys())) #Returns ['size', 'color', 'disposition']

#[('size', 'smol'), ('color', 'black/brown'), ('disposition', 'snuggly')] are known as two item tuples
