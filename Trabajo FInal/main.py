from chess import ChessGame
from board import Board

def print_instructions():
    """
    Imprime las instrucciones para jugar el juego.
    """
    print("Bienvenido al juego de Ajedrez en consola!")
    print("Para mover una pieza, introduce el comando en el formato 'E2 E4'.")
    print("Escribe 'salir' para terminar el juego.")
    print()

def parse_input(input_str):
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

def main():
    """
    Función principal para ejecutar el juego de ajedrez.
    """
    board = Board()
    print_instructions()
    
    # Inicializar el turno con las blancas
    current_turn = 'white'

    while True:
        board.print_board()
        print(f"Turno de las {current_turn}.")
        
        # Pedir al jugador que ingrese un movimiento
        move_input = input("Introduce tu movimiento: ")
        
        if move_input.lower() == 'salir':
            print("Gracias por jugar!")
            break
        
        # Convertir la entrada a coordenadas del tablero
        start, end = parse_input(move_input)
        
        if start is None or end is None:
            continue

        # Intentar mover la pieza
        try:
            piece = board.get_piece(start[0], start[1])
            if piece is None:
                print("No hay una pieza en la posición de inicio.")
                continue
            
            # Verificar que la pieza pertenece al jugador actual
            if piece.color != current_turn:
                print(f"Es el turno de las {current_turn}. No puedes mover las piezas del oponente.")
                continue
            
            # Mover la pieza si es válido
            board.move_piece(start[0], start[1], end[0], end[1])
            
            # Cambiar de turno
            current_turn = 'black' if current_turn == 'white' else 'white'
        
        except ValueError as e:
            print(f"Movimiento no válido: {e}")

if __name__ == '__main__':
    main()


if __name__ == "__main__":
    main()