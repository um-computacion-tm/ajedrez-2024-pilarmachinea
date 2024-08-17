class Piece:
    def __init__(self, color):
        self.__color__ = color

class Rook(Piece):  
    def __init__(self, color):
        super().__init__(color)

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
    
class King(Piece):
    def __init__(self, color):
        super().__init__(color)