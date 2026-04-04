from game.board import Board
from game.player import Player
from utils.constants import PLAYER_X, PLAYER_O


class Game:
    def __init__(self, size=3):
        self.board = Board(size)
        self.players = [
            Player("Player 1", PLAYER_X),
            Player("Player 2", PLAYER_O)
        ]
        self.current_index = 0

    def switch_player(self):
        self.current_index = 1 - self.current_index

    def current_player(self):
        return self.players[self.current_index]

    def play(self):
        while True:
            self.board.display()
            player = self.current_player()

            try:
                row, col = map(int, input(f"{player.name} ({player.symbol}) enter row col: ").split())
            except ValueError:
                print("Invalid input")
                continue

            if not self.board.make_move(row, col, player.symbol):
                print("Invalid move. Try again.")
                continue

            winner = self.board.check_winner()
            if winner:
                self.board.display()
                print(f"🎉 {player.name} wins!")
                break

            if self.board.is_full():
                self.board.display()
                print("It's a draw!")
                break

            self.switch_player()