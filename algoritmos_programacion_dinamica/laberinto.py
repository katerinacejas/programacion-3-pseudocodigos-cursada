'''
Un laberinto L es una matriz de m filas y n columnas con números 0 y 1.
Un 0 denota una posición por la que se puede pasar y un 1 denota una posición 
por la que no se puede pasar. La entrada del laberinto está en la posición L[0, 0]
y la salida en la posición L[m - 1, n - 1].

Queremos saber si existe un camino desde la entrada del laberinto (asumimos 
L[0, 0] = 0) hasta la salida (asumimos igualmente L[m-1, n-1] = 0).

El camino debe cumplir el requisito de que sólo se permiten desplazamientos 
hacia la derecha o hacia abajo; nunca hacia arriba ni hacia la izquierda.

Encuentre una estrategia de programación dinámica que decida si es
posible llegar desde la entrada del laberinto hasta su salida.

Ayuda: es posible construir una matriz booleana A del mismo tamaño que el laberinto. 
Una casilla de esta matriz tendrá el valor true si la casilla correspondiente del laberinto 
es accesible desde la entrada y false si no lo es. 

Las reglas de construcción se pueden definir inductivamente:
1) La entrada es accesible (o sea, debe ser A[0, 0] == true).
2) Una casilla cualquiera A[i, j] es accesible si y sólo si se puede llegar a ella en un paso 
desde una casilla accesible y L[i, j] == 0.

El problema se reduce entonces a determinar si la salida del laberinto es accesible.
'''


def laberinto(lab):
	# creo la matriz booleana con todo False por default donde guardar las soluciones parciales
	m = len(lab)
	n = len(lab[0])
	matriz_accesible = [[False]*n for _ in range(m)]

	for i in range(len(lab)): # itero indice de filas de 0 a n-1
		for j in range(len(lab[i])): # itero indice de columnas de 0 a n-1
			# es el inicio, caso base
			if i == 0 and j == 0: 
				matriz_accesible[0][0] = True

			# no es inicio, averiguo si es una casilla accesible
			elif es_accesible(lab, i, j, matriz_accesible) == True: 
				matriz_accesible[i][j] = True
			else:
				matriz_accesible[i][j] = False
	
	for i in range(len(lab)):
		print(lab[i])
	for i in range(len(matriz_accesible)):
		print(matriz_accesible[i])

	if matriz_accesible[len(lab)-1][len(lab[i])-1] == True:
		print("tiene solucion")
	else: print("no tiene solucion")

def es_accesible(lab, i, j, matriz_accesible):
	if lab[i][j] == 1: # es una pared
		return False
	else: # no es una pared
		if i == 0: # es la primer fila
			return matriz_accesible[i][j-1]
		elif j == 0: # es la primer columna
			return matriz_accesible[i-1][j]
		else: # estoy en el medio del laberinto
			return matriz_accesible[i-1][j] or matriz_accesible[i][j-1]

# laberinto de 3 x 4
lab = [
                    [0,1,0,0],
                    [0,1,1,0],
                    [0,0,0,0]
]

laberinto(lab)