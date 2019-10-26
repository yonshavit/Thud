import board
import pieceFactory
my_board = board.Board()
my_board.print_board()

piece = pieceFactory.PieceFactory.create((7,8))
print(piece.get_print_string())
piece = pieceFactory.PieceFactory.create((0,8))
print(piece.get_print_string())
my_square = my_board.get_Square((7,8))
my_troll_piece = my_square.piece
my_square.vacant_square()
my_other_square = my_board.get_Square((8, 9))
my_other_square.occupy_square(my_troll_piece)
my_board.print_board()