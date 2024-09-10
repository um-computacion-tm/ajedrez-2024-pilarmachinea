import unittest
from piece import Bishop, Piece
from board import Board

class TestBishopPossiblePositions(unittest.TestCase):
    
    def setUp(self):
        # Crear un tablero vacío
        self.board = Board()
        self.bishop = Bishop('white', self.board)  # Suponemos que el alfil es blanco
        
    def test_free_movement(self):
        # Colocar el alfil en el centro del tablero
        row, col = 4, 4
        self.board.__possition__[row, col] = self.bishop
        
        # Obtener posiciones posibles para el alfil
        expected_positions = [
            (5, 5), (6, 6), (7, 7),  # Diagonal arriba-derecha
            (5, 3), (6, 2), (7, 1),  # Diagonal arriba-izquierda
            (3, 5), (2, 6), (1, 7),  # Diagonal abajo-derecha
            (3, 3), (2, 2), (1, 1), (0, 0)  # Diagonal abajo-izquierda
        ]
        
        # Verificar que las posiciones posibles sean las esperadas
        self.assertEqual(set(self.bishop.possible_positions(row, col)), set(expected_positions))

    def test_blocked_by_own_piece(self):
        # Colocar el alfil en el centro del tablero
        row, col = 4, 4
        self.board.__possition__[row, col] = self.bishop
        
        # Colocar una pieza propia en una de las diagonales
        self.board.__possition__[5, 5] = Piece ('white')  # Pieza propia
        
        # Obtener posiciones posibles para el alfil
        expected_positions = [
            (5, 3), (6, 2), (7, 1),  # Diagonal arriba-izquierda
            (3, 5), (2, 6), (1, 7),  # Diagonal abajo-derecha
            (3, 3), (2, 2), (1, 1), (0, 0)  # Diagonal abajo-izquierda
        ]
        
        # Verificar que las posiciones posibles sean las esperadas
        self.assertEqual(set(self.bishop.possible_positions(row, col)), set(expected_positions))

    def test_capture_enemy_piece(self):
        # Colocar el alfil en el centro del tablero
        row, col = 4, 4
        self.board.__possition__[row, col] = self.bishop
        
        # Colocar una pieza enemiga en una de las diagonales
        self.board.__possition__[5, 5] = Piece('black')  # Pieza enemiga
        
        # Obtener posiciones posibles para el alfil
        expected_positions = [
            (5, 5),  # Captura en diagonal
            (5, 3), (6, 2), (7, 1),  # Diagonal arriba-izquierda
            (3, 5), (2, 6), (1, 7),  # Diagonal abajo-derecha
            (3, 3), (2, 2), (1, 1), (0, 0)  # Diagonal abajo-izquierda
        ]
        
        # Verificar que las posiciones posibles sean las esperadas
        self.assertEqual(set(self.bishop.possible_positions(row, col)), set(expected_positions))

    def test_at_board_edge(self):
        # Colocar el alfil en el borde del tablero
        row, col = 0, 0
        self.board.__possition__[row, col] = self.bishop
        
        # Obtener posiciones posibles para el alfil
        expected_positions = [
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)  # Diagonal hacia arriba-derecha
        ]
        
        # Verificar que las posiciones posibles sean las esperadas
        self.assertEqual(set(self.bishop.possible_positions(row, col)), set(expected_positions))

if __name__ == "__main__":
    unittest.main()
