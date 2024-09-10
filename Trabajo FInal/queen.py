from piece import Piece

class Queen(Piece):
    white_str_ = "♕"
    black_str = "♛"

    def possible_positions(self, row, col):
        """
        Devuelve las posiciones posibles para una reina.
        """
        possibles = []

        # Movimientos diagonales (como un alfil)
        directions = [
            (1, 1),    # Abajo-Derecha
            (1, -1),   # Abajo-Izquierda
            (-1, 1),   # Arriba-Derecha
            (-1, -1)   # Arriba-Izquierda
        ]

        for drow, dcol in directions:
            next_row, next_col = row + drow, col + dcol
            while 0 <= next_row < 8 and 0 <= next_col < 8:
                piece_at_pos = self.board.__possition__[next_row, next_col]
                if piece_at_pos is None:  # Casilla vacía
                    possibles.append((next_row, next_col))
                elif piece_at_pos.color != self.color:  # Captura de una pieza enemiga
                    possibles.append((next_row, next_col))
                    break
                else:  # Encuentra una pieza propia
                    break
                next_row += drow
                next_col += dcol

        # Movimientos horizontales y verticales (como una torre)
        directions = [
            (1, 0),    # Abajo
            (-1, 0),   # Arriba
            (0, 1),    # Derecha
            (0, -1)    # Izquierda
        ]

        for drow, dcol in directions:
            next_row, next_col = row + drow, col + dcol
            while 0 <= next_row < 8 and 0 <= next_col < 8:
                piece_at_pos = self.board.__possition__[next_row, next_col]
                if piece_at_pos is None:  # Casilla vacía
                    possibles.append((next_row, next_col))
                elif piece_at_pos.color != self.color:  # Captura de una pieza enemiga
                    possibles.append((next_row, next_col))
                    break
                else:  # Encuentra una pieza propia
                    break
                next_row += drow
                next_col += dcol

        return possibles
