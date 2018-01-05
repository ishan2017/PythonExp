#Double_Dimension_2
import random
import pdb
a = []

COMPUTER = 'X'
USER = 'O'
TIE = ' '
#pdb.set_trace()

class rowColumnCheck():
    def isGameOver(self, table, xPos, yPos):
        pos = table[xPos][yPos]
        #print("rowColumnCheck")
        #pdb.set_trace()
        Count = 0
        for y in range (len(table)):
            if table[xPos][y].getSymbol() == pos.getSymbol():
                Count += 1
            else:
                break
        if Count == len(table):
            return True
        Count = 0
        for x in range (len(table)):
            if table[x][yPos].getSymbol() == pos.getSymbol():
                Count += 1
            else:
                break
        if Count == len(table):
            return True
        return False

class backDiagonalCheck():
    def isGameOver(self, table, xPos, yPos):
        pos = table[xPos][yPos]
        #print("backDiagonalCheck")
        Count = 0
        for i in range (len(table)):
            if table[i][i].getSymbol() == pos.getSymbol():
                Count += 1
            else:
                break
        if Count == len(table):
            return True
        return False

class forwardDiagonalCheck():
    def isGameOver(self, table, xPos, yPos):
        pos = table[xPos][yPos]
        #print("forwardDiagonalCheck")
        Count = 0
        x = 0
        y = len(table) - 1
        for i in range (len(table)):
            if table[x][y].getSymbol() == pos.getSymbol():
                Count += 1
                x = x + 1
                y = y - 1
            else:
                break
        if Count == len(table):
            return True
        return False

class Position():
    def __init__(self, symbol, xPos, yPos):
        self.symbol = symbol
        self.xPos = xPos
        self.yPos = yPos
        self.checkArray = []
    def getSymbol(self):
        return self.symbol

    def setSymbol(self, symbol):
        self.symbol = symbol

    def isGameOver(self, table): 
        #print("Position len(self.checkArray): " + str(len(self.checkArray)))
        for i in range (len(self.checkArray)):
            if self.checkArray[i].isGameOver(table, self.xPos, self.yPos) == True:
                return True
        return False



def printRowSeperator(maxCount):
    for k in range(maxCount):
        print('-',end="")
    print()

def getComputerSelection(a):
    while True:
        row_comp = random.randint(0, size - 1)
        col_comp = random.randint(0, size - 1)
        if a[row_comp][col_comp].getSymbol() == TIE:
            a[row_comp][col_comp].setSymbol(COMPUTER)
            print("Computer Selected : (" + str(row_comp + 1) + "," + str(col_comp + 1) + ")")
            break
    return a[row_comp][col_comp]

def getUserSelection(a):
    while True:
        while True:
            row_user = int(input('please enter the row of your selection (make sure it is between 1 and the size of table) ')) - 1
            if row_user >= 0 and row_user < len(a):
                break
        while True:
            col_user = int(input('please enter the column of your selection (make sure it is between 1 and the size of table) ')) - 1
            if col_user >= 0 and col_user < len(a):
                break
        if a[row_user][col_user].getSymbol() == TIE:
            a[row_user][col_user].setSymbol(USER)
            print("User Selected : (" + str(row_user + 1) + "," + str(col_user + 1) + ")")
            break
        else:
            print("Selection has already been taken")
    return a[row_user][col_user]

def printPositions(maxRowSepCount, a):
    print()
    printRowSeperator(maxRowSepCount)
    for i in range(len(a)):
        print('|',end="")
        for j in range(len(a[i])):
            if j < size:
                print(a[i][j].getSymbol(), end='|')
        print()
        if i < size:
            printRowSeperator(maxRowSepCount)
    print()
    
while True:
    size = int(input('What is the size of this game table (Odd number > 1) : '))
    if ((size % 2) == 1 and size > 1):
        break
    
max_attempts = (size * size) // 2
max_row_sep = (2 * size) + 1

for i in range(size):
    a.append([])
for i in range(size):
    for j in range(size):
        if i == size // 2 and j == size // 2: #center Position
            a[i].append(Position(TIE, i, j)) 
            a[i][j].checkArray.append(rowColumnCheck())
            a[i][j].checkArray.append(backDiagonalCheck())
            a[i][j].checkArray.append(forwardDiagonalCheck())
        elif i == j: #back diagonal
            a[i].append(Position(TIE, i, j))
            a[i][j].checkArray.append(rowColumnCheck())
            a[i][j].checkArray.append(backDiagonalCheck())

        elif i + j == size - 1: # forward diagonal
            a[i].append(Position(TIE, i, j))
            a[i][j].checkArray.append(rowColumnCheck())
            a[i][j].checkArray.append(forwardDiagonalCheck())

        else: # basic
            a[i].append(Position(TIE, i, j))
            a[i][j].checkArray.append(rowColumnCheck())

        
print(a)
        
for attempt in range(max_attempts):    
    selection = getComputerSelection(a)
    if not selection.isGameOver(a):
        printPositions(max_row_sep, a)
        selection = getUserSelection(a)     
    printPositions(max_row_sep, a)
    if selection.isGameOver(a):
        if selection.getSymbol() == COMPUTER:
            print("Computer Won!!")
        else:
            print("User Won!!")
        break

if not selection.isGameOver(a):
    selection = getComputerSelection(a)
    if selection.isGameOver(a):
        if selection.getSymbol() == COMPUTER:
            print("Computer Won!!")
        else:
            print("User Won!!")
    printPositions(max_row_sep, a)
