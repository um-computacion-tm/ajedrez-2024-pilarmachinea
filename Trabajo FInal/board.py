from piece import Rook
from piece import Knight
from piece import Bishop
from piece import Queen
from piece import King
from piece import Pawn

class Board:
    def __init__(self):
        """
        Inicializa el tablero de ajedrez con las piezas en sus posiciones iniciales.
        """
        # Crear un tablero vacío de 8x8
        self.__possition__ = [[None for _ in range(8)] for _ in range(8)]
        self.setup_initial_positions()

    def setup_initial_positions(self):
        """
        Configura las piezas en sus posiciones iniciales.
        """
        # Colocar peones
        for col in range(8):
            self.__possition__[1][col] = Pawn('white', self)
            self.__possition__[6][col] = Pawn('black', self)
        
        # Colocar otras piezas
        piece_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        
        for col, piece_cls in enumerate(piece_order):
            self.__possition__[0][col] = piece_cls('white', self)
            self.__possition__[7][col] = piece_cls('black', self)

    def is_within_bounds(self, row, col):
        """
        Verifica si la posición (row, col) está dentro de los límites del tablero.
        """
        return 0 <= row < 8 and 0 <= col < 8

    def get_piece(self, row, col):
        """
        Devuelve la pieza en la posición especificada (row, col).
        """
        if self.is_within_bounds(row, col):
            return self.__possition__[row][col]
        return None

    def move_piece(self, start_row, start_col, end_row, end_col):
        """
        Mueve una pieza de la posición (start_row, start_col) a (end_row, end_col) si es un movimiento válido.
        """
        piece = self.get_piece(start_row, start_col)
        
        if piece is None:
            raise ValueError("No hay pieza en la posición de inicio.")

        # Validar que el movimiento es posible según las reglas de la pieza
        possible_moves = piece.possible_positions(start_row, start_col)
        
        if (end_row, end_col) not in possible_moves:
            raise ValueError("Movimiento no permitido para la pieza seleccionada.")
        
        # Mover la pieza
        self.__possition__[end_row][end_col] = piece
        self.__possition__[start_row][start_col] = None
        piece.has_moved = True

    def print_board(self):
        """
        Imprime el tablero en su estado actual.
        """
        for row in self.__possition__:
            print(' '.join([str(piece) if piece else '.' for piece in row]))
        print()

if __name__ == '__main__':
    board = Board()
    board.print_board()
