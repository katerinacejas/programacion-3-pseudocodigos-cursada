'''
    algoritmo para ordenar una lista de numeros utilizando la tecnica de merge sort
    divide el array (divide) en mitades hasta llegar a un caso base (array de solo
    1 elemento) y luego mergea (and conquer) los elementos ordenandolos hasta tener
    la lista final
'''

def merge_sort(lista):
    inicio = 0
    fin = len(lista) -1
    # caso base lista vacia
    if fin < 0:
        return "la lista esta vacia"
    
    # si la lista no esta vacía:
    print(resolver_merge_sort(lista, inicio, fin))

def resolver_merge_sort(lista, inicio, fin):
    # caso base, lista de solo 1 elemento
    if inicio == fin:
        return lista[inicio]
    
    # dividir la lista en mitades
    mid = (inicio + fin) // 2
    resolver_merge_sort(lista, inicio, mid)
    resolver_merge_sort(lista, mid+1, fin)

    # merge ordenado
    ordenados = []
    izquierda = lista[inicio:mid+1]
    derecha = lista[mid+1:fin+1]
    indice_izq = 0
    indice_der = 0

    # ordeno uno a uno en las dos mitades, salgo del bucle cuando una de las mitades ya
    # fue ordenada por completa
    while indice_izq < len(izquierda) and indice_der < len(derecha):
        if izquierda[indice_izq] <= derecha[indice_der]:
            ordenados.append(izquierda[indice_izq])
            indice_izq = indice_izq + 1
        else:
            ordenados.append(derecha[indice_der])
            indice_der = indice_der + 1
        print(ordenados)
    
    # si la mitad que no se completó de ordenar es la izquierda:
    if indice_izq < len(izquierda):
        for nro in izquierda[indice_izq:]:
            ordenados.append(nro)
    
    # si la mitad que no se completó de ordenar es la derecha:
    if indice_der < len(derecha):
        for nro in derecha[indice_der:]:
            ordenados.append(nro)

    # piso lista por ordenados
    for i in range(len(ordenados)):
        lista[inicio + i] = ordenados[i]

lista = [4,2,8,5,6,3,9,1,0]
merge_sort(lista)   