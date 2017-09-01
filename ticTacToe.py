import copy

blankBoard = [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~'], 0]
letterDict = {'A':0, 'B':1, 'C':2}

def printBoard(gmBrd):
    print ("\n  A B C")

    num = 1
    for i in gameBoard[:-1]:
        print (str(num) + " ", end='')
        for j in i:
            print (j + " ", end='')
        print ("")
        num += 1

def detWinner(gmBrd):
    row, col = 0, 0

    #Horizontal Check
    while row < 3:
        if gmBrd[row][0] == gmBrd[row][1] and gmBrd[row][1] == gmBrd[row][2]:
            if gmBrd[row][0] != '~':
                return gmBrd[row][0]
        row += 1

    #Vertical Check
    while col < 3:
        if gmBrd[0][col] == gmBrd[1][col] and gmBrd[1][col] == gmBrd[2][col]:
            if gmBrd[0][col] != '~':
                return gmBrd[0][col]
        col += 1

    #Diagonal Check
    if gmBrd[0][0] == gmBrd[1][1] and gmBrd[1][1] == gmBrd[2][2]:
        if gmBrd[1][1] != '~':
            return gmBrd[1][1]

    if gmBrd[0][2] == gmBrd[1][1] and gmBrd[1][1] == gmBrd[2][0]:
        if gmBrd[1][1] != '~':
            return gmBrd[1][1]

    return '~'

def takeTurn(gmBrd, player):
    if gmBrd[3] == 9:
        return 0
    else:
        gmBrd[3] += 1

    while True:
        print ("\n" + player + "'s Turn: ")
        try:
            inp = input("Enter the coordinates: [Format: letter,number] ")
            print(inp)

            #Get Letter
            if inp[0] in letterDict:
                lett = letterDict[inp[0]]
            else:
                print ("Bad letter coordinate, try again...")
                continue

            #Get Number
            if int(inp[2]) > 0 and int(inp[2]) < 4:
                num = int(inp[2]) - 1
            else:
                print ("Bad letter coordinate, try again...")
                continue

        except KeyboardInterrupt:
            exit()

        except:
            print ("Invalid Input, try again...")
            continue

        if gameBoard[num][lett] != '~':
            print ("\nLocation already taken...")
            printBoard(gameBoard)
            continue

        gameBoard[num][lett] = player
        printBoard(gameBoard)
        break

#Set up Program
print ("\n\tWelcome to TicTacToe!\n")
print ("Enter Ctrl+C to exit at any time.\n")
gameBoard = []
lett, num = 0, 0
result = '~'

#Run Game
while True:
    #Set up game
    gameBoard = copy.deepcopy(blankBoard)
    printBoard(gameBoard)
    lett, num = 0, 0
    result = detWinner(gameBoard)

    #Take Turns
    while True:
        #X's Turn
        if takeTurn(gameBoard, 'X') == 0:
            break
        result = detWinner(gameBoard)

        if result != '~':
            break

        #O's Turn
        takeTurn(gameBoard, 'O')
        result = detWinner(gameBoard)

        if result != '~':
            break

    if result != '~':
        print ("\nWinner: %s!\n" % result)
    else:
        print ("\nTie!\n")

    #Play another game?
    while True:
        try:
            yOrN = input("Play another game? (Y/N): ")
        except KeyboardInterrupt:
            exit()
        except:
            print ("Invalid Input, try again...")
            continue

        if yOrN == 'Y':
            break
        if yOrN == 'N':
            exit()

        print ("Invalid Input, try again...")
