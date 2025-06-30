'''
    encontrar un elemento especifico en una lista ordenada de elementos
'''
def buscar(elemento_a_buscar, lista):
    inicio = 0
    fin = len(lista) -1
    if (fin < 0):
        # la lista esta vacia, entonces el elemento no puede existir en la lista
        print("lista vacia, el elemento no se encuentra")
        return
    busqueda_binaria(elemento_a_buscar, inicio, fin, lista)


def busqueda_binaria(elemento_a_buscar, inicio, fin, lista):
    # case base: si inicio y fin son iguales, significa que es la ultima iteracion posible
    if (inicio == fin):
        # caso base existe el elemento
        if elemento_a_buscar == lista[inicio]:
            print(f"Se encontro el elemento {elemento_a_buscar} en la ubicacion {inicio} de la lista {lista}")
            return
        # caso base no existe el elemento
        else:
            print(f"El elemento {elemento_a_buscar} no se encuentra en la lista {lista}")
            return
    
    else:
        #aun no se encontró el elemento. 
        # uso el operador // para quedarme siempre con la parte entera de la division.
        mitad = ((inicio + fin) // 2) 
        
        if elemento_a_buscar <= lista[mitad]:
            # si el elemento a buscar esta en la parte izquierda del indice mitad en la lista
            # entoncecs inicio sigue siendo inicio
            # y fin pasa a ser mitad
            busqueda_binaria(elemento_a_buscar, inicio, mitad, lista)
        else:
            # hago mitad + 1 porque sería mayor a mitad,
            busqueda_binaria(elemento_a_buscar, mitad + 1, fin, lista)

lista = [5,8,13,14,15,26, 99]
elemento_a_buscar = 195
buscar(elemento_a_buscar, lista)