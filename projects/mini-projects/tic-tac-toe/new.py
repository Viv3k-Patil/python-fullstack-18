from board import Board
from player import Player


a = Board()

# row = int(input("enter row"))
# col = int(input("enter col"))
a.make_move(0, 1, "O")
a.make_move(1, 1, "O")
a.make_move(2, 1, "O")
a.print_board()
print(a.check_winner())


    
    