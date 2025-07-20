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

Ayuda: Cada nueva posición se puede considerar como una nueva posición inicial,
desde la cual queremos saber si existe o no, un camino a la salida. Observe tambien
que si se encuentra una trayectoria a la salida, no es necesario seguir explorando
otras trayectorias. 

condicion:
parametros: el laberinto, la entrada, la salida, (ambos en posicion i y posicion j),
            y el conjunto solucion
como mostrar solucion: una lista de las posiciones en las que se puede pasar para
                        salir del laberinto
donde y como se hace backtracking:
caso base:
la entrada va a ser la "etapa"
'''

def laberinto(lab):
    entrada = 0
    salida = len(lab)-1
    solucion = resolver_laberinto(lab, entrada, entrada, salida, salida, [[0,0]]) 
    if solucion != None:
        print("la solucion del laberinto es:")
        print(solucion)
        return
    print("no hubo solucion")
    

def resolver_laberinto(lab, entrada_i, entrada_j, salida_i, salida_j, solucion):
    # caso base
    if entrada_i == salida_i and entrada_j == salida_j:
        print("encontramos la solucion")
        solucion.append([salida_i, salida_j])
        return

    # caso base, nos fuimos del laberinto
    if entrada_i > salida_i or entrada_j > salida_j:
        

    # si aun no encontramos la salida


# laberinto de 3 x 4
lab = [
                    [0,1,0,0],
                    [0,0,0,1],
                    [0,1,0,0]
]

laberinto(lab)

