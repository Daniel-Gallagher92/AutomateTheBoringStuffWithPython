#A for loop repeats the code block once for each value in a list or list-like value

#Range objects are a list-like value

print(range(4)) # returns a range obj == range(0,4)

for i in range(4):
  print(i)

print()

for i in [0,1,2,3]:  #Both the above and this example return the exact same thing
  print(i)

#in a for loop such as above, the first item in the list gets assigned to the variable i,
# then executes the given block of code, then the second item in the list and so on... 
  
# "list like" is referring to the technical Python term "sequences"

#list() function 
# if you want the actual list value from from a range object value, pass it to the list() function
print()
range(4)
print(list(range(4))) #returns [0, 1, 2, 3]

#Really handy if you need to get a collection of integers in a list.
print()
print(list(range(0,100,2))) #returns [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

to_100_by_2 = list(range(0,100,2))
print()
print(to_100_by_2)

# a nice python trick is to use a for loop with the range function with the len function that is passed
# some list value
print()
supplies = ["monkey wrench", "flame-thrower", "No. 2 Pencil"]

for i in range(len(supplies)):
  print("Index " + str(i) + " in supplies is " + supplies[i])
  print()

#Great for running loop code over a list of ANY size when you need the integer index position
  # as well as the value associated with the list item 

#Multiple assignment 

#instead of:

cat = ["Fat", "Orange", "Loud"]
size = cat[0]
color = cat[1]
disposition = cat[2]

#You can use the multiple assignment operator 
#multiple variables on the LEFT SIDE of the assignment operator separated by a comma 

size, color, disposition = cat
print(size)
print(color)
print(disposition)

#Another useful trick is that you can have multiple var on the left side,
# and multiple values on the right side separated by commas as well
print()
size, color, disposition = "small", "black", "quiet"

print(size)
print(color)
print(disposition)

#This latter trick is used commonly for SWAPPING VARIABLES or swap operations 
print()
a = "AAA"
b = "BBB"

print(a)
print(b)

print()
a,b = b,a
print(a)
print(b)