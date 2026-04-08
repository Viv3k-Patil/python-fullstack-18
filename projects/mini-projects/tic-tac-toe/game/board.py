from utils.constants import EMPTY

class Board:
    def __init__(self, size: int):
        self.size = size
        self.grid = [[EMPTY for _ in range(size)] for _ in range(size)]

    def display(self):
        for row in self.grid:
            print(" | ".join(row))
        print("-" * (self.size * 4))

    def is_valid_move(self, row: int, col: int) -> bool:
        return (
            0 <= row < self.size and
            0 <= col < self.size and
            self.grid[row][col] == EMPTY
        )

    def make_move(self, row: int, col: int, symbol: str) -> bool:
        if not self.is_valid_move(row, col):
            return False
        self.grid[row][col] = symbol
        return True

    def is_full(self) -> bool:
        return all(cell != EMPTY for row in self.grid for cell in row)

    def check_winner(self):
        size = self.size

        # rows
        for row in self.grid:
            if row.count(row[0]) == size and row[0] != EMPTY:
                return row[0]

        # columns
        for col in range(size):
            col_vals = [self.grid[row][col] for row in range(size)]
            if col_vals.count(col_vals[0]) == size and col_vals[0] != EMPTY:
                return col_vals[0]

        # diagonals
        diag1 = [self.grid[i][i] for i in range(size)]
        if diag1.count(diag1[0]) == size and diag1[0] != EMPTY:
            return diag1[0]

        diag2 = [self.grid[i][size - i - 1] for i in range(size)]
        if diag2.count(diag2[0]) == size and diag2[0] != EMPTY:
            return diag2[0]

        return None