from board import Tablero
from movimientos import MovimientoPiezas

class ChessGame:
    def __init__(self):
        self.tablero = Tablero()
        self.turno_actual = "Blanco"
        self.ganador = None
        self.reglas_movimiento = MovimientoPiezas()

    # Mueve una pieza de una casilla a otra. Valida si es posible.
    def realizar_movimiento(self, fila_origen, col_origen, fila_destino, col_destino):

        # Mensaje de error en caso de movimiento inválido
        mensaje_error = ""

        pieza_origen = self.tablero.get_piece(fila_origen, col_origen)
        casilla_destino = self.tablero.get_piece(fila_destino, col_destino)

        # Verificar si la casilla de origen tiene una pieza
        if pieza_origen is None:
            mensaje_error = "PiezaInexistente"

        # Verificar si la pieza seleccionada pertenece al jugador en turno
        elif pieza_origen.get_color() != self.turno_actual:
            mensaje_error = "TurnoIncorrecto"

        # Comprobar si la casilla de destino es la misma que la de origen
        elif fila_origen == fila_destino and col_origen == col_destino:
            mensaje_error = "CasillaInvalida"

        # Verificar si la casilla destino está ocupada por una pieza del mismo color
        elif casilla_destino is not None and casilla_destino.get_color() == self.turno_actual:
            mensaje_error = "CasillaOcupada"

        # Si se detecta un error, retornamos el mensaje de error
        if mensaje_error != "":
            return mensaje_error

        # Si todo está correcto, verificamos si el movimiento es válido
        return self.validar_movimiento(casilla_destino, fila_origen, col_origen, fila_destino, col_destino)

    # Habilita el movimiento si es válido
    def validar_movimiento(self, casilla_destino, fila_origen, col_origen, fila_destino, col_destino):

        # Verificar si el movimiento cumple con las reglas
        resultado = self.evaluar_movimiento(self.tablero.get_positions(), fila_origen, col_origen, fila_destino, col_destino)
        if resultado == "MovimientoInvalido":
            return "MovimientoInvalido"

        # Si la pieza en destino es el rey enemigo, finaliza el juego
        if casilla_destino is not None and casilla_destino.get_name() == "Rey" and casilla_destino.get_color() != self.turno_actual:
            self.ganador = self.turno_actual
            return "ReyCapturado"

        # Si todo está correcto, mueve la pieza y cambia el turno
        self.tablero.set_positions(fila_origen, col_origen, fila_destino, col_destino)
        self.cambiar_turno()
        return "MovimientoValido"

    def obtener_reglas(self):
        return self.reglas_movimiento

    # Cambia el turno entre los jugadores
    def cambiar_turno(self):
        self.turno_actual = "Negro" if self.turno_actual == "Blanco" else "Blanco"

    def obtener_tablero(self):
        return self.tablero

    def obtener_turno_actual(self):
        return self.turno_actual

    def obtener_ganador(self):
        return self.ganador

    # Determina si el movimiento cumple con las reglas de la pieza seleccionada
    def evaluar_movimiento(self, posiciones, fila_origen, col_origen, fila_destino, col_destino):
        nombre_pieza = posiciones[fila_origen][col_origen].get_name()
        reglas = self.reglas_movimiento

        # Verifica movimientos específicos según la pieza
        if nombre_pieza == "Torre":
            return reglas.movimiento_recto(posiciones, fila_origen, col_origen, fila_destino, col_destino)

        elif nombre_pieza == "Caballo":
            return reglas.movimiento_caballo(posiciones, fila_origen, col_origen, fila_destino, col_destino)

        elif nombre_pieza == "Alfil":
            return reglas.movimiento_diagonal(posiciones, fila_origen, col_origen, fila_destino, col_destino)

        elif nombre_pieza == "Reina":
            return reglas.movimiento_reina(posiciones, fila_origen, col_origen, fila_destino, col_destino)

        elif nombre_pieza == "Rey":
            return reglas.movimiento_rey(posiciones, fila_origen, col_origen, fila_destino, col_destino)

        elif nombre_pieza == "Peon":
            return reglas.movimiento_peon(posiciones, fila_origen, col_origen, fila_destino, col_destino)

        # Devuelve "Valido" o "MovimientoInvalido"
        return "MovimientoInvalido"
