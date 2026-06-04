board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

def show():
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])
    print()

def win(p):
    return (board[0]==board[1]==board[2]==p or
            board[3]==board[4]==board[5]==p or
            board[6]==board[7]==board[8]==p or
            board[0]==board[3]==board[6]==p or
            board[1]==board[4]==board[7]==p or
            board[2]==board[5]==board[8]==p or
            board[0]==board[4]==board[8]==p or
            board[2]==board[4]==board[6]==p)

player = "X"

for i in range(9):
    show()
    move = int(input("Enter position (0-8): "))
    
    if board[move] == " ":
        board[move] = player
        
        if win(player):
            show()
            print("Player", player, "wins!")
            break
        
        player = "O" if player == "X" else "X"
    else:
        print("Try again!")
else:
    show()
    print("Draw!")