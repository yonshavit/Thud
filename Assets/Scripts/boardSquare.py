from termcolor import colored
import dwarfPiece
from constants import BOARD_RANGE


class BoardSquare:

    def __init__(self, (row, col), piece=None):
        self.position = (row, col)
        self.piece = piece

    def __str__(self):
        """Returns a colored string representing the state of this BoardSquare."""
        if isinstance(self.piece, str):
            return self.piece
        if self.piece is None:
            return colored('E', 'white')
        else:
            return str(self.piece)

    def vacant_square(self):
        """Removes the piece from this position."""
        self.piece = None

    def occupy_square(self, piece):
        """Sets the piece to this position."""
        if self.piece is not None:
            raise TypeError("Attempting to occupy a non-vacant square.")
        self.piece = piece
        self.piece.position = self.position

    def get_adjacent(self):
        ans = []
        (row, col) = self.position
        for row_range in range(row-1, row+2):
            for col_range in range(col-1, col+2):
                if self.valid_square((row_range, col_range)):
                    ans.append((row_range, col_range))
        ans.remove(self.position)
        return ans

    @staticmethod
    def valid_square((row, col)):
        """Return True if the position is in a legal space on the board."""
        # The distance of all valid squares from the Thudstone is 9 at most, the Thudstone is not a valid square.
        return (row != 7 or col != 7) and (abs(row - 7) + abs(col - 7) <= 9) and \
            row in BOARD_RANGE and col in BOARD_RANGE
