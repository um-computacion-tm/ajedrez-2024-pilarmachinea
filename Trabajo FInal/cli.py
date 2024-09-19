from chess import ChessGame
from board import Board
from exceptions import InvalidMove, InvalidMoveNoPiece, InvalidMoveIndexError, InvalidMoveOutOfBounds, InvalidMoveSameColor, InvalidMoveSamePlace

class Cli:

    def __init__(self):
        chess = ChessGame()
        board = chess.get_board()
        position = board.get_position()
        return [chess, position]