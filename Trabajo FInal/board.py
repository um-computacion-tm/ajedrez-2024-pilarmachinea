from knight import Knight
from bishop import Bishop
from rook import Rook
from queen import Queen
from king import King
from pawn import Pawn
from exceptions import InvalidMoveOutOfBounds, InvalidMove, InvalidMoveNoPiece, InvalidMoveIndexError, InvalidMoveSameColor, InvalidMoveSamePlace

class Tablero:
    def __init__(self):
        self.positions= []
        for fila in range(8):
            col = []
            for columna in range(8):
                col.append(None)
            self.positions.append(col)

        #piezas blancas
        self.positions[0][0] = Rook("Blanco")
        self.positions[0][1] = Knight("Blanco")
        self.positions[0][2] = Bishop("Blanco")
        self.positions[0][3] = King("Blanco")
        self.positions[0][4] = Queen("Blanco")
        self.positions[0][5] = Bishop("Blanco")
        self.positions[0][6] = Knight("Blanco")
        self.positions[0][7] = Rook("Blanco")
        

        #peones
        for i in range(8):
            self.positions[1][i] = Pawn("Blanco")
            self.positions[6][i] = Pawn("Negro")

        #piezas negras
        self.positions[7][0] = Rook("Negro")
        self.positions[7][1] = Knight("Negro")
        self.positions[7][2] = Bishop("Negro")
        self.positions[7][3] = King("Negro")
        self.positions[7][4] = Queen("Negro")
        self.positions[7][5] = Bishop("Negro")
        self.positions[7][6] = Knight("Negro")
        self.positions[7][7] = Rook("Negro")

    def __str__(self):
        """Devuelve una representación en cadena del tablero."""
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell) + " "
                else:
                    board_str += ". "
            board_str += "\n"
        return board_str

    def valid_position(self, row, col):
        """Verifica si la posición está dentro del tablero."""
        return 0 <= row < 8 and 0 <= col < 8

    def get_piece(self, row, col):
        """Devuelve la pieza en una posición determinada o None si está vacía."""
        if not self.valid_position(row, col):
            return None  # Cambiar a retornar None en lugar de lanzar una excepción
        return self.positions[row][col]

    def move_piece(self, from_row, from_col, to_row, to_col):
        """Mueve una pieza de una posición a otra si el movimiento es válido."""
        if not self.valid_position(from_row, from_col) or not self.valid_position(to_row, to_col):
            raise InvalidMoveOutOfBounds ("Una o ambas coordenadas están fuera del rango del tablero")

        # Obtener la pieza de origen
        piece = self.get_piece(from_row, from_col)

        # Verificar si el movimiento es válido según las reglas de la pieza
        if not piece.valid_moves(from_row, from_col, to_row, to_col):
            raise InvalidMove("El movimiento no es válido para esta pieza")

        # Verificar si la posición de destino está vacía o contiene una pieza del oponente
        destination_piece = self.get_piece(to_row, to_col)
        if destination_piece is not None and destination_piece.get_color() == piece.get_color():
            raise InvalidMoveSameColor("No se puede mover a una posición ocupada por una pieza del mismo color")

        # Realizar el movimiento
        self.positions[to_row][to_col] = piece
        self.positions[from_row][from_col] = None

    def is_position_empty(self, row, col):
        """Verifica si una posición está vacía."""
        return self.positions[row][col] is None
