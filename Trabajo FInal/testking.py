import unittest
from piece import King, Board

class TestKing(unittest.TestCase):
    def setUp(self):
        """
        Configura el tablero y coloca al rey en diferentes posiciones para las pruebas.
        """
        self.board = Board()  # Crear una instancia del tablero
        self.white_king = King('white', self.board)  # Crear un rey blanco
        self.black_king = King('black', self.board)  # Crear un rey negro

    def test_possible_positions_center(self):
        """
        Prueba de posibles movimientos del rey en el centro del tablero.
        """
        self.board.__possition__ = [[None] * 8 for _ in range(8)]  # Limpiar el tablero
        row, col = 4, 4  # Colocar el rey en el centro
        self.board.__possition__[row][col] = self.white_king
        
        expected_moves = [
            (5, 4), (3, 4), (4, 5), (4, 3), (5, 5), (5, 3), (3, 5), (3, 3)
        ]
        actual_moves = self.white_king.possible_positions(row, col)
        self.assertEqual(set(actual_moves), set(expected_moves))

    def test_possible_positions_corner(self):
        """
        Prueba de posibles movimientos del rey en una esquina del tablero.
        """
        self.board.__possition__ = [[None] * 8 for _ in range(8)]  # Limpiar el tablero
        row, col = 0, 0  # Colocar el rey en la esquina superior izquierda
        self.board.__possition__[row][col] = self.white_king
        
        expected_moves = [(1, 0), (1, 1), (0, 1)]
        actual_moves = self.white_king.possible_positions(row, col)
        self.assertEqual(set(actual_moves), set(expected_moves))

    def test_possible_positions_with_enemy_piece(self):
        """
        Prueba de posibles movimientos del rey con una pieza enemiga adyacente.
        """
        self.board.__possition__ = [[None] * 8 for _ in range(8)]  # Limpiar el tablero
        row, col = 4, 4  # Colocar el rey en el centro
        self.board.__possition__[row][col] = self.white_king

        # Colocar una pieza enemiga en una posición adyacente
        self.board.__possition__[5][4] = self.black_king

        expected_moves = [
            (5, 4), (3, 4), (4, 5), (4, 3), (5, 5), (5, 3), (3, 5), (3, 3)
        ]
        actual_moves = self.white_king.possible_positions(row, col)
        self.assertEqual(set(actual_moves), set(expected_moves))

if __name__ == '__main__':
    unittest.main()
