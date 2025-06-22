"""
entrada: array de N posiciones. 
	en cada posicion irá el nro de la fila donde se ubica la reina.
condiciones: 
	1) no deben comerse las reinas entre si
	2) una reina come a otra si estan en la misma: fila, columna, diagonal
backtracking: si no se puede poner una reaina en una fija. se vuelve atrás.
caso base: si hay lamisma cantidad de reinas puestas que el tamaño del tablero (N)
array = [2,1,0,3] es equivalente a | 0 0 1 0 |  = columna 0 1 2 3
                                   | 0 0 0 0 |       fila 2 3 0 3
                                   | 1 0 0 0 |
								   | 0 1 0 1 |
"""
def n_reinas(array, fila):
	# caso base: si ya llene todo el array
	if len(array)-1 == fila:
		imprimir_tablero(array, len(array))
		return 
	
	for columna in range(len(array)):
		if verificar_filas(array, fila) and verificar_diagonales(array, fila, columna):
			array.append(fila) # ponemos una reina
			print("puse una reina")
			n_reinas(array, fila+1)
			array.pop() # sacamos una reina. backtracking

def verificar_filas(array, fila):
	print("ingrese a verificar filas")
	for columna in range(len(array)):
		if array[columna] == fila: 
			return False
	return True

def verificar_diagonales(array, fila, columna):
	for i in range(len(array)):
		if abs(array[i]-columna) == abs(i - fila):
			return False
	return True

def imprimir_tablero(tablero, n):
    for fila in range(n):
        linea = ''
        for col in range(n):
            if tablero[fila] == col:
                linea += 'Q '
            else:
                linea += '. '
        print(linea)
    print() 

array = [0,0,0,0] # tablero de 4x4
n_reinas(array, 0)