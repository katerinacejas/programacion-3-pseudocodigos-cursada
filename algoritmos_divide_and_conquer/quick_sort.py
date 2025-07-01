'''
    ordenar una lista de numeros realizando el metodo quick sort de divide and conquer

'''

def quick_sort(lista):
    inicio = 0
    fin = len(lista) - 1

    # caso base de lista vacia
    if fin < 0:
        print("la lista esta vacia")
        return
    
    #caso base lista de solo 1 elemento, no hay que ordenar
    if fin == 0:
        print("La lista tiene solo 1 elemento")
        return
    print(lista)
    resolver_quick_sort(lista, inicio, fin)
    print(f"lista ordenada: \n{lista}")

def resolver_quick_sort(lista, inicio, fin):    
    # decidi que para esta implementacion, mi pivot va a ser siempre el ultimo elemento
    # de la lista a ordenar

    # caso base, llegamos a una lista de un solo elemento
    if inicio >= fin:
        return

    pivot = lista[fin]
    indice = inicio -1

    # desde inicio hasta fin-1 porque no incluimos el pivot que es fin
    for j in range(inicio, fin):
        if lista[j] <= pivot:
            indice = indice +1
            aux = lista[j]
            lista[j] = lista[indice]
            lista[indice] = aux
            print(lista)

    # reubico el pivot en su nuevo lugar ordenado
    lista[fin] = lista[indice+1]
    lista[indice+1] = pivot
    
    #resolver para la izquierda del pivot
    resolver_quick_sort(lista, inicio, indice)

    #resolver para la derecha del pivot
    resolver_quick_sort(lista, indice+2, fin)

lista = [4,2,1,8,5,6]
quick_sort(lista)