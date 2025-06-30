'''
Se busca encontrar un elemento en una lista o arreglo que aparezca más de la mitad
del tiempo. Es decir, si un elemento es mayoritario, significa que aparece más 
veces que cualquier otro elemento en la lista. Y aparece por lo menos n/2 + 1 veces 
en un array, siendo n-1 la cantidad de elementos del array.

'''

def elemento_mayoritario(lista):
    inicio = 0
    fin = len(lista)-1
    print(resolver_elemento_mayoritario(lista, inicio, fin))

def resolver_elemento_mayoritario(lista, inicio, fin):
    # caso base, si la lista tiene solo 1 elemento
    if inicio == fin:
        return lista[inicio]
    
    #aun no analizamos toda la lista
    mid = (inicio + fin) // 2
    izquierda_mayoritario = resolver_elemento_mayoritario(lista, inicio, mid)
    derecha_mayoritario = resolver_elemento_mayoritario(lista, mid+1, fin)

    if izquierda_mayoritario == derecha_mayoritario:
        return izquierda_mayoritario
    
    izquierda_count = 0
    for i in range(len(lista)):
        if lista[i] == izquierda_mayoritario:
            izquierda_count = izquierda_count + 1

    derecha_count = 0
    for i in range(len(lista)):
        if lista[i] == derecha_mayoritario:
            derecha_count = derecha_count + 1
    
    if izquierda_count >= (len(lista) / 2) + 1:
        return izquierda_mayoritario
    
    if derecha_count >= (len(lista) / 2) + 1:
        return derecha_mayoritario
    
    return "no hay elemento mayoritario"

lista = [1,2,1,1,1,9,9,9,9,9,9,9,9]
elemento_mayoritario(lista)