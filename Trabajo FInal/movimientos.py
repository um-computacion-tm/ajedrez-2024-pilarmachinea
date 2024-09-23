#calcula la raíz cuadrada de un número.
from math import sqrt

class MovimientoPiezas:
    
    def __init__(self):
        pass

    # Calcula la diferencia entre las coordenadas de origen y destino
    def calcular_diferencia(self, fila_inicio, col_inicio, fila_fin, col_fin):
        dif_fila = abs(fila_fin) - abs(fila_inicio)
        dif_columna = abs(col_fin) - abs(col_inicio)
        return [dif_fila, dif_columna]

    # Evalúa si el movimiento es diagonal (usado por alfiles y reinas)
    def evaluar_movimiento_diagonal(self, tablero, posiciones, fila_inicio, col_inicio, fila_fin, col_fin):
        reglas = MovimientoPiezas()
        diferencias = reglas.calcular_diferencia(fila_inicio, col_inicio, fila_fin, col_fin)

        if abs(diferencias[0]) == abs(diferencias[1]):
            entradas = [fila_inicio, col_inicio, fila_fin, col_fin]
            return tablero.verificar_camino_libre(posiciones, diferencias, entradas)

        return "Movimiento Inválido"

    # Revisa si alguna casilla en el camino del movimiento diagonal está ocupada
    def verificar_camino_libre(self, posiciones, diferencias, entradas):
        origen = posiciones[entradas[0]][entradas[1]]
        incremento_fila = self.calcular_incremento(diferencias[0])
        incremento_col = self.calcular_incremento(diferencias[1])

        resultado = "Válido"
        for casilla in range(1, abs(diferencias[0]) + 1, abs(incremento_fila)):
            if casilla == abs(diferencias[0]) and posiciones[entradas[2]][entradas[3]] is not None:
                if posiciones[entradas[2]][entradas[3]].get_color() != origen.__color__:
                    resultado = "Válido"
                    break

            if posiciones[entradas[0] + (casilla * incremento_fila)][entradas[1] + (casilla * incremento_col)] is not None:
                resultado = "Movimiento Inválido"
                break

        return resultado

    # Calcula el incremento de movimiento en el método de verificación de camino
    def calcular_incremento(self, valor):
        return int(valor / abs(valor))

    # Movimiento en línea recta (utilizado por torres y reinas)
    def movimiento_recto(self, tablero, posiciones, fila_inicio, col_inicio, fila_fin, col_fin):
        reglas = MovimientoPiezas()
        if fila_inicio == fila_fin or col_inicio == col_fin:
            if fila_inicio == fila_fin:
                return reglas.movimiento_horizontal(posiciones, fila_inicio, col_inicio, fila_fin, col_fin)
            elif col_inicio == col_fin:
                return reglas.movimiento_vertical(posiciones, fila_inicio, col_inicio, fila_fin, col_fin)
        return "Movimiento Inválido"

    # Verifica el movimiento horizontal
    def movimiento_horizontal(self, tablero, posiciones, fila_inicio, col_inicio, fila_fin, col_fin):
        pieza = posiciones[fila_inicio][col_inicio]
        paso = 1 if col_fin > col_inicio else -1

        for i in range(col_inicio + paso, col_fin + paso, paso):
            if posiciones[fila_inicio][i] is None:
                if i == col_fin:
                    return "Válido"
                continue
            if posiciones[fila_inicio][i] is not None:
                if i == col_fin and posiciones[fila_inicio][i].get_color() != pieza.__color__:
                    return "Válido"
                return "Movimiento Inválido"

    # Verifica el movimiento vertical
    def movimiento_vertical(self, tablero, posiciones, fila_inicio, col_inicio, fila_fin, col_fin):
        pieza = posiciones[fila_inicio][col_inicio]
        if fila_fin > fila_inicio:
            paso = 1
        else:
            paso = -1

        for i in range(fila_inicio + paso, fila_fin + paso, paso):
            if posiciones[i][col_inicio] is None:
                if i == fila_fin:
                    return "Válido"
                continue
            if posiciones[i][col_inicio] is not None:
                if i == fila_fin and posiciones[i][col_inicio].get_color() != pieza.__color__:
                    return "Válido"
                return "Movimiento Inválido"

    # Movimientos del peón
    def mover_peon(self, tablero, posiciones, fila_inicio, col_inicio, fila_fin, col_fin):
        datos = MovimientoPiezas.preparar_movimiento_peon(posiciones, fila_inicio, col_inicio, fila_fin, col_fin)
        if datos[0].get_color() == "Blanco":
            direccion = 1 
        else: 
            direccion = -1

        if datos[0].get_initial_position():
            if datos[1] == (2 * direccion) and datos[2] == 0 and datos[3] is None:
                datos[0].set_initial_position(False)
                return "Válido"

        if datos[1] == direccion:
            if datos[2] != 0 and datos[3] is not None:
                if sqrt(datos[1]**2 + datos[2]**2) == sqrt(2):
                    return MovimientoPiezas.validar_comer_peon(datos)

            if datos[2] == 0 and datos[3] is None:
                datos[0].set_initial_position(False)
                return "Válido"

        return "Movimiento Inválido"

    # Prepara los datos para mover un peón
    def preparar_movimiento_peon(posiciones, fila_inicio, col_inicio, fila_fin, col_fin):
        pieza_inicial = posiciones[fila_inicio][col_inicio]
        mov_fila = fila_fin - fila_inicio
        mov_columna = col_fin - col_inicio
        destino = posiciones[fila_fin][col_fin]
        return [pieza_inicial, mov_fila, mov_columna, destino]

    # Valida si un peón puede comer otra pieza
    def validar_comer_peon(datos):
        if datos[3].get_color() != datos[0].get_color():
            datos[0].set_initial_position(False)
            return "Válido"
        return "Movimiento Inválido"
