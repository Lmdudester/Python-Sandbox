class Board:

    def __init__(self):
        self.board = [  [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]   ]

        self.cols = ['0', '1', '2', '3', '4', '5', '6']

    def dropDisk(self, player, column):
        for i in reversed(range(0,len(self.board))):
            if self.board[i][column] == 0:
                if(i == 0):
                    self.cols.remove(str(column))
                self.board[i][column] = player
                return player
        return 0

    def checkBoard(self, deltaX, deltaY, x, y, player):
        if(self.board[y][x] != player):
            return False

        tx = x + deltaX
        ty = y + deltaY
        count = 1
        while(tx > -1 and tx < 7 and ty > -1 and ty < 6):
            if(self.board[ty][tx] == player):
                count += 1
            else:
                break
            tx = tx + deltaX
            ty = ty + deltaY

        tx = x - deltaX
        ty = y - deltaY
        while(tx > -1 and tx < 7 and ty > -1 and ty < 6):
            if(self.board[ty][tx] == player):
                count += 1
            else:
                break
            tx = tx - deltaX
            ty = ty - deltaY

        if(count >= 4):
            return True
        else:
            return False

    def playerWon(self, player):
        for i in range(0,len(self.board)):
            if(self.checkBoard(1,1,3,i,player)):
                return True
            if(self.checkBoard(1,-1,3,i,player)):
                return True
            if(self.checkBoard(1,0,3,i,player)):
                return True

        for i in range(0,len(self.board[3])):
            if(self.checkBoard(0,1,i,3,player)):
                return True
        return False

    def __str__(self):
        ret =  "  0   1   2   3   4   5   6  \n"
        ret += "+ - + - + - + - + - + - + - +\n"
        for i in self.board:
            ret += "|"
            for j in i:
                ret += " " + str(j) + " |"
            ret += "\n+ - + - + - + - + - + - + - +\n"
        return ret

def getResp(prompt, failStr, answerList):
    resp = input(prompt).lower()

    while True:
        if(resp in answerList):
            return resp
        if(resp == 'quit'):
            exit()
        print(failStr)
        resp = input(prompt).lower()

def takeTurn(board, player):
    print("Player %d's Turn" % player)
    col = getResp("Where do you want to drop your disk? ",
                "Column full or invalid number.", board.cols)

    board.dropDisk(player, int(col))
    print(board)

    return board.playerWon(player)

def main():
    print("Welcome to Connect 4!\n(Type \"quit\" to quit at any time)")
    resp = 'y'
    while resp == 'y':
        gameBoard = Board()
        print("\n" + gameBoard.__str__())

        while True:
            if(takeTurn(gameBoard, 1)):
                print("Player 1 Won!\n")
                break;

            if(takeTurn(gameBoard, 2)):
                print("Player 2 Won!\n")
                break;

        resp = getResp("Would you like to play another round? (Y/N) ",
                        "Invalid response.", ['y', 'n'])


if __name__ == "__main__":
    main()
