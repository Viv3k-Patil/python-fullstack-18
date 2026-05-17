from board import Board

a=Board()

# row = int(input("Enter row: "))
# col = int(input("Enter col: "))



a.make_move(0,0,"x")
a.make_move(1,0,"x")
a.make_move(2,0,"x")


a.print_Board()
print(a.check_winner())