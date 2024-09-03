from piece import Piece

class Pawn(Piece):
    white_str_ = "♙"
    black_str = "♟"

def possible_positions(self, row, col):
    """
    Devuelve las posiciones posibles para un peón.
    """
    possibles = []
    
    # Determinar la dirección de avance del peón según el color
    direction = 1 if self.color == 'white' else -1
    
    # Movimiento normal de una casilla hacia adelante
    next_row = row + direction
    if 0 <= next_row < 8:  # Asegurarse de que esté dentro del tablero
        if self.board.__possition__[next_row, col] is None:  # La casilla debe estar vacía
            possibles.append((next_row, col))
            
            # Movimiento inicial de dos casillas
            if (row == 1 and self.color == 'white') or (row == 6 and self.color == 'black'):
                next_row_initial = row + (2 * direction)
                if self.board.__possition__[next_row_initial, col] is None:  # Ambas casillas deben estar vacías
                    possibles.append((next_row_initial, col))
    
    # Captura en diagonal
    for delta_col in [-1, 1]:  # Diagonal izquierda y derecha
        capture_row = row + direction
        capture_col = col + delta_col
        
        if 0 <= capture_row < 8 and 0 <= capture_col < 8:  # Dentro del tablero
            target_piece = self.board.__possition__[capture_row, capture_col]
            # Verificar si hay una pieza oponente en la casilla de captura
            if target_piece is not None and target_piece.color != self.color:
                possibles.append((capture_row, capture_col))
    
    # Movimiento especial "En passant"
    # (Se necesitaría lógica adicional para verificar si es posible capturar "en passant")
    
    return possibles