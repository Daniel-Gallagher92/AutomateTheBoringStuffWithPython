#A for loop repeats the code block once for each value in a list or list-like value

#Range objects are a list-like value

print(range(4)) # returns a range obj == range(0,4)

for i in range(4):
  print(i)

print()

for i in [0,1,2,3]:  #Both the above and this example return the exact same thing
  print(i)

# "list like" is referring to the technical Python term "sequences"
  
