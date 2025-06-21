def sumar_hasta_llegar_a_suma_final (vector_inicial, vector_solucion, suma_final, suma_parcial, indice_vector_inicial):
	for i in range(2): #la condicion si lo incluyo o no. i=0 incluyo. i=1 no incluyo
		vector_solucion[indice_vector_inicial] = i # se guarda la solucion parcial
		suma_parcial = suma_parcial + (vector_inicial[indice_vector_inicial] * i) # multiplicamos por i para decidir si lo incluimos o no
		
		#caso base
		if(indice_vector_inicial == len(vector_inicial) - 1): 
			print("Caso base alcanzado: ", vector_solucion)
			
			if(suma_parcial == suma_final): 
				# si es solucion
				print("Solucion encontrada: ", vector_solucion)

		elif(suma_parcial <= suma_final):
				
				# no estamos al final del vector y la suma parcial es menor que la suma final, seguimos iterando ese subarbol
				print("Recursividad: ", vector_solucion, "Suma parcial: ", suma_parcial)
				sumar_hasta_llegar_a_suma_final(vector_inicial, vector_solucion, suma_final, suma_parcial, indice_vector_inicial + 1)
		
vector_inicial = [2, 3, 10, 15]
suma_final = 12
vector_solucion_inicializado = [0] * len(vector_inicial)
sumar_hasta_llegar_a_suma_final(vector_inicial, vector_solucion_inicializado, suma_final, 0, 0)

# condicion: si lo incluyo o no en la suma
# donde y como el backtracking: si sumaParcial <= sumaFinal
# caso base para la solucion: si llegamos al final del vector
# es_solucion: si sumaParcial == sumaFinal

