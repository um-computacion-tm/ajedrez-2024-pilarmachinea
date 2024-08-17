from chess import Chess

def main():
    chess = Chess()
    while True:
        play(chess)
        move = input("Introduce tu movimiento o quit para salir: ")
        if move == "quit":
            break

def play(chess):
    try:
        print(chess.sh)
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To row: "))
        to_col = int(input("To col: "))
        chess.move(from_row, from_col, to_row, to_col)

    except Exception as e:
        print("Error, asegurate introducir un movimiento valido")


if __name__ == "__main__":
    main()