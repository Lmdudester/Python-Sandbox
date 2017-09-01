import copy

blankBoard = [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
letterDict = {'A':0, 'B':1, 'C':2}

def printBoard(gmBrd):
    print "\n  A  B  C"

    num = 1
    for i in gameBoard:
        print str(num),
        for j in i:
            print j + " ",
        print ""
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
    while True:
        print "\n" + player + "'s Turn: "
        try:
            lett = raw_input("Enter the letter coordinate: ")
            if lett in letterDict:
                lett = letterDict[lett]
            else:
                print "Bad letter coordinate, try again..."
                continue

            num = int(raw_input("Enter the number coordinate: "))
            if num >= 1 and num <= 3:
                num = num - 1
            else:
                print "Bad number coordinate, try again..."
                continue

        except KeyboardInterrupt:
            exit()

        except:
            print "Invalid Input, try again..."
            continue

        if gameBoard[num][lett] != '~':
            print "\nLocation already taken..."
            printBoard(gameBoard)
            continue

        gameBoard[num][lett] = player
        printBoard(gameBoard)
        break

#Set up Program
print "\n\tWelcome to TicTacToe!\n"
print "Enter Ctrl+C to exit at any time.\n"
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
    while result == '~':
        #X's Turn
        takeTurn(gameBoard, 'X')
        result = detWinner(gameBoard)

        if result != '~':
            break;

        #O's Turn
        takeTurn(gameBoard, 'O')
        result = detWinner(gameBoard)

    print "\nWinner: %s\n" % result

    #Play another game?
    while True:
        try:
            yOrN = raw_input("Play another game? (Y/N): ")
        except KeyboardInterrupt:
            exit()
        except:
            print "Invalid Input, try again..."
            continue

        if yOrN == 'Y':
            break
        if yOrN == 'N':
            exit()

        print "Invalid Input, try again..."
