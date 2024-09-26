from chess import ChessGame
from board import Tablero
from exceptions import InvalidMove, InvalidMoveNoPiece, InvalidMoveIndexError, InvalidMoveOutOfBounds, InvalidMoveSameColor, InvalidMoveSamePlace

class Cli:

    def __init__(self):
        self.chess = ChessGame()
        self.positions = self.chess.obtener_tablero().obtener_posiciones()
        
    
    def comenzar(self):
        self.mostrar_tablero()

    def mostrar_tablero(self):
            print("Turno: " + self.chess.obtener_turno_actual())
            print("   " + "   ".join([str(i) for i in range(8)]))
            print("  " + "----" * 8) 

            for i, fila in enumerate(self.positions):
                fila_str = ' | '.join([str(piece) if piece else ' ' for piece in fila])
                print(f'{i} | {fila_str} |') 
                print("  " + "----" * 8)  


    def input_function(self):
        try:
            from_row = int(input('From row: '))
            from_col = int(input('From col: '))
            to_row = int(input('To row: '))
            to_col = int(input('To col: '))

        # Verificar si las coordenadas están dentro del rango
            if any(coord < 0 or coord > 7 for coord in [from_row, from_col, to_row, to_col]):
                raise InvalidMoveOutOfBounds()

            return [from_row, from_col, to_row, to_col]
        except ValueError:
            print("Error: Entrada no válida. Debe introducir un número entero.")
            return False
