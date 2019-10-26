from termcolor import colored
from boardSquare import valid_square


class GamePiece:
    """Abstract GamePiece Class."""

    def __init__(self, (row, col)):
        self.position = (row, col)

    def show_possible_moves(self, my_board):
        """Creates a new modified board where the squares at self.position's piece is 'D', 'magenta'
        and all possible move options pieces are 'P', 'cyan'."""
        new_board = my_board
        possible_moves = self.get_moves_list(my_board)
        # Change the possible movement squares to P.
        for position in possible_moves:
                new_board.get_square(position).piece = colored("P", "cyan")
        # Change my own square's color to magenta.
        position = self.position
        new_board.get_square(position).piece = colored("D", "magenta")
        print(new_board)

    def move(self, my_board, pos):
        """Moves the gamepiece to the relevent square if possible, returns the number of points scored."""
        raise NotImplementedError("Abstract Function")

    def get_moves_list(self, my_board):
        """Returns a list of the possible moves by this GamePiece."""
        raise NotImplementedError("Abstract Function")

    def sum_pieces_in_opposite_direction(self, my_board, (opp_row, opp_col)):
        """Receives a board and a cell adjacent to self
        Returns a counter of how many pieces are of same type in the opposite direction."""
        my_type = type(self)
        (row, col) = self.position
        (row_dir, col_dir) = (row-opp_row, col-opp_col)
        counter = 0
        while valid_square((row+row_dir, col+col_dir)) and\
                isinstance(my_board.get_square((row+row_dir, col+col_dir)).piece, my_type):
            counter += 1
            (row, col) = (row+row_dir, col+col_dir)
        return counter
