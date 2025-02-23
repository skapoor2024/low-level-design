from pydantic import BaseModel, Field, field_validator
from board import Board

class Move(BaseModel):
    row: int
    col: int
    player: str
    board: Board

    @field_validator("row")
    @classmethod
    def validate_row(cls, row, values):
        board = values.get("board")
        if board is None:
            raise ValueError("Board instance must be provided for validation")
        if not (0 <= row < board.board_size):
            raise ValueError(f"Row must be between 0 and {board.board_size - 1}")
        return row

    @field_validator("col")
    @classmethod
    def validate_col(cls, col, values):
        board = values.get("board")
        if board is None:
            raise ValueError("Board instance must be provided for validation")
        if not (0 <= col < board.board_size):
            raise ValueError(f"Column must be between 0 and {board.board_size - 1}")
        return col

    @field_validator("col")
    @classmethod
    def check_occupied(cls, col, values):
        board = values.get("board")
        row = values.get("row")
        if board and row is not None and board.grid[row][col] != '_': #Check if row and board exists
            raise ValueError("That space is already occupied!")
        return col

    def __str__(self):
        return f'Player {self.player} moved to ({self.row},{self.col})'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col and self.player == other.player
    
    
