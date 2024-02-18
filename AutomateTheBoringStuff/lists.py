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