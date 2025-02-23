from pydantic import BaseModel,Field, field_validator
from typing import List
from board import Board
# from player import Player
from move import Move

class Game(BaseModel):

    """
    Define the game board
    Define the players
    Assign random player to start
    Assing the X and O randomly
    """

    board:Board
    players:List[str] = Field(default = ['X','O'])
    current_player:str = Field(default = 'X')
    winner:str = None

    @field_validator('players')
    @classmethod
    def check_players(cls,v):
        if len(v)!=2:
            raise ValueError('Only two players')
        return v
    
    def __init__(self,**data):
        super().__init__(**data)
        self.board = Board(**data)
        self.current_player = self.players[0]
        self.winner = None

    def switch_player(self):
        self.current_player = self.players[0] if self.current_player == self.players[1] else self.players[1]

    def play(self,move:Move)->bool:

        if self.winner:
            return False
        
        if self.board.is_full():
            return False
        
        if self.board.make_move(move):
            if self.board.check_winner(move):
                self.winner = move.player
            self.switch_player()
            return True
        else:    
            return False
        
    def print_board(self):
        return self.board.print_board()
    
    def play_game(self):

        while self.winner is None and self.board.is_full() is False:
            
            self.print_board()
            print(f'Player {self.current_player}\'s turn')
            
            try:
                
                row = int(input(f'Enter row: between 0 and {self.board.board_size-1}'))
                col = int(input(f'Enter col: between 0 and {self.board.board_size-1}'))
                move = Move(row = row,col = col, player = self.current_player, board = self.board)

                if not self.play(move):
                    continue

            except ValueError as e:
                print(e)
                continue

            except Exception as e:
                print(e)
                continue

        self.print_board()

        if self.winner:
            print(f'Player {self.winner} wins!')

        elif self.board.is_full():
            print('It\'s a tie!')
        







            
    



