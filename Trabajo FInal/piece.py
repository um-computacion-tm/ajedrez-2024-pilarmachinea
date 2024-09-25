class Piece:
    def __init__(self, color, name):
        self.__color__ = color
        self.__name__ = name

    def __str__(self):
        return self.white_str_ if self.__color__ == 'white' else self.black_str_
    
    def color(self):
        return self.__color__
    
    def name(self):
        return self.__name__



