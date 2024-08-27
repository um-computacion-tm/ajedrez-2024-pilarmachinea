class Piece:
    def __init__(self, color):
        self.__color__ = color

    def __str__(self):
        ...

    # verifica un movimiento especifico es valido
    def is_valid_move(self, board, start, end):
        raise NotImplementedError

class Rook(Piece):  
    ...

class Knight(Piece):
    ...

class Bishop(Piece):
    ...

class Queen(Piece):
     ...

class King(Piece):
      ...

class Pawn(Piece):
    ...
