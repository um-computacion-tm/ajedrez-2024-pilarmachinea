from chess import ChessGame
from board import Tablero
from exceptions import InvalidMove, InvalidMoveNoPiece, InvalidMoveIndexError, InvalidMoveOutOfBounds, InvalidMoveSameColor, InvalidMoveSamePlace

class Cli:

    def __init__(self):
        self.chess = ChessGame()
        self.positions = self.chess.obtener_tablero().obtener_posiciones()
        
    
    def comenzar(self):
        print("Para salir escriba QUIT.")
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
        from_row = int(input('From row: '))

            # Si el usuario introduce 999, significa que se quiere salir del juego
        if from_row == 999:
                return False

        Cli.buscar_index_error(self,from_row)

        from_col = int(input('From col: '))
        Cli.buscar_index_error(self,from_col)

        to_row = int(input('To row: '))
        Cli.buscar_index_error(self,to_row)

        to_col = int(input('To col: '))
        Cli.buscar_index_error(self,to_col)   

        return [from_row, from_col, to_row, to_col]
