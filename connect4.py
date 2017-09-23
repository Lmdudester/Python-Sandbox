class Board:

    def __init__(self):
        self.board = [  [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]   ]

    def dropDisk(self, player, column):
        for i in reversed(range(0,6)):
            if self.board[i][column] == 0:
                self.board[i][column] = player
                return player
        return 0

    def __str__(self):
        ret = "+ - + - + - + - + - + - + - +\n"
        for i in self.board:
            ret += "|"
            for j in i:
                ret += " " + str(j) + " |"
            ret += "\n+ - + - + - + - + - + - + - +\n"
        return ret

def main():
    board = Board()
    print(board)

    board.dropDisk(1,0)
    board.dropDisk(1,0)
    board.dropDisk(1,0)
    board.dropDisk(1,0)
    board.dropDisk(1,0)
    board.dropDisk(1,0)
    if(board.dropDisk(1,0) == 0):
        print("Error")

    print(board)

if __name__ == "__main__":
    main()
