import unittest
from piece import Queen
from board import Board

class TestQueen(unittest.TestCase):
    def setUp(self):
        """
        Configura el tablero y coloca a la reina en diferentes posiciones para las pruebas.
        """
        self.board = Board()  # Crear una instancia del tablero
        self.white_queen = Queen('white', self.board)  # Crear una reina blanca
        self.black_queen = Queen('black', self.board)  # Crear una reina negra

    def test_possible_positions_center(self):
        """
        Prueba de posibles movimientos de la reina en el centro del tablero.
        """
        self.board.__possition__ = [[None] * 8 for _ in range(8)]  # Limpiar el tablero
        row, col = 3, 3  # Colocar la reina en el centro
        self.board.__possition__[row][col] = self.white_queen

        expected_moves = [
            # Movimientos diagonales
            (4, 4), (5, 5), (6, 6), (7, 7),   # Abajo-Derecha
            (2, 2), (1, 1), (0, 0),           # Arriba-Izquierda
            (4, 2), (5, 1), (6, 0),           # Abajo-Izquierda
            (2, 4), (1, 5), (0, 6),           # Arriba-Derecha
            # Movimientos horizontales y verticales
            (4, 3), (5, 3), (6, 3), (7, 3),   # Abajo
            (2, 3), (1, 3), (0, 3),           # Arriba
            (3, 4), (3, 5), (3, 6), (3, 7),   # Derecha
            (3, 2), (3, 1), (3, 0)            # Izquierda
        ]
        
        actual_moves = self.white_queen.possible_positions(row, col)
        self.assertEqual(set(actual_moves), set(expected_moves))

    def test_possible_positions_corner(self):
        """
        Prueba de posibles movimientos de la reina en una esquina del tablero.
        """
        self.board.__possition__ = [[None] * 8 for _ in range(8)]  # Limpiar el tablero
        row, col = 0, 0  # Colocar la reina en la esquina superior izquierda
        self.board.__possition__[row][col] = self.white_queen

        expected_moves = [
            # Movimientos diagonales
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),  # Abajo-Derecha
            # Movimientos horizontales y verticales
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),  # Abajo
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)   # Derecha
        ]
        
        actual_moves = self.white_queen.possible_positions(row, col)
        self.assertEqual(set(actual_moves), set(expected_moves))

    def test_possible_positions_with_blocking_pieces(self):
        """
        Prueba de posibles movimientos de la reina con piezas propias y enemigas bloqueando el camino.
        """
        self.board.__possition__ = [[None] * 8 for _ in range(8)]  # Limpiar el tablero
        row, col = 3, 3  # Colocar la reina en el centro
        self.board.__possition__[row][col] = self.white_queen

        # Colocar piezas propias en algunas direcciones
        self.board.__possition__[3][5] = Queen('white', self.board)  # Pieza propia a la derecha
        self.board.__possition__[5][3] = Queen('white', self.board)  # Pieza propia abajo

        # Colocar piezas enemigas en otras direcciones
        self.board.__possition__[3][1] = Queen('black', self.board)  # Pieza enemiga a la izquierda
        self.board.__possition__[1][3] = Queen('black', self.board)  # Pieza enemiga arriba

        expected_moves = [
            # Movimientos diagonales
            (4, 4), (5, 5), (6, 6), (7, 7),   # Abajo-Derecha
            (2, 2), (1, 1), (0, 0),           # Arriba-Izquierda
            (4, 2), (5, 1), (6, 0),           # Abajo-Izquierda
            (2, 4), (1, 5), (0, 6),           # Arriba-Derecha
            # Movimientos horizontales y verticales con bloqueos
            (4, 3), (2, 3), (1, 3),  # Vertical (Arriba- se detiene en pieza enemiga)
            (3, 2), (3, 1),          # Horizontal (Izquierda- se detiene en pieza enemiga)
            (3, 4),                  # Horizontal (Derecha- se detiene en pieza propia)
        ]
        
        actual_moves = self.white_queen.possible_positions(row, col)
        self.assertEqual(set(actual_moves), set(expected_moves))


if __name__ == '__main__':
    unittest.main()
