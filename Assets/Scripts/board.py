from termcolor import colored
from pieceFactory import PieceFactory
from constants import BOARD_RANGE
from boardSquare import BoardSquare
valid_square = BoardSquare.valid_square



class Board:
    """A class that hold the gameboard as a 15 by 15 matrix."""

    def __init__(self):
        #Attributes
        self.squares = [[None for col in BOARD_RANGE] for row in BOARD_RANGE]
        for row in BOARD_RANGE:
            for col in BOARD_RANGE:
                pos = (row,col)
                if valid_square(pos):
                    self.squares[row][col] = BoardSquare(pos, PieceFactory.create(pos))

                else:
                    self.squares[row][col] = BoardSquare(pos)

    # Functions

    def get_square(self,(row, col)):
        """Returns the BoardSquare at pos."""
        return self.squares[row][col]

    def __str__(self):
        """SReturns a string represntation of board."""
        ans = ""
        for row in BOARD_RANGE:
            for col in BOARD_RANGE:
                if not valid_square((row, col)):
                    ans = ans + colored('*', 'red')
                else:
                    ans = ans + str(self.get_square((row, col)))
            ans = ans + "\n"
        return ans
