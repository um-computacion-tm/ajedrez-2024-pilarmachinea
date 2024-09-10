import unittest
from piece import Knight
from board import Board

class TestKnight(unittest.TestCase):
    def setUp(self):
        """
        Configura el tablero y coloca al caballo en diferentes posiciones para las pruebas.
        """
        self.board = Board()  # Crear una instancia del tablero
        self.white_knight = Knight('white', self.board)  # Crear un caballo blanco
        self.black_knight = Knight('black', self.board)  # Crear un caballo negro

    def test_possible_positions_center(self):
        """
        Prueba de posibles movimientos del caballo en el centro del tablero.
        """
        self.board.__possition__ = [[None] * 8 for _ in range(8)]  # Limpiar el tablero
        row, col = 4, 4  # Colocar el caballo en el centro
        self.board.__possition__[row][col] = self.white_knight

        expected_moves = [
            (6, 5), (6, 3), (2, 5), (2, 3),  # Movimientos verticales
            (5, 6), (5, 2), (3, 6), (3, 2)   # Movimientos horizontales
        ]
        
        actual_moves = self.white_knight.possible_positions(row, col)
        self.assertEqual(set(actual_moves), set(expected_moves))

    def test_possible_positions_corner(self):
        """
        Prueba de posibles movimientos del caballo en una esquina del tablero.
        """
        self.board.__possition__ = [[None] * 8 for _ in range(8)]  # Limpiar el tablero
        row, col = 0, 0  # Colocar el caballo en la esquina superior izquierda
        self.board.__possition__[row][col] = self.white_knight

        expected_moves = [(2, 1), (1, 2)]  # Solo dos movimientos posibles desde la esquina
        
        actual_moves = self.white_knight.possible_positions(row, col)
        self.assertEqual(set(actual_moves), set(expected_moves))

    def test_possible_positions_with_blocking_pieces(self):
        """
        Prueba de posibles movimientos del caballo con piezas propias y enemigas bloqueando el camino.
        """
        self.board.__possition__ = [[None] * 8 for _ in range(8)]  # Limpiar el tablero
        row, col = 4, 4  # Colocar el caballo en el centro
        self.board.__possition__[row][col] = self.white_knight

        # Colocar piezas propias y enemigas en algunas posiciones alcanzables
        self.board.__possition__[6][5] = Knight('white', self.board)  # Pieza propia
        self.board.__possition__[3][6] = Knight('black', self.board)  # Pieza enemiga

        expected_moves = [
            (6, 3), (2, 5), (2, 3), # Movimientos permitidos
            (5, 6), (5, 2), (3, 2), # Movimientos permitidos
            (3, 6)                  # Movimiento de captura (pieza enemiga)
        ]
        
        actual_moves = self.white_knight.possible_positions(row, col)
        self.assertEqual(set(actual_moves), set(expected_moves))

if __name__ == '__main__':
    unittest.main()
