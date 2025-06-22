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
def n_reinas(tamanio, fila=0, array=[]):
	# caso base: si ya llene todo el array
	if tamanio == fila:
		imprimir_tablero(array, tamanio)
		return 
	
	for columna in range(tamanio):
		if verificar_filas(array, columna) and verificar_diagonales(array, fila, columna):
			array.append(columna) # ponemos una reina
			print("puse una reina")
			n_reinas(tamanio, fila+1, array)
			array.pop() # sacamos una reina. backtracking

def verificar_filas(array, col):
	print("ingrese a verificar filas")
	for columna in array:
		if columna == col: 
			return False
		
	print("return true verificar filas")
	return True

def verificar_diagonales(array, fila, columna):
	for i, c in enumerate(array):
		if abs(c - columna) == abs(i - fila):
			return False

	print("return true verificar diagonales")
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

n_reinas(4)