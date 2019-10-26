from termcolor import colored
import gamePiece
import dwarfPiece
from boardSquare import valid_square


class TrollPiece(gamePiece.GamePiece):
    def __init__(self, (row, col)):
        gamePiece.GamePiece.__init__(self,(row, col))

    def __str__(self):
        return colored("T", 'green')

    def move(self, my_board, target):
        target_square = my_board.get_square(target)
        move_list = self.get_moves_list(my_board)
        # If target square isn't possible, return -1 to signal error.
        # Also generate shoved to know if the troll can capture more than one dwarf.
        for position, shove in move_list:
            if target == position:
                legal_move = True
                shoved = shove
        if not legal_move:
            return -1
        else:
            # First vacant our own square
            my_board.get_square(self.position).vacant_square()
            # Then occupy target square
            target_square.occupy_square(self)
            # If target space has dwarf, check for captures, otherwise return the score.
            if has_adjacent_dwarf(my_board, target):
                return self.capture_dwarfs(my_board, shoved)
            else:
                return 0

    @staticmethod
    def get_capture_dwarf_position():
        while True:
            dwarf = raw_input('Input dwarf coordinates as: "x, y" or "-" to cancel.')
            if dwarf == "-":
                return ()
            else:
                # TODO: Add try statement for input check.
                return tuple(map(int, dwarf.split(',')))

    def capture_dwarfs(self, my_board, shoved):
        # Case 1: Troll was shoved..
        if shoved:
            score = 0
            adjacent_dwarfs = len(get_adjacent_dwarfs(my_board, self.position))

            while adjacent_dwarfs > 0:
                new_score_delta = self.capture_one_dwarf(my_board)
                if new_score_delta == 0:
                    # If no dwarf was inputted make sure at least one dwarf was captured.
                    if score == 0:
                        print("Must capture at least one dwarf")
                        continue
                    # If score > 0 we can return.
                    return score
                # If we captured a dwarf, we update the score and the adjacent dwarfs list.
                score += new_score_delta
                adjacent_dwarfs -= 1
            # If we ran out of adjacent dwarfs.
            return score

        # Case 2: Capture one dwarf or cancel..
        return self.capture_one_dwarf(my_board)

    def capture_one_dwarf(self, my_board):
        target = self.position
        adjacent_dwarfs = get_adjacent_dwarfs(my_board, target)
        while True:
            dwarf = TrollPiece.get_capture_dwarf_position()
            # If no dwarf is to be captured, return the score change 0.
            if dwarf == ():
                return 0
            # If the dwarf is a legal capture, remove it from the board and return the score change(1)
            if dwarf in adjacent_dwarfs:
                my_board.get_square(dwarf).vacant_square()
                return 1
            # Otherwise re prompt the user for a dwarf or - to cancel.
            print("Illegal dwarf capture coordinates.")

    def get_moves_list(self, my_board):
        """Returns a list of the possible moves by this GamePiece.
        Each move is a tuple of (position, boolean) where the boolean indicates whether the troll was shoved."""
        (row, col) = self.position
        ans = []
        # For each direction
        for check_row in range(row - 1, row + 2):
            for check_col in range(col - 1, col + 2):
                # Skip self as it is not a direction
                if (check_row, check_col) == self.position:
                    continue
                # Aggregate the list of possible moves in the direction (check_row, check_col)
                ans = ans + self.get_moves_in_direction(my_board, (check_row, check_col))
        return ans

    def get_moves_in_direction(self, my_board, (target_row, target_col)):
        (my_row, my_col) = self.position
        number_of_trolls = self.sum_pieces_in_opposite_direction(my_board, (target_row, target_col))
        # The direction in which we are checking
        (row_dir, col_dir) = (target_row - my_row, target_col - my_col)
        # The current square we check and advance.
        (row_step, col_step) = (my_row + row_dir, my_col + col_dir)
        steps_taken = 1
        ans = []
        # As long as the next square is a valid, empty square that's either close or can be shoved into.
        while valid_square((row_step, col_step)) and \
                (steps_taken == 1 or steps_taken <= number_of_trolls) and \
                my_board.get_square((row_step, col_step)).piece is None:
            # Check to see if there's an adjacent dwarf so shove is legal.
            if steps_taken > 1 and has_adjacent_dwarf(my_board, (row_step, col_step)):
                ans.append(((row_step, col_step), True))
            elif steps_taken == 1:
                ans.append(((row_step, col_step), number_of_trolls > 0))
            steps_taken += 1
            (row_step, col_step) = (row_step + row_dir, col_step + col_dir)
        return ans


def has_adjacent_dwarf(board, target):
    """Returns true if exists a square adjacent to target with a dwarf."""
    return get_adjacent_dwarfs(board, target) != []


def get_adjacent_dwarfs(board, target):
    """Returns a list of position tuples of each adjacent square that contains a dwarf."""
    ans = []
    adjacent_list = board.get_square(target).get_adjacent()
    for position in adjacent_list:
        if isinstance(board.get_square(position).piece, dwarfPiece.DwarfPiece):
            ans.append(position)
    return ans
