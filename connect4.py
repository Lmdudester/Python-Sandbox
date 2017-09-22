class Board:

    def __init__(self):
        self.board = [  [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0]   ]

    def dropDisk(board, player, column):
        for i in reverse(range(0,8)):
            if self.board[column][i] == 0:
                self.board[column][i] = player
                return board
            return None

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


if __name__ == "__main__":
    main()
