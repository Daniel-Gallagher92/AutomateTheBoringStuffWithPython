# Different use cases of escape character 

print('That is Brittani\'s dog, lil Navi!')
print()
print('Hey there!\nHow are you?\nI\'m fine' ) # prints strings in a block rather than one line
print()

#Raw strings begin with lower case r immediately r''

# as a Raw String, Python interprets the backslash as a literal character, meant to be a part of the string

print(r'That is Brittani\'s dog.') # returns That is Brittani\'s dog. 
print()

### Multiline strings 
dogBurglar = print("""Dear Brittani,
      Navi has been arrested for shoplifting chicken chips,
      burglary,
      and extortion of the Pet Shop owner.
      Sincerely,
      The FBI""")

dogBurglar