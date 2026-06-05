game=[
    [0,1,2],
    [3,4,5],
    [6,7,8]
]
print("\n",game[0],"\n",game[1],"\n",game[2])
for  i  in range(len(game)):
  for j in range(len(game[i])):
    n = int(input("enter the position"))
    game[i][j]=input(f" enter input for {i},{j}")
print("\n",game[0],"\n",game[1],"\n",game[2])