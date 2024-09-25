from cli import Cli
from exceptions import InvalidMove, InvalidMoveNoPiece, InvalidMoveIndexError, InvalidMoveOutOfBounds, InvalidMoveSameColor, InvalidMoveSamePlace

def iniciar_juego():
    jugador = Cli()
    jugador.comenzar()

    while True:
        try:
            entrada_usuario = input("Introduce tu movimiento (o quit para salir): ")  # Obtiene entrada del usuario
            if entrada_usuario.lower() == "quit":  # Verifica si la entrada es "QUIT"
                print("Gracias por jugar. ¡Hasta luego!")
                break  # Sale del bucle y termina el juego

            # Asumiendo que la entrada tiene el formato "E2 E4" o similar
            movimientos = entrada_usuario.split()
            if len(movimientos) != 2:
                print("Entrada no válida. Asegúrate de usar el formato correcto.")
                continue
            
            origen, destino = movimientos[0], movimientos[1]

            resultado_movimiento = jugador.chess.realizar_movimiento(origen, destino)

            if resultado_movimiento == "ReyCapturado":
                print("¡El rey ha sido capturado! Fin de la partida.")
                print("El jugador ganador es: " + jugador.chess.obtener_ganador())
                break

            # Limpiar la pantalla al finalizar cada turno (si tienes esta función)
            jugador.limpiar_pantalla()

            # Mostrar el nuevo estado del tablero
            jugador.mostrar_tablero()

        except ValueError as error:
            print("Entrada no válida. Se esperaba un movimiento en el formato E2 E4.")
        except Exception as error:  # Maneja cualquier otra excepción
            print(error)

if __name__ == '__main__':
    iniciar_juego()
