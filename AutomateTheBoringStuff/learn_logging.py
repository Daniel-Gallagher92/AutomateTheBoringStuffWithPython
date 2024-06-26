import logging
# below using the filename= arg, we can save our log messages to a .txt file in the cwd and it will not print to terminal

logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL) # this line disables log messages that follow. Comment out to see logs again

logging.debug('Start of Program')
# Example: Buggy Factorial Program

def factorial(n):
  logging.debug('Start of factorial(%s)' % (n))
  total = 1 

  for i in range(1, n + 1): # range must start at 1, instead of the default zero when given only one arg
    total *= i
    logging.debug('i is %s, total is %s' % (i,total))

  logging.debug('Return value is %s' % (total))  
  return total

print(factorial(5))

logging.debug('End of Program')
