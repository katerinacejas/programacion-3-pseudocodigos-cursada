'''
Basicamente se basa en entender que cada objeto puede estar o no estar en 
la solucion, que la suma de pesos no sobrepase la capacidad de la mochila y 
que la suma de valores sea maxima. La solucion seria un vector booleano 
o un vector con 0's y 1's

Encontrar el subconjunto de objetos cuya suma de pesos no exceda 
la capacidad C y cuyo valor total sea máximo.
'''
def mochila(capacidad_maxima, objetos):
    # objetos sería una lista de objetos que tienen atributo el peso y el valor
    # objetos[1].peso y objetos[2].valor
    solucion = []
    etapa = 0
    resolver_mochila(capacidad_maxima, objetos, etapa, solucion, 0, 0)

def resolver_mochila(capacidad_maxima, objetos, etapa, solucion, peso_solucion, valor_solucion): 
    # etapa sería el objeto a analizar
    if etapa == len(objetos)-1:
        return solucion
    
    for i in range(2):
        # i = 0 no lo agrega
        # i = 1 lo agrega
        solucion.add(i)
        peso_solucion = peso_solucion + objetos[etapa].peso
        valor_solucion = valor_solucion + objetos[etapa].valor

        if peso_solucion <= capacidad_maxima:
            if etapa < len(objetos)-1:
                resolver_mochila(capacidad_maxima, objetos, etapa+1, solucion, peso_solucion, valor_solucion)
                solucion.pop()  
    return solucion

        
        

