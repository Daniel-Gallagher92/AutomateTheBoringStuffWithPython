import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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
# returns 0 .... BROKEN! 