

class Board:
    def __init__(self):
        # data
        self.board = [
            ["", "", "_"],
            ["", "", "_"],
            ["", "", "_"]
        ]

    # behavior
    def make_move(self, row, col, symbol):
        self.board[row][col] = symbol

    # action
    def print_board(self):
        for row in self.board:
            print("|".join(row))

    def check_winner(self):
        # check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != "_":
                return row[0]