spam = 0
while spam < 5:
    print(' Hiya!')
    spam = spam + 1
    print('\n')

name = ' '
while name != 'your name':
    print('Please enter your name')
    name = input()
    print('\n')
print('Thank You!')
print('\n')

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))