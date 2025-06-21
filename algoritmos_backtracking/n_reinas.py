"""
entrada: array de N posiciones. 
	en cada posicion irá el nro de la fila donde se ubica la reina.
condiciones: 
	1) no deben comerse las reinas entre si
	2) una reina come a otra si estan en la misma: fila, columna, diagonal
backtracking: si no se puede poner una reaina en una fija. se vuelve atrás.
caso base: si hay lamisma cantidad de reinas puestas que el tamaño del tablero (N)
array = [2,1,0,3] es equivalente a | 0 0 1 0 |
                                   | 0 1 0 0 |
                                   | 1 0 0 0 |
								   | 0 0 0 1 |
"""
def n_reinas(array, fila):
	array.append(fila) # ponemos una reina en la fila de la columna actual
	if()

	


array = [0] * 8 # tablero de 8x8 
n_reinas(array, 0)