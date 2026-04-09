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
            
        # check columns
        for col in range(3):
            col_values = []
            for row in range(3):
                col_values.append(self.board[row][col])
            if col_values[0] == col_values[1] == col_values[2] != "_":
                return col_values[0]



# class Board:
#     def __init__(self):
#         #data
#         self.board=[
#              ["_","_","_"],
#              ["_","_","_"],
#              ["_","_","_"]
# ] 
#          #behaviour 
#     def make_move(self,row,col,symbol):
#         self.board[row][col]=symbol
#          #action
#     def print_board(self):    
#           for row in self.board:
#            print("|".join(row))
    
#     def check_winner(self):
#         #check row
#         for row in self.board():
#             if row[0]==row[1]==row[2] !="_":
#                 return row[0]
            
#         for col in range(3):
#             col_values=[]
#             for row in range(3):
#                 col_values.append(self.board[row][col])
#             if col_values[0] == col_values[1]==col_values[2] !="_":
#                   return col_values[0]
                

