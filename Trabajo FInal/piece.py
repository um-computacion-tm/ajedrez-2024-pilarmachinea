class Piece:
    def __init__(self, color, name):
        self.__color__ = color
        self.__name__ = name
    
    def color(self):
        return self.__color__
    
    def name(self):
        return self.__name__

    def __str__(self):
        return self.__white_str__ if self.__color__ == 'Blanco' else self.__black_str__
    


