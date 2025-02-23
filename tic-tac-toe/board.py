from typing import List
from pydantic import BaseModel, Field
from move import Move


class Board(BaseModel):
    board_size: int = Field(default=3, ge=1)
    grid: List[List[str]] = []
    count: int = 0

    def __init__(self, **data):
        super().__init__(**data)
        self.grid = [
            ["_" for _ in range(self.board_size)] for _ in range(self.board_size)
        ]

    def is_full(self) -> bool:
        return self.count == self.board_size**2

    def print_board(self) -> None:
        for row in self.grid:
            print("|".join(row))
            print("-" * (self.board_size * 2 - 1))
        print("\n")

    def check_winner(self, move: Move) -> bool:
        # check row
        if all(
            self.grid[move.row][col] == move.player for col in range(self.board_size)
        ):
            return True

        # check col
        if all(
            self.grid[row][move.col] == move.player for row in range(self.board_size)
        ):
            return True

        # check diagonal
        if all(self.grid[i][i] == move.player for i in range(self.board_size)):
            return True

        # check anti-diagonal
        if all(
            self.grid[i][self.board_size - 1 - i] == move.player
            for i in range(self.board_size)
        ):
            return True
        return False

    def make_move(self, move: "Move") -> bool:
        if (
            0 <= move.row < self.board_size
            and 0 <= move.col < self.board_size
            and self.grid[move.row][move.col] == "_"
        ):
            self.grid[move.row][move.col] = move.player
            self.count += 1
            return True
        else:
            return False
