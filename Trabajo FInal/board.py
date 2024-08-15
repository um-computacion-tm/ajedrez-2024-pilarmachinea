from piece import Rook

class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        self.__positions__[0][0] = Rook("black")
        self.__positions__[0][7] = Rook("black")
        self.__positions__[7][7] = Rook("white")
        self.__positions__[7][0] = Rook("white")

def get_piece(self,row, col):
    return self.__positions__[row][col]





"""
para poner alguna pieza pongo self.positions[0][0] = rook() (torre)
from "archivo" import "clase"
"""