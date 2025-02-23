from game import Game
from board import Board

class TicTacToe():

    def __init__(self):

        self.board = Board()
        self.game = Game(board = self.board, players = ['X','O'])

    def run(self):
        self.game.play_game()
        print(f'Game Over!')

if __name__ == '__main__':
    t = TicTacToe()
    t.run()

