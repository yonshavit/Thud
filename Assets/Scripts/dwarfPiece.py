from termcolor import colored
from gamePiece import GamePiece
from trollPiece import TrollPiece
from boardSquare import valid_square


class DwarfPiece(GamePiece):
    def __init__(self, (row, col)):
        GamePiece.__init__(self, (row, col))

    def __str__(self):
        return colored("D", 'blue')

    def get_moves_list(self, my_board):
        """Returns a list of all legal move positions."""
        (row, col) = self.position
        ans = []
        # For each direction
        for check_row in range(row-1, row+2):
            for check_col in range(col-1, col+2):
                # Skip self as it is not a direction
                if (check_row, check_col) == self.position:
                    continue
                # Aggregate the list of possible moves in the direction (check_row, check_col)
                ans = ans + (self.get_moves_in_direction(my_board, (check_row, check_col)))
        return ans

    def get_moves_in_direction(self, my_board, (target_row, target_col)):
        # Get the direction and starting point
        (my_row, my_col) = self.position
        # The direction in which we are checking
        (row_dir, col_dir) = (target_row - my_row, target_col - my_col)
        # The current square we check and advance.
        (row_step, col_step) = (my_row + row_dir, my_col + col_dir)
        # Set up step counter and ans
        step_counter = 0
        ans = []
        # While the next step is not a wall or a dwarf
        while valid_square((row_step, col_step)) and \
                not isinstance(my_board.get_square((row_step, col_step)).piece, DwarfPiece):
            # Count the step
            step_counter += 1
            # If it's a troll, check for throw.
            if isinstance(my_board.get_square((row_step, col_step)).piece, TrollPiece):
                # If you can hurl at the troll, add it to ans.
                if step_counter <= self.sum_pieces_in_opposite_direction(my_board, (target_row, target_col)):
                    ans.append((row_step, col_step))
                # Finally break the while loop because we stop before him or on him.
                return ans
            # else it's clear, add it to ans.
            else:
                ans.append((row_step, col_step))
            # Finally advance step
            (row_step, col_step) = (row_step + row_dir, col_step + col_dir)
        return ans

    def move(self, my_board, pos):
        score = 0
        target_square = my_board.get_square(pos)
        move_list = self.get_moves_list(my_board)
        # If target square isn't possible, return -1 to signal error.
        if pos not in move_list:
            return -1
        # First vacant our own square
        (my_row, my_col) = self.position
        my_board.get_square((my_row, my_col)).vacant_square()
        # Then occupy target square
        # Check if it's a troll, and update score if necessary.
        if isinstance(target_square.piece, TrollPiece):
            target_square.vacant_square()
            score = 4
        # Occupy the square and return the score.
        target_square.occupy_square(self)
        print(my_board)
        return score

