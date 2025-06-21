algoritmo busquedaBinaria(int[] u[0..n − 1], int ini, fin, x)
{
	if (ini > fin)
	{ // primer caso base
		return false;
	}
	else if (ini == fin)
	{ // segundo caso base
		return (u[ini] == x);
	}
	else
	{ // quedan dos o más elementos
		mid = (ini + fin) / 2;
		if (x == u[mid])
		{ // tercer caso base
			return true;
		}
		else if (x > u[mid])
		{ // mitad derecha
			return BinSearch(u, mid + 1, fin, x)
		}
		else
		{ // mitad izquierda
			return BinSearch(u, ini, mid − 1, x)
		}
	}
}

algoritmo bubbleSort(int[] u[0..n − 1])
{
	for (i = n − 1; i > 0; i - -)
	{
		for (j = 0; j < i; j++)
		{
			if (u[i] < u[j])
			{
				int aux = u[i] u[i] = u[j] u[j] = aux
			}
		}
	}
}

algoritmo insertionSort(int[] u[0..n − 1])
{
	for (i = 1; i < n; i++)
	{
		for (j = i; j > 0, j - -)
		{
			if (u[j] < u[j − 1])
			{
				int aux = u[j − 1] u[j − 1] = u[j] u[j] = aux
			}
		}
	}
}

Algoritmo MergeSort(int[] u[0..n - 1], int ini, fin)
{
	if (ini < fin)
	{
		int mid = (ini + fin) / 2;
		MergeSort(u, ini, mid);
		MergeSort(u, mid + 1, fin);
		Merge(u, ini, fin);
	}
}

Algoritmo Merge(int[] u[0..n − 1], int ini, fin)
{
	w = int[0..fin − ini];
	int mid = (ini + fin) / 2;
	i = ini;
	j = mid + 1;
	for (k = 0; ≤ fin − ini; k++)
	{
		if ((j > fin) || (u[i] ≤ u[j] && i < mid + 1))
		{
			w[k] = u[i];
			i++;
		}
		else
		{
			w[k] = u[j];
			j++;
		}
	}
	for (k = 0; k ≤ fin − ini; k++)
	{
		u[ini + k] = w[k];
	}
}

QuickSort(u[1...n], ini, fin) {
  if ini < fin:
    int p = Pivot(u, ini, fin) // particiona y devuelve la posición final del pivot
    QuickSort(u, ini, p-1)     // ordena la parte izquierda
    QuickSort(u, p+1, fin)     // ordena la parte derecha
}

Pivot(u, ini, fin) {
	// Se elije el primer elemento como pivot
	p = u[ini]           
	i = ini + 1
	j = fin

	// Mueves i hacia la derecha hasta encontrar algo > pivot
	while i ≤ fin and u[i] ≤ p:
		i++

	// Mueves j hacia la izquierda hasta encontrar algo ≤ pivot
	while u[j] > p:
		j--

	// Mientras no se crucen, intercambias u[i] y u[j] y sigues
	while i < j:
		int aux = u[j];
		u[j] = u[i];
		u[i] = aux;
	
		// reajustas i y j de la misma forma
		while i ≤ fin and u[i] ≤ p: 
			i++
		while u[j] > p:
			j--

	// Llegaste al cruce: colocas el pivot en su lugar
	u[ini] = u[j];
	u[j] = p;
	return j    // j es ahora la posición «definitiva» del pivot
}

bool Algoritmo Palindrome (int [ ] u[0..n − 1], int ini, fin) { //realizado con divide and conquer
	if (ini ≥ fin) {
		return true;
	} else if (u[ini] ̸= u[fin]) {
		return false;
	} else {
		return Palindrome(u, ini + 1, fin − 1);
	}
}

int Algoritmo Fib (int n) { // realizado con divide and conquer
	if (n ≤ 1) { // casos base
		return n;
	} else {
		return Fib(n − 1)+Fib(n − 2);
	}
}


