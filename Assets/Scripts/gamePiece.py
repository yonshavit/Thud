import boardSquare

class GamePiece():
    """Abstract GamePiece Class."""

    def __init__(self, (row, col)):
        self.position = (row, col)

    def get_print_string(self):
        """Returns a colored string representing the GamePiece."""
        raise NotImplementedError("Abstract Function")

    def show_possible_move(self, board):
       raise NotImplementedError("Abstract Function")

    def move(self, board, pos):
        raise NotImplementedError("Abstract Function")

    def destroy(self, board):
        """Removes this piece from it's position on the board."""
        self.position.piece = None
