
from piece import Piece

class King(Piece):
    white_str_ = "♔"
    black_str = "♚"

    def possible_positions(self, row, col):
        """
        Devuelve las posiciones posibles para un rey.
        """
        possibles = []

        # Direcciones de movimiento posibles para el rey (una casilla en cualquier dirección)
        directions = [
            (1, 0),    # Abajo
            (-1, 0),   # Arriba
            (0, 1),    # Derecha
            (0, -1),   # Izquierda
            (1, 1),    # Abajo-Derecha
            (1, -1),   # Abajo-Izquierda
            (-1, 1),   # Arriba-Derecha
            (-1, -1)   # Arriba-Izquierda
        ]

        for drow, dcol in directions:
            next_row, next_col = row + drow, col + dcol

            # Verificar si la nueva posición está dentro del tablero
            if 0 <= next_row < 8 and 0 <= next_col < 8:
                piece_at_pos = self.board.__possition__[next_row, next_col]
                if piece_at_pos is None:  # Casilla vacía
                    possibles.append((next_row, next_col))
                elif piece_at_pos.color != self.color:  # Captura de una pieza enemiga
                    possibles.append((next_row, next_col))

        return possibles
