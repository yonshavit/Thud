# from __future__ import print_function
import sys
from termcolor import colored, cprint
import gamePiece
import boardSquare
import pieceFactory

class Board():
    """A class that hold the gameboard as a 15 by 15 matrix."""

    # Functions

    def __init__(self):
        #Attributes
        self.squares = [ [ None for col in range(15) ] for row in range(15) ]
        for row in range (0, 15):
            for col in range(0, 15):
                pos = (row,col)
                if Board.valid_square(pos):
                    self.squares[row][col] = boardSquare.BoardSquare(pos,pieceFactory.PieceFactory.create(pos))

                else:
                    self.squares[row][col] = boardSquare.BoardSquare(pos)

    def get_Square(self,(row, col)):
        """Returns the BoardSquare at pos."""
        return self.squares[row][col]

    def print_board(self):
        """Prints an ascii representation of the board to the console."""
        for row in range(0,15):
            for col in range(0,15):
                if not Board.valid_square((row , col)):
                    cprint('*', 'red', end='')
                else:
                    cprint(self.squares[row][col].print_piece(), end='')
            cprint("\n", end='')

    @staticmethod
    def valid_square((row, col)):
        """Return True if the position is in a legal space on the board."""
        # The distance of all valid squares from the Thudstone is 9 at most, the Thudstone is not a valid square.
        return (row != 7 or col != 7) and (abs(row - 7) + abs(col - 7) <= 9)
