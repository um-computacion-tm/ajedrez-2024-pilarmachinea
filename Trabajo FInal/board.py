from knight import Knight
from bishop import Bishop
from rook import Rook
from queen import Queen
from king import King
from pawn import Pawn

class Tablero:
    def __init__(self):
        self.positions= []
        for fila in range(8):
            col = []
            for columna in range(8):
                col.append(None)
            self.positions.append(col)

        #piezas blancas
        self.positions[0][0] = Rook("Torre", "Blanco")
        self.positions[0][1] = Knight("Caballo", "Blanco")
        self.positions[0][2] = Bishop("Alfil", "Blanco")
        self.positions[0][3] = King("Rey", "Blanco")
        self.positions[0][4] = Queen("Reina", "Blanco")
        self.positions[0][5] = Bishop("Alfil", "Blanco")
        self.positions[0][6] = Knight("Caballo", "Blanco")
        self.positions[0][7] = Rook("Torre", "Blanco")
        

        #peones
        for i in range(8):
            self.positions[1][i] = Pawn("Peon", "Blanco")
            self.positions[6][i] = Pawn("Peon", "Negro")

        #piezas negras
        self.positions[7][0] = Rook("Torre", "Negro")
        self.positions[7][1] = Knight("Caballo", "Negro")
        self.positions[7][2] = Bishop("Alfil", "Negro")
        self.positions[7][3] = King("Rey", "Negro")
        self.positions[7][4] = Queen("Reina", "Negro")
        self.positions[7][5] = Bishop("Alfil", "Negro")
        self.positions[7][6] = Knight("Caballo", "Negro")
        self.positions[7][7] = Rook("Torre", "Negro")

    def obtener_posiciones(self):
        return self.positions
    
    #actualiza el tablero después de un movimiento
    def actualizar_posiciones(self, fila_origen, col_origen, fila_destino, col_destino):
        #mueve la pieza
        self.positions[fila_destino][col_destino] = self.positions[fila_origen][col_origen]
        #casilla de origen vacía
        self.positions[fila_origen][col_origen] = None

    #obtiene la pieza en una casilla específica
    def obtener_pieza(self, fila, columna):
        return self.positions[fila][columna] if self.positions[fila][columna] else None
