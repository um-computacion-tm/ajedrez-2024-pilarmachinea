# exceptions.py

class InvalidMove(Exception):
    pass

class InvalidMoveNoPiece(InvalidMove):
    def __init__(self):
        super().__init__("No hay pieza en la posición de inicio.")

class InvalidMoveIndexError(InvalidMove):
    def __init__(self):
        super().__init__("Numero de fila o columna incorrecto.")

class InvalidMoveOutOfBounds(InvalidMove):
    def __init__(self):
        super().__init__("El movimiento está fuera de los límites del tablero.")

class InvalidMoveSameColor(InvalidMove):
    def __init__(self):
        super().__init__("No puedes mover una pieza a una posición ocupada por otra pieza de tu mismo color.")

class InvalidMoveSamePlace(InvalidMove):
    def __init__(self):
        super().__init__("No puede mover una pieza a su misma casilla.")

class CInvalidMoveNotColor(InvalidMove):
    def __init__(self):
        super().__init__("La pieza seleccionada no es de tu color.")