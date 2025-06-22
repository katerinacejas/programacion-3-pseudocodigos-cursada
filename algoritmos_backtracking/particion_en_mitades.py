'''
Dado un conjunto de n enteros se desea encontrar, si existe, una particion en dos
subconjuntos disjuntos, tal que la suma de sus elementos sea la misma.

conjunto = [2,5,1,7,6,9]
una solucion sería sum[2,5,1,7] = 15 y  sum[6,9] = 15 

conjunto = [4,3,4,5]
una solucion seria sum[4,4] = 8 y sum[3,5] = 8

'''

def particion_en_mitades(conjunto):
    total = sum(conjunto)
    #una poda anticipada, si no se puede dividir por 2 sin que haya resto, entonces no hay dos conjuntos que puedan tener la suma de la mitad
    if total % 2 != 0:
        print("No hay solucion (suma total impar).")
        return
    objetivo = total // 2
    resolver(conjunto, [], 0)

def resolver(conjunto, solucion, etapa):
    # aca voy agregando los numeros iterando con i = 0 o 1
    for i in range(2):
        solucion.append(i)
        if(len(solucion) > len(conjunto)):
            return
        #caso base: cuando la etapa es la ultima del conjunto
        if etapa == len(conjunto)-1:
            suma1 = 0
            suma2 = 0
            for nro in range(len(conjunto)):
                if solucion[nro] == 1: 
                    suma1 += conjunto[nro]
                else:
                    suma2 += conjunto[nro]
            if suma1 == suma2:
                print("hay solucion: cada subconjunto suma: ", suma1)
                print(solucion)
                print(conjunto)
                return
            else:
                solucion.pop()
        
        # aun quedan nros del conjunto por agregar al conjunto solucion
        else:
            #aumentamos la etapa
            resolver(conjunto, solucion, etapa+1)
            solucion.pop()


conjunto = [4,3,4,9,3,3,3,0,1,2,5,3,2]
particion_en_mitades(conjunto)