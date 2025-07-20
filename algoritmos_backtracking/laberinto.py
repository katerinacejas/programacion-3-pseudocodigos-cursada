'''
Un laberinto L es una matriz de m filas y n columnas con números 0 y 1.
Un 0 denota una posición por la que se puede pasar y un 1 denota una posición 
por la que no se puede pasar. La entrada del laberinto está en la posición L[0, 0]
 y la salida en la posición L[m - 1, n - 1].

Queremos saber si existe un camino desde la entrada del laberinto (asumimos 
L[0, 0] = 0) hasta la salida (asumimos igualmente L[m-1, n-1] = 0).

El camino debe cumplir el requisito de que sólo se permiten desplazamientos 
hacia la derecha o hacia abajo; nunca hacia arriba ni hacia la izquierda.

Describa una estrategia de backtracking y su pseudocodigo que determine si existe
un camino desde la entrada hasta la salida. No es necesario que se dé el camino
de escape, es suficiente con decidir si existe o no un camino.

Cada nueva posición se puede considerar como una nueva posición inicial, desde la cual queremos 
saber si existe o no, un camino a la salida. Observe tambien que si se encuentra una trayectoria a la 
salida, no es necesario seguir explorando otras trayectorias. 

condicion:
parametros: el laberinto, la entrada, la salida, (ambos en posicion i y posicion j), y el conjunto solucion
como mostrar solucion: una lista de las posiciones en las que se puede pasar para salir del laberinto
donde y como se hace backtracking:
caso base:
la entrada va a ser la "etapa"
'''

def laberinto(lab):
    entrada = 0
    salida_i = len(lab)-1
    salida_j = len(lab[0])-1
    resolver_laberinto(lab, entrada, entrada, salida_i, salida_j, [])
    

def resolver_laberinto(lab, entrada_i, entrada_j, salida_i, salida_j, solucion):
    solucion.append([entrada_i, entrada_j])
    
    # caso base, encontramos la salida del laberinto
    if entrada_i == salida_i and entrada_j == salida_j:
        print("encontramos la solucion")
        print(f"solucion encontrada es: ", solucion)
        return

    # PODA DE FACTIBILIDAD: caso, lo siguiente es una pared y fuera del laberinto en alguno de los dos ejes
    if es_un_lateral_sin_salida(lab, entrada_i, entrada_j, salida_i, salida_j) == True:
        print("encontramos un lateral del laberinto sin salida")
        return 
    
	# PODA DE FACTIBILIDAD: caso, no se puede ir ni abajo ni a la derecha, no hay salida por ahí
    if entrada_i == salida_i and entrada_j != salida_j:
        if lab[entrada_i][entrada_j+1] == 1:
            print("no se puede avanzar ni abajo ni a la derecha")
            return 
    elif entrada_i != salida_i and entrada_j == salida_j:
        if lab[entrada_i+1][entrada_j] == 1:
            print("no se puede avanzar ni abajo ni a la derecha")
            return 
        
	# si aun no resolvimos el laberinto, y no estamos en un sin salida, seguimos buscando

	# caso, puedo ir abajo
    if entrada_i < salida_i and lab[entrada_i+1][entrada_j] == 0:
        resolver_laberinto(lab, entrada_i+1, entrada_j, salida_i, salida_j, solucion)
        solucion.pop() 
        print("backtracking, retrocedo")
    
	# caso, puedo ir a la derecha:
    if entrada_j < salida_j and lab[entrada_i][entrada_j+1] == 0:
        resolver_laberinto(lab, entrada_i, entrada_j+1, salida_i, salida_j, solucion)
        solucion.pop() 
        print("backtracking, retrocedo")
    
    

def es_un_lateral_sin_salida(lab, entrada_i, entrada_j, salida_i, salida_j):
    #estoy en el lateral abajo y no hay salida para la derecha
	if entrada_i == salida_i and entrada_j < salida_j and lab[entrada_i][entrada_j+1] == 1:
		return True
    
	# estoy en el lateral de la derecha y no hay salida para abajo
	if entrada_j == salida_j and entrada_i < salida_i and lab[entrada_i+1][entrada_j] == 1:
		return True

	# no es un lateral sin salida
	return False

# laberinto de 3 x 4
lab = [
                    [0,1,0,0],
                    [0,0,1,0],
                    [1,0,0,0]
]

laberinto(lab)

