def max_min_vector_rotad (lista, inicio, fin):
    if inicio >= fin:
        return lista[inicio]
    else:
        mid = (inicio + fin) // 2
        max_min_vector_rotad(lista, inicio, mid)
        max_min_vector_rotad(lista, mid+1, fin)

        if lista[fin] < lista[inicio]:
            return f"el mayor es el {lista[inicio]} y el menor es el {lista[fin]}"
        
lista= [4,5,6,0,1,2]
print(max_min_vector_rotad(lista, 0, len(lista)-1))