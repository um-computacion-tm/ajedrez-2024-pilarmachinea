from piece import Piece

class Knight(Piece):
    white_str_= "♘"
    black_str = "♞"

    def possible_positions(self, row, col):
        """
        Devuelve las posiciones posibles para un caballo.
        """
        possibles = []

        # Definir los 8 movimientos posibles del caballo
        knight_moves = [
            (2, 1), (2, -1),   # Dos abajo, uno derecha/izquierda
            (-2, 1), (-2, -1), # Dos arriba, uno derecha/izquierda
            (1, 2), (-1, 2),   # Uno abajo/arriba, dos derecha
            (1, -2), (-1, -2)  # Uno abajo/arriba, dos izquierda
        ]

        # Verificar cada movimiento posible
        for drow, dcol in knight_moves:
            next_row, next_col = row + drow, col + dcol

            # Comprobar si el movimiento se mantiene dentro del tablero
            if 0 <= next_row < 8 and 0 <= next_col < 8:
                piece_at_pos = self.board.__possition__[next_row, next_col]
                
                # Si la casilla está vacía o contiene una pieza enemiga
                if piece_at_pos is None or piece_at_pos.color != self.color:
                    possibles.append((next_row, next_col))

        return possibles
