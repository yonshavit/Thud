from dwarfPiece import DwarfPiece
from trollPiece import TrollPiece


class PieceFactory:
    """A factory class to generate gamepieces based on starting position."""

    @staticmethod
    def create((row, col)):
        if (abs(row - 7) + abs(col - 7) == 9) or\
                (abs(row - 7) + abs(col - 7) == 8 and (row == 0 or row == 14 or col == 0 or col == 14)):
            return DwarfPiece((row, col))
        elif abs(row - 7) <= 1 and abs(col - 7) <= 1:
            return TrollPiece((row, col))
        else:
            return None
