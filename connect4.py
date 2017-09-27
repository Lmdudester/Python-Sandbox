from random import *

class Board:

    def __init__(self):
        self.board = [  [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]   ]

        self.cols = ['0', '1', '2', '3', '4', '5', '6']

        self.top = [5, 5, 5, 5, 5, 5, 5]

    def dropDisk(self, player, column):
        for i in reversed(range(0,len(self.board))):
            if self.board[i][column] == 0:
                if(i == 0):
                    self.cols.remove(str(column))
                self.top[column] -= 1
                self.board[i][column] = player
                return (i, column)
        return 0

    def checkBoard(self, deltaX, deltaY, x, y, player):
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

        return count

    def playerWon(self, x, y, player):
        if(self.checkBoard(1,1,x,y,player) >= 4):
            return True
        if(self.checkBoard(1,-1,x,y,player) >= 4):
            return True
        if(self.checkBoard(1,0,x,y,player) >= 4):
            return True
        if(self.checkBoard(0,1,x,y,player) >= 4):
            return True

        return False

    def compSearch(self, player):
        playerCheck = []
        for x in range(0, len(self.board[0])):
            if(self.top[x] != -1):
                #posY, negY, zeroY, zeroX
                playerCheck += [ max([self.checkBoard(1,1,x,self.top[x],player), self.checkBoard(1,-1,x,self.top[x],player),
                                self.checkBoard(1,0,x,self.top[x],player), self.checkBoard(0,1,x,self.top[x],player)]) ]
            else:
                playerCheck += [1]

        #If computer can win now, place disk there
        for i in range(0, len(playerCheck)):
            if(playerCheck[i] >= 4):
                self.dropDisk(player, i)
                print(self)
                print("Computer: Player %d dropped in column %d.\n" % (player,i))
                return True

        #Determine other player
        oppPlay = 0
        if(player == 1):
            oppPlay = 2
        else:
            oppPlay = 1

        #Block other player if they are about to win
        for x in range(0, len(self.board[0])):
            #posY, negY, zeroY, zeroX
            if(max([self.checkBoard(1,1,x,self.top[x],oppPlay), self.checkBoard(1,-1,x,self.top[x],oppPlay),
                            self.checkBoard(1,0,x,self.top[x],oppPlay), self.checkBoard(0,1,x,self.top[x],oppPlay)]) >= 4
                            and self.top[x] != -1):
                self.dropDisk(player, x)
                print(self)
                print("Computer: Player %d dropped in column %d.\n" % (player,x))
                return False

        #Search for 3 in a row potential
        for i in range(0, len(playerCheck)):
            if(playerCheck[i] == 3):
                self.dropDisk(player, i)
                print(self)
                print("Computer: Player %d dropped in column %d.\n" % (player,i))
                return False

        #Search for 2 in a row potential
        for i in range(0, len(playerCheck)):
            if(playerCheck[i] == 2):
                self.dropDisk(player, i)
                print(self)
                print("Computer: Player %d dropped in column %d.\n" % (player,i))
                return False

        #Otherwise do a random drop
        location = randint(0, len(self.cols)-1)
        self.dropDisk(player, int(self.cols[location]))
        print(self)
        print("Computer: Player %d dropped in column %d.\n" % (player,location))
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

    position = board.dropDisk(player, int(col))
    print(board)

    return board.playerWon(position[1], position[0], player)

def main():
    print("Welcome to Connect 4!\n(Type \"quit\" to quit at any time)")
    resp = 'y'
    while resp == 'y':
        players = int(getResp("How many players will be playing? (0-2) ",
                    "Invalid number.", ['0', '1', '2']))

        gameBoard = Board()
        print("\n" + gameBoard.__str__())

        while True:
            if(players == 0):
                print("Computer: Player 1's Turn")
                if(gameBoard.compSearch(1)):
                    print("Computer: Player 1 Won!\n")
                    break;
            else:
                if(takeTurn(gameBoard, 1)):
                    print("Player 1 Won!\n")
                    break;

            if(players == 1 or players == 0):
                print("Computer: Player 2's Turn")
                if(gameBoard.compSearch(2)):
                    print("Computer: Player 2 Won!\n")
                    break;
            else:
                if(takeTurn(gameBoard, 2)):
                    print("Player 2 Won!\n")
                    break;

            if(len(gameBoard.cols) == 0):
                print("It's a tie!\n")
                break;

        resp = getResp("Would you like to play another round? (Y/N) ",
                        "Invalid response.", ['y', 'n'])


if __name__ == "__main__":
    main()
