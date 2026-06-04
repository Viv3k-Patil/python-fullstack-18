class Board:
    #data
    def __init__(self):
        self.board = [
               ["_","_","_"],
               ["_","_","_"],
               ["_","_","_"]
]
    #Behaviour
    def make_move(self,row,col,symbol):
        self.board[row][col] = symbol


    def print_Board(self):
        for row in self.board:
          print(" | ".join(row))

    #Action
    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2]  != "_":
                return row[0]


    def check_colums(self):
      for col in range(3):
           col_values = []
           for row in range(3):
            col_values.append(self.board[row][col])
           if col_values[0] == col_values[1] == col_values[2] != "_":
            return col_values[0]