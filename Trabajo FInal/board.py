from piece import Rook
from piece import Knight
from piece import Bishop
from piece import Queen
from piece import King
from piece import Pawn

class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)

        #Posicion de inicio de cada pieza
        self.__positions__[0][0] = Rook("black", self)
        self.__positions__[0][7] = Rook("black", self)
        self.__positions__[0][1] = Knight("black", self)
        self.__positions__[0][6] = Knight("black", self)
        self.__positions__[0][2] = Bishop("black", self)
        self.__positions__[0][5] = Bishop("black", self)
        self.__positions__[0][3] = Queen("black", self)
        self.__positions__[0][4] = King("black", self)
        self.__positions__[1][0] = Pawn("black", self)
        self.__positions__[1][1] = Pawn("black", self)
        self.__positions__[1][2] = Pawn("black", self)
        self.__positions__[1][3] = Pawn("black", self)
        self.__positions__[1][4] = Pawn("black", self)
        self.__positions__[1][5] = Pawn("black", self)
        self.__positions__[1][6] = Pawn("black", self)
        self.__positions__[1][7] = Pawn("black", self)
        
        self.__positions__[7][7] = Rook("white", self)
        self.__positions__[7][0] = Rook("white", self)
        self.__positions__[7][1] = Knight("white", self)
        self.__positions__[7][6] = Knight("white", self)
        self.__positions__[7][2] = Bishop("white", self)
        self.__positions__[7][5] = Bishop("white", self)
        self.__positions__[7][3] = Queen("white", self)
        self.__positions__[7][4] = King("white", self)
        self.__positions__[6][0] = Pawn("white", self)
        self.__positions__[6][1] = Pawn("white", self)
        self.__positions__[6][2] = Pawn("white", self)
        self.__positions__[6][3] = Pawn("white", self)
        self.__positions__[6][4] = Pawn("white", self)
        self.__positions__[6][5] = Pawn("white", self)
        self.__positions__[6][6] = Pawn("white", self)
        self.__positions__[6][7] = Pawn("white", self)
       

    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str

    def get_piece(self,row, col):
        return self.__positions__[row][col]

    def move_piece(self, start, end):
        piece = self.board[start[1]][start[0]]
        if not piece:
            print("No hay ninguna pieza en la posición inicial.")
            return False

        if piece.color != self.current_turn:
            print(f"No es el turno de {piece.color}.")
            return False

        if piece.is_valid_move(self.board, start, end):
            destination_piece = self.board[end[1]][end[0]]
            if destination_piece and destination_piece.color == piece.color:
                print("No puedes capturar tu propia pieza.")
                return False

            self.board[end[1]][end[0]] = piece
            self.board[start[1]][start[0]] = None
            self.current_turn = 'black' if self.current_turn == 'white' else 'white'
            return True
        else:
            print("Movimiento inválido.")
            return False




"""
para poner alguna pieza pongo self.positions[0][0] = rook() (torre)
from "archivo" import "clase"
"""