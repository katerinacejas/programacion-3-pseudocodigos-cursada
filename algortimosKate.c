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


int Algoritmo Cambio(int v) { //input: monto. output: numero de monedas
	int n = 0;
	int accum = 0;
	int i = 0;
	int coins[] = [500, 200, 100, 50, 20, 10, 5, 1];
	while (accum < v ) && (i < length(coins)) {
		if (accum + coins[i] <= v) {
			accum = accum + coins[i];
			n = n+1; //mayor moneda que podemos usar
		}
		else {
			i = i+1; //seguimos buscando
		}
	}
	if (i < length(coins )) 
		return n; //devolvemos el numero de monedas usadas
	else return -1 // no hay solucion
}

float [] Algoritmo Knapsack (obj [ ] O, int max) { // O[i].weight, O[i].value
	float[]R // la salida
	sort O by value / weight // Θ(n log n)
	for(i=0; i<n; i++){ // Θ(n)
		R[i] = 0
	}
	i=0
	int accum = 0
	while( accum < max) && (i < n){ // Θ(n)
		R[i] = min(1, (max − accum)/O[i].weight)
		accum = accum + R[i] ∗ O[i].weight
		i++
	}
	return R
}


























