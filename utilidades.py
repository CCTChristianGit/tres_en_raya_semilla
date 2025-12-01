def comprobar_ganador(x, y, tablero):

    # ¿Qué casilla tenemos que comprobar?
    jugador = tablero[x][y]
    print("Voy a comprobar ", jugador, " en ", x, ",", y)

    ##########################################
    # Miramos hacia la izquierda y derecha
    victoria_lateral = True

    for fila in tablero:
        for col in fila:
            if 
    
    if victoria_lateral:
        return True
    ##########################################
    # Miramos hacia abajo
    victoria_columna = True

    # TODO: comprobacion
    pass

    if victoria_columna:
        return True
    ##########################################
    # Diagonal
    victoria_diagonal = True
        

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
