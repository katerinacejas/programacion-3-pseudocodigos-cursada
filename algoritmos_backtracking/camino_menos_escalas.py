'''
Dado un sistema de rutas aereas modelado mediante un grafo, determine la ruta 
que contenga la minima cantidad de escalas entre un par de ciudades dadas.
'''
def camino_menos_escalas(grafo, origen, destino):
    cola.encolar(origen)
    visitados.add(origen)
    
    while(no_este_vacia(cola)):
        nodo = cola.primero()
        cola.desencolar(nodo)

        #caso base, se encontró el destino
        if(nodo == destino):
            return nodo
        
        adyacentes = grafo.get_adyacentes(nodo)

        while(no_este_vacio(adyacentes)):
            nodo_adyacente = elegir(adyacentes)
            adyacentes.eliminar(nodo_adyacente)

            if no_pertenece(nodo_adyacente, visitados):
                cola.encolar(nodo_adyacente)
                visitados.add(nodo_adyacente)