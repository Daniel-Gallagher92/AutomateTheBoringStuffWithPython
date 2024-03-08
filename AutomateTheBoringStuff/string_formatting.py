name = 'Daniel'
place = 'Blank Barbers'
time = '6 pm'
food = 'Apple Pie'

print('Hello ' + name + ', you\'re invited to a party at ' + place + ' at ' + time + '. Please bring ' + food + '.')

# This complicated syntax returns:
# Hello Daniel, you're invited to a party at Blank Barbers at 6 pm. Please bring Apple Pie.

#Instead you can use conversion specifiers with %s 

print('Hello %s, you\'re invited to a party at %s at %s. Please bring %s.' % (name, place, time, food))

# evaluates to the exact same thing
# Hello Daniel, you're invited to a party at Blank Barbers at 6 pm. Please bring Apple Pie.