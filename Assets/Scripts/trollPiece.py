from termcolor import colored
import gamePiece
# from dwarfPiece import DwarfPiece
import dwarfPiece
from boardSquare import BoardSquare
valid_square = BoardSquare.valid_square


class TrollPiece(gamePiece.GamePiece):
    def __init__(self, (row, col)):
        gamePiece.GamePiece.__init__(self,(row, col))

    def __str__(self):
        return colored("T", 'green')

    def move(self, my_board, target):
        target_square = my_board.get_square(target)
        move_list = self.get_moves_list(my_board)
        #If target square isn't possible, return -1 to signal error.
        #Also generate shoved to know if the troll can capture more than one dwarf.
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
            #If target space has dwarf, check for captures, otherwise return the score.
            if TrollPiece.has_dwarf(my_board, target):
                return self.capture_dwarf(my_board, target, shoved)
            else:
                return 0

    def capture_dwarf(self, my_board, target, shoved):
        #TODO: Currently leaving this as is but I think that the only class that should interact with
        #TODO: the players is gameManager. So this should be reshaped into a bunch of gameManager methods
        #TODO: that return parsed information from the player.
        capture =  raw_input("Do you wish to capture a dwarf Y/N?")
        while capture != "Y" and capture != "N":
            capture = raw_input("Invalid answer. Do you wish to capture a dwarf Y/N?")
        if capture == "N":
            return 0
        else:
            dwarf_list = TrollPiece.get_dwarfs(my_board, target)
            #If troll can capture more than one dwarf.
            if shoved:
                score = 0
                while dwarf_list != []:
                    dwarf = raw_input('Input dwarf coordinates as: "x, y" or "-" to cancel.')
                    if dwarf == "-":
                        #If piece has been shoved(not adjacent to target) it must capture at least one dwarf.
                        if score == 0 and self.position not in my_board.get_square(target).get_adjacent():
                            print("Must capture at least one dwarf")
                            continue
                        else:
                            return score
                    else:
                        dwarf = tuple(map(int, dwarf.split(',')))
                        if dwarf in dwarf_list:
                            my_board.get_square(dwarf).vacant_square()
                            score += 1
                            dwarf_list.remove(dwarf)
                        else:
                            print("There's no dwarf in the indicated coordinates.")
            #Otherwise choose a dwarf to capture or end.
            else:
                #TODO: Didn't bother with text correctness, because of the earlier TODO.
                while True:
                    dwarf = raw_input('Input dwarf coordinates as: "x, y" or "-" to cancel.')
                    if dwarf == "-":
                        return 0
                    else:
                        dwarf = tuple(map(int, dwarf.split(',')))
                        if dwarf in dwarf_list:
                            my_board.get_square(dwarf).vacant_square()
                            return 1
                        else:
                            print("There's no dwarf in the indicated coordinates.")

    @staticmethod
    def has_dwarf(board, target):
        '''Returns true if exists a square adjacent to target with a dwarf.'''
        return TrollPiece.get_dwarfs(board, target) != []

    @staticmethod
    def get_dwarfs(board, target):
        '''Returns a list of position tuples of each adjacent square that contains a dwarf.'''
        ans = []
        adjacent_list = board.get_square(target).get_adjacent()
        for position in adjacent_list:
            if isinstance(board.get_square(position).piece, dwarfPiece.DwarfPiece):
                ans.append(position)
        return ans

    def get_moves_list(self, my_board):
        """Returns a list of the possible moves by this GamePiece."""
        (row, col) = self.position
        ans = []
        # For each direction
        for check_row in range(row - 1, row + 2):
            for check_col in range(col - 1, col + 2):
                # Skip self as it is not a direction
                if (check_row, check_col) == self.position:
                    continue
                #Check amount of trolls in opposite direction
                number_of_trolls = self.check_line(my_board, (check_row, check_col))
                #Get the direction in case we shove.
                (row_dir, col_dir) = (check_row - row, check_col - col)
                (row_step, col_step) = self.position
                (row_step, col_step) = (row_step + row_dir, col_step + col_dir)
                steps_taken = 1
                #As long as we haven't hit a piece, a wall or ran out of shove distance.
                while valid_square((row_step, col_step)) and\
                        (steps_taken == 1 or steps_taken <= number_of_trolls) and\
                        my_board.get_square((row_step, col_step)).piece is None:
                    #Check to see if you can get shoved there.
                    if steps_taken > 1 and self.has_dwarf(my_board, (row_step, col_step)):
                        ans.append(((row_step, col_step), True))
                    elif steps_taken == 1:
                        ans.append(((row_step, col_step), number_of_trolls > 0))
                    steps_taken += 1
                    (row_step, col_step) = (row_step + row_dir, col_step + col_dir)
        return ans
