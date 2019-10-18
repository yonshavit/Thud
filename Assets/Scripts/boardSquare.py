

class BoardSquare():

    def  __init__(self, (row, col), piece = None):
        self.position = (row, col)
        self.piece = piece

    def print_piece(self):
        """Returns a colored string representing the state of this BoardSquare."""
        if self.piece is None:
            return 'E'
        else:
            return self.piece.get_print_string()

    def vacant_square(self):
        """Removes the piece from this position."""
        self.piece = None

    def occupy_square(self, piece):
        """Sets the piece to this position."""
        self.piece = piece
        self.piece.position = self.position
