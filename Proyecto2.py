#Crear el tablero
Tablero = [["0" for _ in range(8)] for _ in range(8)]

#Conocer el índice/letra de la columna
letrasColumnas = "abcdefgh"

def indiceColumna(letra):
    if letra in letrasColumnas:
        return letrasColumnas.index(letra)
    
    else:
        print("Letra no válida")
        return -1

#Poner una pieza en el tablero
def piezaTablero(tablero, pieza, color, posicion):
    fila = int(posicion[1]) - 1
    columna = indiceColumna(posicion[0])

    if fila >= 0 and columna >= 0:
        tablero[fila][columna] = (pieza, color)

#Validar la posición de la pieza en el tablero
def checkPosicion(posicion, filas, columnas):
    if len(posicion) != 2:
        return False
    
    fila = int(posicion[1])
    columna = indiceColumna(posicion[0])
    return 1 <= fila <= filas and 0 <= columna < columnas

#Saber si un espacio está vacío
def espacioVacio(tablero, posicion):
    fila = int(posicion[1]) - 1
    columna = indiceColumna(posicion[0])
    return tablero[fila][columna] == "0"

#Saber si la posición de la pieza a evaluar fue ingresada
def evaluarPieza(tablero, posicion):
    fila = int(posicion[1]) - 1
    columna = indiceColumna(posicion[0])
    return tablero[fila][columna] != "0"

#Movimientos correctos de una pieza
def movimientosPieza(tablero, piezaPosicion, filas, columnas):
    filaPieza = int(piezaPosicion[1]) - 1
    columnaPieza = indiceColumna(piezaPosicion[0])
    movimientos = []

    #Mover hacia arriba
    for fila in range(filaPieza - 1, -1, -1):
        if tablero[fila][columnaPieza] == "0":
            movimientos.append(letrasColumnas[columnaPieza] + str(fila + 1))
        
        else:
            movimientos.append(letrasColumnas[columnaPieza] + str(fila + 1))
            break

    #Mover hacia abajo
    for fila in range(filaPieza + 1, filas):
        if tablero[fila][columnaPieza] == "0":
            movimientos.append(letrasColumnas[columnaPieza] + str(fila + 1))
        
        else:
            movimientos.append(letrasColumnas[columnaPieza] + str(fila + 1))
            break

    #Mover hacia la izquierda
    for columna in range(columnaPieza - 1, -1, -1):
        
        if tablero[filaPieza][columna] == "0":
            movimientos.append(letrasColumnas[columna] + str(filaPieza + 1))
        
        else:
            movimientos.append(letrasColumnas[columna] + str(filaPieza + 1))
            break

    #Mover hacia la derecha
    for columna in range(columnaPieza + 1, columnas):
        
        if tablero[filaPieza][columna] == "0":
            movimientos.append(letrasColumnas[columna] + str(filaPieza + 1))
        
        else:
            movimientos.append(letrasColumnas[columna] + str(filaPieza + 1))
            break

    return movimientos

#Mostrar el tablero
def mostrarTablero(tablero):
    for fila in tablero:
        
        fila_str = ["[{}]".format("_" if casilla == "0" else casilla[0]) for casilla in fila]
        print(" ".join(fila_str))

#Datos ingresados por el usuario
def main():
    filas = 8
    columnas = 8
    tablero = [["0" for _ in range(columnas)] for _ in range(filas)]

    #Poner piezas en el tablero
    Piezas = int(input("Ingrese el número de piezas a agregar: "))
    for _ in range(Piezas):
        piezas = ["rey" , "dama" , "torre" , "alfil" , "caballo" , "peón"]
        tipoPieza = input("Ingrese el tipo de pieza: ")

        while tipoPieza not in piezas:
            print("Ingrese una pieza válida")
            tipoPieza = input("Ingrese el tipo de pieza: ")
            
        #Elegir color de las piezas
        colores = ["blanco", "negro"]
        colorPieza = input("Ingrese el color de la pieza: ")
        
        while colorPieza not in colores:
            print("Ingrese un color válido")
            colorPieza = input("Ingrese el color de la pieza: ")

        #Elegir posición de las piezas
        while True:
            posicionPieza = input("Ingrese la posición de la pieza en el tablero (ej: a1, e4, f8): ")
            
            if not checkPosicion(posicionPieza, filas, columnas):
                print("Posición inválida.")
                continue

            if not espacioVacio(tablero, posicionPieza):
                print("Hay una pieza en esa posición.")
                continue
            break

        piezaTablero(tablero, tipoPieza, colorPieza, posicionPieza)

    #Ingresar posición de la torre
    while True:
        piezaPosicion = input("Ingrese la posición de la torre a evaluar: ")

        if not checkPosicion(piezaPosicion, filas, columnas):
            print("Posición inválida.")
            continue

        if not evaluarPieza(tablero, piezaPosicion):
            print("No hay una pieza en esa posición.")
            continue
        break

    #Mostrar movimientos válidos de la pieza
    movPieza = movimientosPieza(tablero, piezaPosicion, filas, columnas)
    print("\nMovimientos válidos de la pieza seleccionada:")
    
    for movimiento in movPieza:
        print(movimiento)

    #Mostrar el tablero (opcional)
    print("\nTablero:")
    mostrarTablero(tablero)

#Sin esto NO corre el código :)
if __name__ == "__main__":
    main()