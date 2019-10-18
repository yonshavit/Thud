import gamePiece
from termcolor import colored

class TrollPiece(gamePiece.GamePiece):
    def __init__(self, (row, col)):
        gamePiece.GamePiece.__init__(self,(row, col))

    def get_print_string(self):
        return colored("T", 'green')

    def show_possible_move(self, board):
        pass
