'''
Dado un conjunto de numeros enteros, queremos dividirlo en dos subconjuntos de modo que la
diferencia absoluta de la suma de los elementos de los dos conjuntos sea la minima posible.
Si la cantidad del conjunto es par, entonces el modulo de cada subconjunto serán iguales a 
la cantidad / 2.
Si la cantidad del conjunto es impar, entonces el modulo de un conjunto será igual a la 
(cantidad de numeros - 1) / 2, y el otro será igual a la (cantidad+1) /2
Describa una estrategia de backtracking.

Ejemplos:
Si conjunto = {3,4,5,-3,100,1,89,54,23,20}
Si conjunto = {1,0,1,1,0,0,1,1,0,0}
|conjunto| = 10
|subconjunto1| = |subconjunto2| = 10/2 = 5
subconjunto1 = {4,100,1,23,20}
subconjunto2 = {3,5,-3,89,54}
La suma da 148

Si conjunto = {23,45,-34,12,0,98,-99,4,189,-1,4}
|conjunto| = 11
|subconjunto1| = 5
|subconjunto2| = 6
subconjunto1 = {45,-34,12,98,-1}
subconjunto2 = {23,0,-99,4,189,4}
Las sumas dan 120 y 121 respectivamente
'''

def division_dif_minima(conjunto, etapa, subconjunto, diferencia, cant0, cant1):
	max0 = len(conjunto) // 2
	max1 = len(conjunto) - max0

	if cant0 > max0 or cant1 > max1:
		return diferencia

	# caso base, llegue al final del conjunto
	if etapa == len(conjunto):
		diferencia = min(diferencia, abs(sumar(conjunto, subconjunto, 0) - sumar(conjunto, subconjunto, 1)))
		if diferencia == abs(sumar(conjunto, subconjunto, 0) - sumar(conjunto, subconjunto, 1)):
			print(f"subconjunto:", subconjunto)
			print(f"diferencia minima: ", diferencia)
		return diferencia

	# los 0 seran un conjunto y los 1 otro.
	for i in range(2):
		subconjunto.append(i)
		nuevo_cant0 = cant0
		nuevo_cant1 = cant1
		if i == 0:
			nuevo_cant0 = cant0 + 1
		else: 
			nuevo_cant1 = cant1 + 1
		
		diferencia_hija = division_dif_minima(conjunto, etapa+1, subconjunto, diferencia, nuevo_cant0, nuevo_cant1)
		diferencia = min(diferencia, diferencia_hija)

		subconjunto.pop()	

	return diferencia
		
def sumar(conjunto, subconjunto, nro):
	suma = 0
	for i in range(len(subconjunto)):
		if subconjunto[i] == nro:
			suma = suma + conjunto[i]
	return suma

conjunto = [3,4,5,-3,100,1,89,54,23,20]
maximo = float('inf')
print(f"final: ",division_dif_minima(conjunto, 0, [], maximo, 0, 0))