int Algoritmo Cambio(int monto) { //input: monto. output: numero de monedas
	int cantidadMonedasUsadas = 0;
	int montoPagado = 0;
	int i = 0;
	int monedas[] = [500, 200, 100, 50, 20, 10, 5, 1];
	while (montoPagado < monto ) && (i < monedas.length) {
		if (montoPagado + monedas[i] <= montoPagado) {
			montoPagado = montoPagado + monedas[i];
			cantidadMonedasUsadas++; //mayor moneda que podemos usar
		}
		else {
			i++; //seguimos buscando
		}
	}
	if (i < monedas.length) 
		return cantidadMonedasUsadas; //devolvemos el numero de monedas usadas
	else return -1 // no hay solucion
}

struct objetosGreedy {
	int valor;
	int peso;
}

float [] ordenar(objetosGreedy [] objetos) { // O(n log(n))
	float[] ordenados = new float[objetos.length]
	for (int i = 0; i<objetos.length; i++) {
		ordenados[i] = objetos[i].peso / objetos[i].valor;
	}
	sort(ordenados);
	return ordenados;
}

float [] Algoritmo MochilaGreedy (objetosGreedy[ ] objetos, int max) { 
// objetos[i].peso, objetos[i].valor
	float[] conjuntoSolucion; // la salida
	float[] objetosOrdenados = ordenar(objetos); // O(n log(n))
	for(int i =0; i<objetos.length; i++){ // Θ(n) : inicializo el conjunto solucion
		conjuntoSolucion[i] = 0
	}
	i=0
	int accum = 0
	while( accum < max) && (i < objetos.length){ // Θ(n)
		conjuntoSolucion[i] = min(1, (max − accum)/objetos[i].peso)
		accum = accum + (conjuntoSolucion[i] ∗ objetos[i].peso)
		i++
	}
	return conjuntoSolucion;
}

// ESQUEMA GENERICO DE GREEDY
Algoritmo GreedyGenerico:
	input: conjuntoCandidatos[]
	output: conjuntoSolucion[] //conjunto solucion del problema
	while conjuntoCandidatos no sea vacío Y NO funcionSolucion(conjuntoSolucion):
		x = funcionSeleccion(conjuntoCandidatos)
		conjuntoCandidatos = conjuntoCandidatos/x
		if funcionFactibilidad(conjuntoSolucion union x):
			conjuntoSolucion = conjuntoSolucion union x
	if funcionSolucion(conjuntoSolucion):
		return conjuntoSolucion
	else
		return "No hay solucion"

// ALGORITMO DIJKSTRA CASO 2: 
// retorna el grafo con el camino minimo desde el vertice origen hacia todos los demas
struct GrafoTDA {
	int [] vertices;
	int [] aristas;
}

algoritmo Dijkstra (GrafoTDA grafoInicial, int verticeOrigen) {
	int []visitados = {verticeOrigen}
	GrafoTDA grafoFinal = inicializarGrafo() // inicializa el grafo solución
	foreach vertice in grafoInicial.vertices {
		grafoFinal.agregarVertice(vertice) // Los nodos de grafoInicial
	}
	foreach vertice ∈ grafoInicial.vecindario(verticeOrigen) {
		grafoFinal.agregarArista(verticeOrigen, vertice, grafoInicial.peso(verticeOrigen, vertice))
	}
	int []candidatos = inicializarConjunto() // Nodos candidatos
	candidatos = grafoInicial.vertices \ visitados //el operador \ realiza una resta de conjuntos
	while !candidatos.conjuntoVacio() {
		int min = infinito
		int nodoAux;
		foreach nodo ∈ candidatos {
			if (grafoFinal.existeArista(verticeOrigen, nodo) && 
				grafoFinal.peso(verticeOrigen, nodo) < min) {
					min = grafoFinal.peso(verticeOrigen, nodo)
					nodoAux = nodo
			}
		}
		visitados.agregarVertice(nodoAux)
		candidatos.sacar(nodoAux)
		int[] candidatosAux = copiar(candidatos)
		int nodoAux2;
		while !candidatosAux.conjuntoVacio() {
			nodoAux2 = candidatosAux.elegir()
			candidatosAux.sacar(nodoAux2)
			if (grafoInicial.existeArista(nodoAux, nodoAux2)) {
				if(grafoFinal.existeArista(verticeOrigen, nodoAux2)) {
					if(grafoFinal.peso(verticeOrigen, nodoAux) + grafoInicial.peso(nodoAux, nodoAux2)
						< grafoFinal.peso(verticeOrigen, nodoAux2)) {
							grafoFinal.agregarArista(nodoAux, nodoAux2, grafoInicial.peso(nodoAux, nodoAux2))
							grafoFinal.eliminarArista(verticeOrigen, nodoAux2)
					}
				}
				else {
					grafoFinal.agregarAristaI(nodoAux, nodoAux2, grafoInicial.peso(nodoAux, nodoAux2))
				}
			}
		}
	}
	return grafoFinal
}

