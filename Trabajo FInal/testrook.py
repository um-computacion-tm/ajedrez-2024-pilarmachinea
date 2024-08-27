from rook import Rook
from board import Board
from pawn import Pawn
import unittest

class TestRook(unittest.TestCase):
    def test_str(self):
        board = Board()
        rook = Rook("white")
        self.assertEqual(str(rook), "♖")

    def test_move_vertical_desc(self):
        rook = Rook("white")
        #parametros...
        #[el tablero]
        #[el lugar de la torre]
        #[el destino]
        #verificar...
        possibles = rook.possible_positions(5,0)
        self.assertEqual(possibles, [(5,0), (6,0), (7,0)])

    def test_move_vertical_asc(self):
        Board = Board()
        board.__positions__[6][0] = Pawn("white")
        rook = Rook("white")
        possibles = rook.possible_positions(4,0)
        self.assertEqual(possibles, [(3,0), (2,0), (1,0), (0,0)])

if __name__ == '__main__':
    unittest.main()