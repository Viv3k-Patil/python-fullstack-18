class Board:
    def __init__(self):
        self.board=[
            ["_","_","_"],
            ["_","_","_"],
            ["_","_","_"]
        ]
    def _make_move(self,row,col,symbol):
        self.board[row][col]= symbol

    def print_board(self):
        for row in self.board:
            print("|".join(row))

a = Board()

row = int(input("enter row"))
col = int(input("enter col"))

a._make_move(row, col, "X")
a.print_board()


    