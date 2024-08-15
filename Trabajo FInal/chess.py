from board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "white"


    def move(self, from_row, from_col, to_row, to_col):
    
        #validate coords
        piece = self.board.__positions_.get_piece(from_row, from_col)
        self.change_turn()
        #existe del 0 al 7 y del 0 al 7 teniendo en cuenta las coordenandas que se pueden poner para mover

    def change_turn(self):
        if self.__turn__ == "white":
            self.__turn__ = "black"
        else:
            self.__turn__ = "white"
            