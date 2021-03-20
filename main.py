# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def DisplayBoard(board):
    print("""
    +-------+-------+-------+
    |       |       |       |
    |   """, board[1], """   |   """, board[2], """   |   """, board[3], """   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   """, board[4], """   |   """, board[5], """   |   """, board[6], """   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   """, board[7], """   |   """, board[8], """   |   """, board[9], """   |
    |       |       |       |
    +-------+-------+-------+
    """, sep="")


def EnterMove():
    global board
    if (VictoryFor(board, 'X') == 0):
        print("\n\nEl juego termino, maquina gana")
        return 0  # se termina el juego
    if (len(MakeListOfFreeFields(board)) == 0):
        print("\n\nEl juego termino, no hay mas espacios")
        return 0  # se termina el juego
    while True:  # bucle hasta indicar movimiento
        a = int(input("\n\tIngresar movimiento:"))
        if (a in MakeListOfFreeFields(board)):
            break  # acepta movimiento
    board[a] = 'O'
    if (VictoryFor(board, 'O') == 0):
        DisplayBoard(board)
        print("\n\nEl juego termino, Jugador gana")
        return 0  # se termina el juego
    return VictoryFor(board, 'O')


#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#

def MakeListOfFreeFields(board):
    lista = []
    for x, y in board.items():
        if (y != 'X' and y != 'O'):
            lista.append(x)
    return lista


#
# la función examina el tablero y construye una lista de todos los cuadros vacíos
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#

def VictoryFor(board, sign):
    if (board[1] == sign and board[4] == sign and board[7] == sign):
        return 0
    elif (board[2] == sign and board[5] == sign and board[8] == sign):
        return 0
    elif (board[3] == sign and board[6] == sign and board[9] == sign):
        return 0
    elif (board[1] == sign and board[5] == sign and board[9] == sign):
        return 0
    elif (board[3] == sign and board[5] == sign and board[7] == sign):
        return 0
    elif (board[1] == sign and board[2] == sign and board[3] == sign):
        return 0
    elif (board[4] == sign and board[5] == sign and board[6] == sign):
        return 0
    elif (board[7] == sign and board[8] == sign and board[9] == sign):
        return 0
    else:
        return 1


#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
# devuelve 0 si alguien gana


def maquina():
    global board
    print("\n\tTurno de la maquina\n")
    if (1 in MakeListOfFreeFields(board) and 9 in MakeListOfFreeFields(board)):
        board[1] = 'X'
        return
    elif (1 in MakeListOfFreeFields(board) and board[9] == 'X'):
        board[1] = 'X'
        return
    elif (9 in MakeListOfFreeFields(board) and board[1] == 'X'):
        board[9] = 'X'
        return  # primer diagonal
    elif (3 in MakeListOfFreeFields(board) and 7 in MakeListOfFreeFields(board)):
        board[3] = 'X'
        return
    elif (3 in MakeListOfFreeFields(board) and board[7] == 'X'):
        board[3] = 'X'
        return
    elif (7 in MakeListOfFreeFields(board) and board[3] == 'X'):
        board[7] = 'X'
        return  # segunda diagonal
    elif (2 in MakeListOfFreeFields(board) and 8 in MakeListOfFreeFields(board)):
        board[2] = 'X'
        return
    elif (2 in MakeListOfFreeFields(board) and board[8] == 'X'):
        board[2] = 'X'
        return
    elif (8 in MakeListOfFreeFields(board) and board[2] == 'X'):
        board[8] = 'X'
        return  # vertical medio
    elif (4 in MakeListOfFreeFields(board) and 6 in MakeListOfFreeFields(board)):
        board[4] = 'X'
        return
    elif (4 in MakeListOfFreeFields(board) and board[6] == 'X'):
        board[4] = 'X'
        return
    elif (6 in MakeListOfFreeFields(board) and board[4] == 'X'):
        board[6] = 'X'
        return  # horizontal medio
    else:
        for i in range(1, 10):
            if (i in MakeListOfFreeFields(board)):
                board[i] = 'X'
                return  # rellena el primer blanco que encuentra


#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#

board = {1: 1, 2: 2, 3: 3, 4: 4, 5: 'X', 6: 6, 7: 7, 8: 8, 9: 9}
DisplayBoard(board)
while EnterMove():
    DisplayBoard(board)
    maquina()
    DisplayBoard(board)

input("Presiona para salir")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# hola soy mati
