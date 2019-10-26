from dwarfPiece import DwarfPiece
from trollPiece import TrollPiece


def create((row, col)):
    """A factory function to generate game pieces based on starting position."""
    if (abs(row - 7) + abs(col - 7) == 9) or\
            (abs(row - 7) + abs(col - 7) == 8 and (row == 0 or row == 14 or col == 0 or col == 14)):
        return DwarfPiece((row, col))
    elif abs(row - 7) <= 1 and abs(col - 7) <= 1:
        return TrollPiece((row, col))
    else:
        return None
