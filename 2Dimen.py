#Double_Dimension_2
import random
row_comp = 0
col_comp = 0
row_user = 0
col_user = 0
a = []

COMPUTER = 'X'
USER = 'O'
TIE = ' '

#symbols = ['X', 'O']

def printRowSeperator(maxCount):
    for k in range(maxCount):
        print('-',end="")
    print()

def getComputerSelection():
    while True:
        row_comp = random.randint(0, size - 1)
        col_comp = random.randint(0, size - 1)
        if a[row_comp][col_comp] == TIE:
            a[row_comp][col_comp] = COMPUTER
            print("Computer Selected : (" + str(row_comp) + "," + str(col_comp) + ")")
            break
    return isWinPosition(row_comp, col_comp)

def getUserSelection(size):
    while True:
        while True:
            row_user = int(input('please enter the row of your selection (make sure it is between 1 and one less of the size of your array) '))
            if row_user >= 0 and row_user < size:
                break
        while True:
            col_user = int(input('please enter the column of your selection (make sure it is between 1 and one less of the size of your array) '))
            if col_user >= 0 and col_user < size:
                break
        if a[row_user][col_user] == TIE:
            a[row_user][col_user] = USER
            print("User Selected : (" + str(row_user) + "," + str(col_user) + ")")
            break
        else:
            print("Selection has already been taken")
        return isWinPosition(row_user, col_)

def isWinPosition(row, col):
    return TIE

def printPositions(maxRowSepCount):
    print()
    printRowSeperator(maxRowSepCount)
    for i in range(len(a)):
        print('|',end="")
        for j in range(len(a[i])):
            if j < size:
                print(a[i][j], end='|')

        print()
        if i < size:
            printRowSeperator(maxRowSepCount)
    print()
    
while True:
    size = int(input('What is the size of this two dimension array (Odd number > 1) : '))
    if ((size % 2) == 1 and size > 1):
        break
    
max_attempts = (size * size) // 2
max_row_sep = (2 * size) + 1

##for i in range(size):
##    for j in range(size):
##        index = random.randint(0, 2)
##        a[i].append(symbols[index])

for i in range(size):
    a.append([])
for i in range(size):
    for j in range(size):
        a[i].append(' ')
        
for attempt in range(max_attempts):    
    won = getComputerSelection()
    if won != COMPUTER:
        printPositions(max_row_sep)
        getUserSelection(size)     
        won = isWinPosition(row_user, col_user)
    printPositions(max_row_sep)
    if won != TIE:
        if won == COMPUTER:
            print("Computer Won!!")
        else:
            print("User Won!!")
        break

if won == TIE:
    won = getComputerSelection()
    if won != TIE:
        if won == COMPUTER:
            print("Computer Won!!")
        else:
            print("User Won!!")
    printPositions(max_row_sep)

    
    