// ALGORITMO PRIM
arbol Prim (int [n][n] matrizGrafo) { // n es la cantidad de nodos que tiene el grafo
	arbol arbolPrim = null // el arbol que retornará la funcion.
	for (int i = 0; i < n; i++) { 
		//en este bucle se inicializan los vectores masCercano y minDist
		// haciendo que el vertice 0 sea el primer elegido y que entonces el vertice
		// mas cercano de cualquier candidato con el 0 sea el 0 por no haber ninguno mas
		// y por lo tanto la minima distnacia va a ser la arista que tengan entre esos
		// candidatos y el vertice 0 por ser el unico.
		masCercano[i] = 0
		minDist[i] = matrizGrafo[0][i]
	}
	repeat n-1 veces { // en cada iteracion se agrega un vertice al arbol.
		// se repite hasta que no haya mas vertices que agregar, por lo tanto n-1 veces
		min = infinito
		for (int j=0; j<n; j++){ //se busca el vertice mas proximo
			if (0 <= minDist[j] < min) { 
				//evaluo que sea mayor o igual a 0 para evitar los -1 que ya fueron agregados
				min = minDist[j]
				verticeNuevo = j
			}
		}
		arbolPrim = arbolPrim union {(masCercano[verticeNuevo],verticeNuevo)} //añadir la arista al arbol
		minDist[verticeNuevo] = -1 //se agrega verticeNuevo al arbol
		for (j = 0; j<n; j++) { //se recalculan las distancias
			// es decir, se actulizan los vecinos de K.
			if (matrizGrafo[verticeNuevo][j] < minDist[j]) {
				minDist[j] = matrizGrafo[verticeNuevo][j]
				masCercano[j] = verticeNuevo
			}
		}
	}
	return arbolPrim	
}

//ALGORITMO KRUSKAL
struct Grafo {
	array vertices;
	lista aristas;
}
struct aristaCola {
	int nodoOrigen;
	int nodoDestino;
}
arbol Kruskal (Grafo grafo) {
	arbol = inicializarConjunto(); //arbol.length() = 0
	listaAristas = inicializarCola();
	listaAristas = insertarOrdenadas(grafo.aristas);
	cantidadNodos = grafo.vertices.length()

	forEach vertice in grafo.vertices {
		vertice.inicializarConjunto(); // crea los arboles triviales, uno por cada vertice
	}

	while (arbol.length() != cantidadNodos-1){
		aristaCola arista = listaAristas.primero() //la arista candidata con menor costo
		listaAristas.eliminarPrimero();
		nodoOrigen = buscar(arista.nodoOrigen);
		nodoDestino = buscar(arista.nodoDestino);
		if (nodoOrigen != nodoDestino){
			combinar(nodoOrigen, nodoDestino) //fusiona los dos arboles triviales
			arbol = arbol union {(arista)} //añade la arista al arbol
		}
	}
	return arbol;
}
















