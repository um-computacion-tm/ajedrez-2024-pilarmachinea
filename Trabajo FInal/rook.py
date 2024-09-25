from piece import Piece

class Rook(Piece):
    white_str_ = "♖"
    black_str_ = "♜"

    def __str__(self):
        return self.white_str_ if self.color == 'white' else self.black_str_
