from piece import Piece

class Bishop(Piece):
    white_str_ = "♗"
    black_str = "♝"

def possible_positions(self, row, col):
    """
    Devuelve las posiciones posibles para un alfil.
    """
    possibles = []

    # Movimientos diagonales
    # Diagonal hacia arriba-derecha
    next_row, next_col = row + 1, col + 1
    while next_row < 8 and next_col < 8:
        if self.board.__possition__[next_row, next_col] is not None:
            if self.board.__possition__[next_row, next_col].color != self.color:  # Captura de una pieza enemiga
                possibles.append((next_row, next_col))
            break  # Detener si encuentra una pieza (propia o enemiga)
        possibles.append((next_row, next_col))
        next_row += 1
        next_col += 1

    # Diagonal hacia arriba-izquierda
    next_row, next_col = row + 1, col - 1
    while next_row < 8 and next_col >= 0:
        if self.board.__possition__[next_row, next_col] is not None:
            if self.board.__possition__[next_row, next_col].color != self.color:  # Captura de una pieza enemiga
                possibles.append((next_row, next_col))
            break
        possibles.append((next_row, next_col))
        next_row += 1
        next_col -= 1

    # Diagonal hacia abajo-derecha
    next_row, next_col = row - 1, col + 1
    while next_row >= 0 and next_col < 8:
        if self.board.__possition__[next_row, next_col] is not None:
            if self.board.__possition__[next_row, next_col].color != self.color:  # Captura de una pieza enemiga
                possibles.append((next_row, next_col))
            break
        possibles.append((next_row, next_col))
        next_row -= 1
        next_col += 1

    # Diagonal hacia abajo-izquierda
    next_row, next_col = row - 1, col - 1
    while next_row >= 0 and next_col >= 0:
        if self.board.__possition__[next_row, next_col] is not None:
            if self.board.__possition__[next_row, next_col].color != self.color:  # Captura de una pieza enemiga
                possibles.append((next_row, next_col))
            break
        possibles.append((next_row, next_col))
        next_row -= 1
        next_col -= 1

    return possibles
