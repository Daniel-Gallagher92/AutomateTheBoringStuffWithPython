myDog = { 'name': 'Navi', 'age': 3 , 'color': 'black/brown'}

allDogs = []

allDogs.append({ 'name': 'Spud', 'age': 3 , 'color': 'brown'})
allDogs.append({ 'name': 'Ozzy' , 'age': 14 , 'color': 'grey'})
allDogs.append({ 'name': 'Navi', 'age': 3 , 'color': 'black/brown'})

print(allDogs)


theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

import pprint

pprint.pprint(theBoard)

theBoard['top-L'] = 'O'
theBoard['top-M'] = 'O'
theBoard['top-R'] = 'O'
theBoard['mid-L'] = 'X'
theBoard['mid-M'] = 'X'
theBoard['low-R'] = 'X'

pprint.pprint(theBoard)

def printBoard(board):
    """Print board
    
    Prints each row of a given tic-tac-toe board.
    
    Args:
        board:  Dictionary containing space names as keys and contents as values.

    Returns:
        None. Prints rows of tic-tac-toe board.
    """
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

print()
printBoard(theBoard)


#type function for when you need to identify value you are working with
print(type(42)) #returns <class 'int'>
print(type('hiya')) #returns <class 'str'>
print(type(3.14)) #returns <class 'float'>
print(type(theBoard)) #returns <class 'dict'>
print(type(theBoard['mid-M'])) #returns <class 'str'> which helps identify the VALUE paired to the key
