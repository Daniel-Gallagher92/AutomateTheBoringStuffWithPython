globalVariable = 42

def localScopeExample():
  localVariable = 42

print('awesome code')
print('awesome code also here')

def spam(): 
  eggs = 'Hello'
  print(eggs)

eggs = 42
spam() #This will return the local eggs var assigned in the function
print(eggs) #This will return global eggs var assigned outside the funtion

#If you want to assign a new global variable value from INSIDE of a function you must add a global statement at the top of the function 

def spam():
  global eggs #This will ensure you are changing the global variable 
  eggs = 'Hello'
  print(eggs)