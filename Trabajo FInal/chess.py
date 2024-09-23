from board import Board
from movimientos import MoviminetoPiezas

class ChessGame:
    def __init__(self):
        """
        Inicializa el juego de ajedrez.
        """
        self.board = Board()
        self.current_turn = 'white'
        self.ganador = None
        self.reglas = MoviminetoPiezas()

    def print_instructions(self):
        """
        Imprime las instrucciones para jugar el juego.
        """
        print("Bienvenido al juego de Ajedrez en consola!")
        print("Para mover una pieza, introduce el comando en el formato 'E2 E4'.")
        print("Escribe 'salir' para terminar el juego.")
        print()

    def parse_input(self, input_str):
        """
        Convierte una entrada del usuario en coordenadas de tablero.
        """
        try:
            start, end = input_str.split()
            start_row, start_col = 8 - int(start[1]), ord(start[0].upper()) - ord('A')
            end_row, end_col = 8 - int(end[1]), ord(end[0].upper()) - ord('A')
            return (start_row, start_col), (end_row, end_col)
        except (ValueError, IndexError):
            print("Entrada no válida. Asegúrate de usar el formato 'E2 E4'.")
            return None, None

    def switch_turn(self):
        """
        Cambia el turno al siguiente jugador.
        """
        self.current_turn = 'black' if self.current_turn == 'white' else 'white'

    def play(self):
        """
        Ejecuta el bucle principal del juego de ajedrez.
        """
        self.print_instructions()

        while not self.is_game_over:
            self.board.print_board()
            print(f"Turno de las {self.current_turn}.")
            
            # Pedir al jugador que ingrese un movimiento
            move_input = input("Introduce tu movimiento: ")

            if move_input.lower() == 'salir':
                print("Gracias por jugar!")
                self.is_game_over = True
                break
            
            # Convertir la entrada a coordenadas del tablero
            start, end = self.parse_input(move_input)

            if start is None or end is None:
                continue

            # Intentar mover la pieza
            try:
                piece = self.board.get_piece(start[0], start[1])
                if piece is None:
                    print("No hay una pieza en la posición de inicio.")
                    continue
                
                # Verificar que la pieza pertenece al jugador actual
                if piece.color != self.current_turn:
                    print(f"Es el turno de las {self.current_turn}. No puedes mover las piezas del oponente.")
                    continue

                # Mover la pieza si es válido
                self.board.move_piece(start[0], start[1], end[0], end[1])

                # Cambiar de turno
                self.switch_turn()

            except ValueError as e:
                print(f"Movimiento no válido: {e}")

if __name__ == '__main__':
    game = ChessGame()
    game.play()

            