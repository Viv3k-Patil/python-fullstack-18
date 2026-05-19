board = ["0","1","2","3","4","5","6","7","8"]
player = "X"

for i in board:
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

    n = int(input("Enter position: ")) 

    if board[n] == "X" or board[n] == "O":
        print("Taken")
        continue
    else:
        board[n] = player

    if (board[0]==board[1]==board[2] or
        board[3]==board[4]==board[5] or
        board[6]==board[7]==board[8] or
        board[0]==board[3]==board[6] or
        board[1]==board[4]==board[7] or
        board[2]==board[5]==board[8] or
        board[0]==board[4]==board[8] or
        board[2]==board[4]==board[6]):
        print(player, "wins")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"
else:
    print("Draw")