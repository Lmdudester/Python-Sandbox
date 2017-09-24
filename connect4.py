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
        for i in reversed(range(0,6)):
            if self.board[i][column] == 0:
                if(i == 0):
                    self.cols.remove(str(column))
                self.board[i][column] = player
                return player
        return 0

    def checkX(self, x, y, player):
        for i in [0,1,2]:
            x += 1
            if(self.board[y][x] != player):
                return False
        return True

    def checkY(self, x, y, player):
        for i in [0,1,2]:
            y -= 1
            if(self.board[y][x] != player):
                return False
        return True

    def checkXY(self, lr, x, y, player):
        for i in [0,1,2]:
            x += lr
            y -= 1
            if(self.board[y][x] != player):
                return False
        return True

    def playerWon(self, player):
        #For y coordinates in reverse
        for y in reversed(range(0,len(self.board))):
            #For x coordiates
            for x in range(0,len(self.board[y])):
                #If the player isn't right then skip it
                if(self.board[y][x] != player):
                    continue
                #If we need to check up
                if(y >= 3):
                    if(self.checkY(x, y, player)): #Check Up
                        return True

                    if(x >= 3):
                        if(self.checkXY(-1, x, y, player)): #Check Up-Left
                            return True

                    if(x <= 3):
                        if(self.checkX(x, y, player)): #Check Right
                            return True
                        if(self.checkXY(1, x, y, player)): #Check Up-Right
                            return True
                #Don't need to check up at all
                else:
                    if(x <= 3):
                        if(self.checkX(x, y, player)): #Check Right
                            return True

        #If nothing was found
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

        resp = getResp("Would you like to play another round? (Y/N)",
                        "Invalid response.", ['y', 'n'])


if __name__ == "__main__":
    main()
