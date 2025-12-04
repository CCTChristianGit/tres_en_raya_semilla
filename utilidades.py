def comprobar_ganador(x, y, tablero):

    # ¿Qué casilla tenemos que comprobar?
    jugador = tablero[x][y]
    print("Voy a comprobar ", jugador, "(jugador) en:\nColumna:", x, ", Fila:", y)
    print()

    ##########################################
    # Miramos hacia la izquierda y derecha
    victoria_lateral = True

    for col in range(3):
        if tablero[x][col] != jugador:
            victoria_lateral = False
    
    if victoria_lateral:
        return f"Victoria en la Fila {x}"
    ##########################################
    # Miramos hacia abajo
    victoria_columna = True

    for fila in range(3):
        if tablero[fila][y] != jugador:
            victoria_lateral = False

    if victoria_columna:
        return f"Victoria en la Columna {y}"
    ##########################################
    # Diagonal

    if x == y: 
        victoria_diagonal = True
        for i in range(3):
            if tablero[i][i] != jugador:
                victoria_diagonal = False

    if victoria_diagonal:
            return f"Victoria en la diagonal {x},{y}"

    return False


def mostrar_tablero(tablero):
    for linea in tablero:
        print(linea)

# X --> 1
# O --> -1
# - --> 0
def convertir_tablero(tablero):
    nuevo_tablero = []
    for i in tablero:
        lista_aux = []
        for j in i:
            if j == "X":
                lista_aux.append(1)
            elif j == "O":
                lista_aux.append(-1)
            else:
                lista_aux.append(0)

        nuevo_tablero.append(lista_aux)

    return(nuevo_tablero)
    ##########################################
    #TODO: Convertirlo a una lista de listas
    # ej: [[1,1,0], [1,-1,-1], [0, 0, 0]]

    return nuevo_tablero
