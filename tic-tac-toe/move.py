from pydantic import BaseModel


class Move(BaseModel):
    row: int
    col: int
    player: str

    def __str__(self):
        return f"Player {self.player} moved to ({self.row},{self.col})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (
            self.row == other.row
            and self.col == other.col
            and self.player == other.player
        )
