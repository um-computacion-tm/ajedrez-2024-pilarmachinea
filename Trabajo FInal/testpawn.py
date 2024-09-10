import unittest
from piece import Pawn
from board import Board 

class TestPawn(unittest.TestCase):
    def setUp(self):
        """
        Configura el tablero y coloca peones en diferentes posiciones para las pruebas.
        """
        self.board = Board()  # Crear una instancia del tablero
        self.white_pawn = Pawn('white', self.board)  # Crear un peón blanco
        self.black_pawn = Pawn('black', self.board)  # Crear un peón negro

    def test_possible_positions_white_pawn_initial(self):
        """
        Prueba de movimientos iniciales posibles para un peón blanco en su posición de inicio.
        """
        self.board.__possition__ = [[None] * 8 for _ in range(8)]  # Limpiar el tablero
        row, col = 1, 4  # Colocar el peón blanco en su posición inicial
        self.board.__possition__[row][col] = self.white_pawn

        expected_moves = [(2, 4), (3, 4)]  # Un avance simple y uno doble
        actual_moves = self.white_pawn.possible_positions(row, col)
        self.assertEqual(set(actual_moves), set(expected_moves))

    def test_possible_positions_black_pawn_initial(self):
        """
        Prueba de movimientos iniciales posibles para un peón negro en su posición de inicio.
        """
        self.board.__possition__ = [[None] * 8 for _ in range(8)]  # Limpiar el tablero
        row, col = 6, 4  # Colocar el peón negro en su posición inicial
        self.board.__possition__[row][col] = self.black_pawn

        expected_moves = [(5, 4), (4, 4)]  # Un avance simple y uno doble
        actual_moves = self.black_pawn.possible_positions(row, col)
        self.assertEqual(set(actual_moves), set(expected_moves))

    def test_possible_positions_white_pawn_blocked(self):
        """
        Prueba de movimientos posibles para un peón blanco bloqueado.
        """
        self.board.__possition__ = [[None] * 8 for _ in range(8)]  # Limpiar el tablero
        row, col = 1, 4  # Colocar el peón blanco en su posición inicial
        self.board.__possition__[row][col] = self.white_pawn
        self.board.__possition__[2][4] = Pawn('black', self.board)  # Colocar un peón negro justo adelante

        expected_moves = []  # No puede moverse porque está bloqueado
        actual_moves = self.white_pawn.possible_positions(row, col)
        self.assertEqual(set(actual_moves), set(expected_moves))

    def test_possible_positions_white_pawn_capture(self):
        """
        Prueba de movimientos de captura en diagonal para un peón blanco.
        """
        self.board.__possition__ = [[None] * 8 for _ in range(8)]  # Limpiar el tablero
        row, col = 3, 3  # Colocar el peón blanco en el tablero
        self.board.__possition__[row][col] = self.white_pawn
        self.board.__possition__[4][2] = Pawn('black', self.board)  # Colocar un peón negro en diagonal izquierda
        self.board.__possition__[4][4] = Pawn('black', self.board)  # Colocar un peón negro en diagonal derecha

        expected_moves = [(4, 3), (4, 2), (4, 4)]  # Movimiento hacia adelante y dos capturas diagonales
        actual_moves = self.white_pawn.possible_positions(row, col)
        self.assertEqual(set(actual_moves), set(expected_moves))

    def test_possible_positions_black_pawn_capture(self):
        """
        Prueba de movimientos de captura en diagonal para un peón negro.
        """
        self.board.__possition__ = [[None] * 8 for _ in range(8)]  # Limpiar el tablero
        row, col = 4, 4  # Colocar el peón negro en el tablero
        self.board.__possition__[row][col] = self.black_pawn
        self.board.__possition__[3][3] = Pawn('white', self.board)  # Colocar un peón blanco en diagonal izquierda
        self.board.__possition__[3][5] = Pawn('white', self.board)  # Colocar un peón blanco en diagonal derecha

        expected_moves = [(3, 4), (3, 3), (3, 5)]  # Movimiento hacia adelante y dos capturas diagonales
        actual_moves = self.black_pawn.possible_positions(row, col)
        self.assertEqual(set(actual_moves), set(expected_moves))

    # Aquí podrías añadir una prueba para "En Passant" si se implementa esa lógica
    # def test_en_passant_white_pawn(self):
    #     pass  # Implementar cuando esté disponible la lógica de "en passant"


if __name__ == '__main__':
    unittest.main()
