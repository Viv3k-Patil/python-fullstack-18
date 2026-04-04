from board import Board
from Player import Player

a = Board()
a=Player()
# row = int(input("enter row"))
# col = int(input("enter col"))

a.make_move(0, 0, "O")
a.make_move(1, 0,  "O")
a.make_move(2, 0, "O")
a.print_board()
print(a.check_winner())

