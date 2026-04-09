from board import Board
#from player import Player
a = Board()
#a= Player()
row = int(input("enter row"))
col = int(input("enter col"))

a.make_move(0, 0, "0")
a.make_move(1, 0,  "X") 
a.make_move(2, 0, "X")
a.print_board()
print(a.check_winner())

