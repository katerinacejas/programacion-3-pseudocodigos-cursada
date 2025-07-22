'''
La raíz cuadrada entera de un número n es el máximo valor entero u tal que u^2 ≤ n. 
Por ejemplo, la raíz entera de 18 es 4 y la de 9 es 3.
Esto es porque ( 4^2 ≤ 18 < 5^2 )  y  ( 3^2 ≤ 9 < 4^2 )
Esto es porque ( 4*4 ≤ 18 < 5*5 )  y  ( 3*3 ≤ 9 < 4*4 )

Por supuesto, esto se podía resolver en tiempo O(n) comenzando en 0 y recorriendo secuencialmente
los números hasta encontrar el que buscamos. Queremos algo más eficiente.
Describa una estrategia divide-and-conquer para encontrar la raíz cuadrada de un número disponiendo 
únicamente de la posibilidad de utilizar las cuatro operaciones aritméticas básicas (no podemos
calcular directamente la raíz cuadrada) en tiempo mejor que lineal.
'''

def calcular_raiz_cuadrada_entera(nro):
	print(raiz_cuadrada_entera(nro, 0, nro))

def raiz_cuadrada_entera(nro, inicio, fin):
	if inicio >= fin:
		return fin
	
	mid = (inicio + fin) // 2

	# caso base, encontre la raiz cuadrada entera
	if mid*mid <= nro and (mid+1)*(mid+1) > nro:
		return mid
	
	else:
		if mid*mid > nro:
			return raiz_cuadrada_entera(nro, inicio, mid)
		else:
			return raiz_cuadrada_entera(nro, mid+1, fin)

calcular_raiz_cuadrada_entera(10)

'''
a: cantidad de veces que se llama a la recursividad
b: en cuantas unidades disminuye la entrada
k: grado del polinomio, es deir, las sentencias que se ejecutan fuera del llamado recursivo
a = 1
b = 2
k = 0
b^k = 2^0 = 1 = a
--> complejidad temporal = O(n^0 * log(n)) --> O(log(n)) < O(n) --> cumple con el requisito
'''