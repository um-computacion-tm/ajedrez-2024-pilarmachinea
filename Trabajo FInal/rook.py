from piece import Piece

class Rook(Piece):
    white_str_ = "♖"
    black_str = "♜"

    #Como se mueve? las torres se mueven horizontal o verticalmente pero si tenemos otra pieza en la casilla, no se puede mover hacia esa casilla ni las de atras
    def possible_positions_vd(self, row, col):
        #la columna es igual, recorrer las filas
        #range(inicio, fin que no esta incluido)
        possibles = []
        for next_row in range(row + 1, 8):
            #que las celda que sigue no este ocupada
            if self.board.__possition__[next_row,col] is not None:
                break
            possibles.append((next_row, col))
        return possibles
        
    def possible_positions_va(self, row, col):
        #la columna es igual, recorrer las filas
        possibles = []

        for next_row in range(row - 1, -1, -1):
            if self.board.__possition__[next_row,col] is not None:
                break
            possibles.append((next_row, col))
        return possibles